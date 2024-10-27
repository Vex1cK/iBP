from PySide6.QtCore import QThread, Signal, Slot, QObject
from scipy.io.wavfile import write
from src.config import AUDIO_PATH
from datetime import datetime
from time import sleep
import soundcard as sc
import numpy as np
import threading
import logging
import os


class Recorder(QObject):
    data_is_saving = Signal()
    data_saved = Signal()

    def __init__(self, sample_rate, interval, root=AUDIO_PATH):
        super().__init__()
        self.sample_rate = sample_rate
        self.interval = interval
        self.num_frames = self.sample_rate * self.interval
        self.root = root
        self.recording = threading.Event()
        self.data_out = []
        self.data_in = []
        self.max_int16 = np.iinfo(np.int16).max
        self.recording_bool = False
        self.need_to_save = True

    def record_output(self):
        with sc.get_microphone(id=str(sc.default_speaker().name), include_loopback=True).recorder(samplerate=self.sample_rate) as mic:
            while self.recording.is_set():
                self.data_out.append(mic.record(numframes=self.num_frames))

    def record_input(self):
        mic = sc.default_microphone()
        with mic.recorder(samplerate=self.sample_rate) as recorder:
            while self.recording.is_set():
                self.data_in.append(recorder.record(numframes=self.num_frames))

    def stop_recording_input(self):
        input("Нажмите Enter для завершения записи...")
        self.recording.clear()
        logging.info("Остановка...")

    def stop_recording(self):
        self.recording_bool = True
        while self.recording_bool:
            sleep(0.01)
        self.recording.clear()
        self.data_is_saving.emit()
        # logging.info("Остановка записи...")

    def save_data(self):
        if self.need_to_save:
            # Конвертация данных и объединение их
            data_out_combined = np.concatenate(self.data_out, axis=0)
            data_in_combined = np.concatenate(self.data_in, axis=0)

            data_int16_out = (data_out_combined * self.max_int16).astype(np.int16)
            data_int16_in = (data_in_combined * self.max_int16).astype(np.int16)

            if data_int16_out.shape[0] != data_int16_in.shape[0]:
                min_length = min(data_int16_out.shape[0], data_int16_in.shape[0])
                data_int16_out = data_int16_out[:min_length]
                data_int16_in = data_int16_in[:min_length]


            all_data = np.concatenate((data_int16_out, data_int16_in), axis=1)

            output_file = os.path.join(self.root, (datetime.now().__str__().split('.')[0].replace(':', '-') + '.wav'))  # unique path
            with open(output_file, 'w') as file:  # to create file
                ...
            write(output_file, self.sample_rate, all_data)
            logging.info("Audio file saved")

            self.data_in = []
            self.data_out = []
        else:
            logging.info("Audio file not saved (not need)")
        self.data_saved.emit()
    
    def start_recording(self):
        self.recording.set()
    
        thread_out = threading.Thread(target=self.record_output)
        thread_in = threading.Thread(target=self.record_input)
        thread_stop = threading.Thread(target=self.stop_recording)
        if __name__ == '__main__':
            thread_stop = threading.Thread(target=self.stop_recording_input)
        
        thread_out.start()
        thread_in.start()
        thread_stop.start()

        thread_stop.join()
        thread_out.join()
        thread_in.join()

        self.save_data()


class RecorderThread(QThread):
    data_is_saving = Signal()
    data_saved = Signal()

    def __init__(self, sample_rate, interval, parent=None):
        super().__init__(parent)
        self.sample_rate = sample_rate
        self.interval = interval
        self.recorder = Recorder(sample_rate, interval)
        self.recording = False

        self.recorder.data_saved.connect(self.on_data_saved)
        self.recorder.data_is_saving.connect(self.on_data_is_saving)

    def run(self):
        self.recorder.start_recording()

    def start_recording(self):
        if not self.recording:
            self.recording = True
            self.start()

    def stop_recording(self, need_to_save=True):
        if self.recording:
            self.recorder.recording_bool = False
            self.recording = False
        self.recorder.need_to_save = need_to_save
    
    @Slot()
    def on_data_is_saving(self):
        self.data_is_saving.emit()
        logging.info(f"data_is_saving emitted in RecorderThread")
    
    @Slot()
    def on_data_saved(self):
        self.data_saved.emit()
        logging.info(f"data_saved emitted in RecorderThread")
        


# if __name__ == "__main__":
#     sample_rate = 44100
#     sec = 3

#     recorder = Recorder(sample_rate, sec)
#     inp = input("Нажмите Enter для начала записи: ")

#     while "-" not in inp:
#         recorder.start_recording()
#         inp = input("Нажмите Enter для начала записи: ")