import logging
import os
import ctypes
from PySide6.QtWidgets import QMainWindow, QDialog
from PySide6.QtCore import QTimer
from .main_tab import MainTab
from .audio_files_tab import AudioTab
from .closing_while_recording_dialog_widget import ClosingDialog
from .ui import Ui_MainWindow
from .config import AUDIO_PATH

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.check_paths()

        self.can_close = True

        self.main_tab = MainTab(self.ui, self)
        self.file_tree_tab = AudioTab(self.ui, self)
    
    def check_paths(self):
        logging.info("Checking paths")
        self.check_audio_path()
    
    def check_audio_path(self):
        logging.info("Checking audio path")
        if not os.path.exists(AUDIO_PATH):
            logging.info("Audio path does not exist")
            logging.info("Creating audio path")
            os.mkdir(AUDIO_PATH)
            if os.path.exists(AUDIO_PATH):
                logging.info("Audio path created")
                return
            logging.error("Failed to create audio path")
            logging.error("Exiting the program")
            assert False, "Failed to create audio path"
        logging.info("Audio path exists")
    
    def closeEvent(self, event):
        logging.info("Trying to close the main window")
        if self.main_tab.recorder_thread.recording:
            logging.info("Recording is in progress, opening dialog")
            dialog = ClosingDialog(self.main_tab)
            result = dialog.exec()

            if result == QDialog.Accepted:
                choice = dialog.get_result()
                if choice == dialog.option1:
                    logging.info("User chose save and close")
                    self.main_tab.stop_recording()
                    self.main_tab.data_started_saving()
                elif choice == dialog.option2:
                    logging.info("User chose not save and close")
                    self.main_tab.stop_recording(need_to_save = True)
                    self.main_tab.data_started_saving()
            else:
                logging.info("User chose to continue recording")
                event.ignore()
                return
        if not self.can_close:
            logging.info("can_close is False, starting timer")
            self.timer = QTimer(self)
            self.timer.timeout.connect(self.check_can_close)
            self.timer.start(100)  # Проверяем каждые 100 мс
            event.ignore()
        else:
            logging.info("all good, closing the window")
            self.finish_closing(event)

    def check_can_close(self):
        if self.can_close:
            self.timer.stop()
            self.close()
            logging.info("can_close is True, closing the window")

    def finish_closing(self, event):
        ctypes.windll.ole32.CoUninitialize()
        logging.info("COM completed.")
        if event:
            event.accept()