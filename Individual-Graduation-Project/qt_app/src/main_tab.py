import logging
import ctypes
from PySide6.QtWidgets import QWidget, QDialog
from PySide6.QtCore import Slot, QTimer
from src.audio import RecorderThread
from src.closing_while_recording_dialog_widget import ClosingDialog


class MainTab(QWidget):
    def __init__(self, ui, main_self):
        super().__init__()
        logging.info("MainTab starting initialization")
        self.ui = ui

        self.main_self = main_self
        self.sample_rate = 16000
        self.interval = 3
        self.init_()

    def init_(self):
        self.ui.buttonStart.clicked.connect(self.start_recording)
        self.ui.buttonStop.clicked.connect(self.stop_recording)
        self.ui.buttonStop.setEnabled(False)

        self.recorder_thread = RecorderThread(self.sample_rate, self.interval)

        self.recorder_thread.data_is_saving.connect(self.data_started_saving)
        self.recorder_thread.data_saved.connect(self.data_saved)

        logging.info("MainTab initialized")
    
    @Slot()
    def data_started_saving(self):
        self.main_self.can_close = False
        logging.info("can_close set to False")
    
    @Slot()
    def data_saved(self):
        self.main_self.can_close = True
        logging.info("can_close set to True")

    @Slot()
    def start_recording(self):
        self.ui.buttonStart.setEnabled(False)
        self.ui.buttonStop.setEnabled(True)
        self.recorder_thread.start_recording()
        logging.info("Recording started")

    @Slot()
    def stop_recording(self, need_to_save=False):
        need_to_save = not need_to_save  # костыль
        self.ui.buttonStart.setEnabled(True)
        self.ui.buttonStop.setEnabled(False)
        self.recorder_thread.stop_recording(need_to_save)
        logging.info("Recording stopped")