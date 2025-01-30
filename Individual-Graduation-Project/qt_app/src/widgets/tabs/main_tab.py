import logging
logger = logging.getLogger(__name__)

from PySide6.QtWidgets import QWidget, QMessageBox
from PySide6.QtCore import Slot, QTimer
import os

from src.utils.audio import RecorderThread
from src.server.auth_ping_api_client import ping
from src.config.config import AUDIO_PATH
from src.utils.other_utils import logout_util
from src.widgets.dialogs.settings_dialog_widget import SettingsDialog


class MainTab(QWidget):
    def __init__(self, ui, main_self):
        super().__init__()
        logger.debug("MainTab starting initialization")
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

        self.labelCountAudio_default_text = self.ui.labelCountAudio.text()
        self.labelCountFolders_default_text = self.ui.labelCountFolders.text()
        self.labelServerStatus_default_text = self.ui.labelServerStatus.text()
        self.labelPing_default_text = self.ui.labelPing.text()

        self.update_file_labels()
        self.update_ping_labels()

        self.ping_timer = QTimer(self)
        self.ping_timer.timeout.connect(self.update_ping_labels)
        self.ping_timer.start(60000)

        self.file_labels_update_timer = QTimer(self)
        self.file_labels_update_timer.timeout.connect(self.update_file_labels)
        self.file_labels_update_timer.start(60000)

        self.ui.buttonLogOut.clicked.connect(self.logout_dialog)

        self.ui.buttonSettings.clicked.connect(self.open_settings)

        logger.debug("MainTab initialized")

    def update_file_labels(self):
        audio_cnt_text = self.labelCountAudio_default_text.replace("%%", f"{len(os.listdir(AUDIO_PATH))}")
        self.ui.labelCountAudio.setText(audio_cnt_text)

        # folders_cnt_text = self.labelCountFolders_default_text.replace("%%", f"{len(os.listdir(FOLDER_PATH))}")
        folders_cnt_text = self.labelCountFolders_default_text.replace("%%", "0")
        self.ui.labelCountFolders.setText(folders_cnt_text)
    
    def update_ping_labels(self):
        ping_ok, ping_msg = ping()
        if ping_ok:
            ping_value = round(float(ping_msg), 0)
        else:
            ping_value = 0

        server_color_text = ("green", "Есть") if ping_ok else ("red", "Нет")

        server_text = self.labelServerStatus_default_text.replace(
            "%%", f"<font color='{server_color_text[0]}'>{server_color_text[1]}</font>")
        self.ui.labelServerStatus.setText(server_text)

        color_ping = "green" if ping_value < 500 else "red" if ping_value > 3000 else "orange"
        ping_text = self.labelPing_default_text.replace("%%", f"<font color='{color_ping}'>{ping_value}</font>")
        self.ui.labelPing.setText(ping_text)

        # logger.info(f"ping: {ping_value} ms | updated successfully")
    
    def open_settings(self):
        dialog = SettingsDialog()
        dialog.exec()
        
    @Slot()
    def data_started_saving(self):
        self.main_self.can_close = False
        logger.debug("can_close set to False")
    
    @Slot()
    def data_saved(self):
        self.main_self.can_close = True
        logger.debug("can_close set to True")

    @Slot()
    def start_recording(self):
        self.ui.buttonStart.setEnabled(False)
        self.ui.buttonStop.setEnabled(True)
        self.recorder_thread.start_recording()
        logger.debug("Recording started")

    @Slot()
    def stop_recording(self, need_to_save=False):
        need_to_save = not need_to_save  # костыль
        self.ui.buttonStart.setEnabled(True)
        self.ui.buttonStop.setEnabled(False)
        self.recorder_thread.stop_recording(need_to_save)
        logger.debug("Recording stopped")
    
    def logout_dialog(self):
        reply = QMessageBox.question(
            self,
            "Вопрос",
            "Вы уверены что хотите выйти из аккаунта?",
            QMessageBox.Yes | QMessageBox.No
        )
        
        if reply == QMessageBox.Yes:
            logger.info("Выходим из аккаунта")
            logout_util()
            self.main_self.stack_widget.setCurrentIndex(1)
        else:
            pass