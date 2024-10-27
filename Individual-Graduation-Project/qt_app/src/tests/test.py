from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor
from pydub import AudioSegment
import torch
import numpy as np

device = "cuda:0" if torch.cuda.is_available() else "cpu"
torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32

model_id = "openai/whisper-large-v3"
model = AutoModelForSpeechSeq2Seq.from_pretrained(
    model_id, torch_dtype=torch_dtype, low_cpu_mem_usage=True, use_safetensors=True
)
model.to(device)

processor = AutoProcessor.from_pretrained(model_id)

# Установка языка транскрипции (например, русский)
forced_decoder_ids = processor.get_decoder_prompt_ids(language="ru", task="transcribe")

def transcribe_audio(file_path):
    # Загрузка и конвертация аудио в массив чисел
    audio = AudioSegment.from_file(file_path)
    samples = np.array(audio.get_array_of_samples()).astype(np.float32)

    # Обеспечение правильного формата (2D массив для модели)
    input_features = processor(samples, return_tensors="pt", sampling_rate=audio.frame_rate).input_features
    input_features = input_features.to(device)

    # Генерация текста с использованием forced_decoder_ids
    generated_ids = model.generate(
        input_features,
        forced_decoder_ids=forced_decoder_ids,
        max_new_tokens=128,
    )
    transcription = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
    return transcription

# Пример использования
transcription = transcribe_audio("audio_recordings/123.wav")
print("Транскрипция:", transcription)
