import logging
logger = logging.getLogger(__name__)

import os
import asyncio
import math
from concurrent.futures import ThreadPoolExecutor
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline
from pydub import AudioSegment
import torch
import warnings

from config import PATH_TO_OUTPUTS_FILES, PATH_TO_A2T_MODEL

warnings.filterwarnings("ignore", category=FutureWarning, message=".*inputs.*deprecated.*input_features.*instead")
warnings.filterwarnings("ignore", message=".*flash attention.*")


class AudioToTextAsync:
    def __init__(self, model_name="openai/whisper-large-v3", segment_length=15 * 60 * 1000):
        logger.debug(f"AudioToTextModel starting initialization| chache: {PATH_TO_A2T_MODEL}")
        self.path_to_model = PATH_TO_A2T_MODEL
        self.model_name = model_name
        self.device = ("cuda:0" if torch.cuda.is_available() else "cpu")
        logger.debug(f"Device: {self.device}")
        self.torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32

        self.model = AutoModelForSpeechSeq2Seq.from_pretrained(
            self.path_to_model, cache_dir=self.path_to_model, torch_dtype=self.torch_dtype,
            low_cpu_mem_usage=True, use_safetensors=True, local_files_only=True
        )
        self.model.to(self.device)
        self.processor = AutoProcessor.from_pretrained(self.path_to_model,
                                                       cache_dir=self.path_to_model, local_files_only=True)

        self.transcriber = pipeline(
            "automatic-speech-recognition",
            model=self.model,
            tokenizer=self.processor.tokenizer,
            feature_extractor=self.processor.feature_extractor,
            torch_dtype=self.torch_dtype,
            device=self.device,
        )
        self.segment_length = segment_length  # Длина сегмента в миллисекундах
        logger.debug("AudioToTextModel initialized")

        # ThreadPoolExecutor для выполнения блокирующих операций в потоках
        self.executor = ThreadPoolExecutor(max_workers=4)

    def split_audio(self, file_path):
        """
        Разделяет аудиофайл на сегменты заданной длины.
        :param file_path: Путь к исходному аудиофайлу.
        :return: Список путей к сегментам.
        """
        logger.debug(f"Splitting audio file {file_path}...")
        audio = AudioSegment.from_file(file_path)
        total_length = len(audio)
        num_segments = math.ceil(total_length / self.segment_length)

        base_name, ext = os.path.splitext(file_path)
        output_files = []

        for i in range(num_segments):
            start_time = i * self.segment_length
            end_time = min((i + 1) * self.segment_length, total_length)
            segment = audio[start_time:end_time]

            segment_file = f"{base_name}_segment_{i + 1}{ext}"
            segment.export(segment_file, format=ext[1:])
            output_files.append(segment_file)
            logger.info(f"Segment {i + 1} saved in: {segment_file}")

        logger.debug(f"Audio file {file_path} has been split into {num_segments} segments")
        return output_files

    def transcribe_segment(self, segment):
        """
        Транскрибирует один аудиосегмент в текст.
        :param segment: Путь к аудиосегменту.
        :return: Расшифрованный текст.
        """
        logger.debug(f"Transcribing segment {segment}...")
        result = self.transcriber(segment, generate_kwargs={"language": "russian", "forced_decoder_ids": None})
        return result['text']

    async def transcribe_audio(self, file_path, output_name, save_segments_files=False):
        """
        Асинхронная транскрипция аудиофайла.
        :param file_path: Путь к исходному аудиофайлу.
        :param output_name: Название выходного файла.
        :param save_segments_files: Сохранять ли сегменты после обработки.
        """

        loop = asyncio.get_event_loop()

        output_path = os.path.join(PATH_TO_OUTPUTS_FILES, output_name)

        # Разделение аудио на сегменты
        segments_files = await loop.run_in_executor(self.executor, self.split_audio, file_path)
        full_text = ""

        # Асинхронная транскрипция каждого сегмента
        for segment in segments_files:
            segment_text = await loop.run_in_executor(self.executor, self.transcribe_segment, segment)
            full_text += segment_text + "\n"

            # Сохранение текста в файл
            try:
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(full_text)
            except Exception as e:
                logger.error(f"Error saving text to file: {e}")
                return False, str(e)

        logger.debug(f"The transcription is complete. The text is saved in {output_path}")

        # Удаление сегментов, если нужно
        if not save_segments_files:
            logger.debug("Deleting segment files...")
            try:
                for segment in segments_files:
                    os.remove(segment)
                    logger.debug(f"File {segment} has been deleted")
            except Exception as e:
                logger.error(f"Error deleting segment files: {e}")
                return False, str(e)

        return True, output_path
