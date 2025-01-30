import logging
logger = logging.getLogger(__name__)

import os
from PySide6.QtWidgets import QDialog, QFileDialog

from src.ui_module.change_paths_dialog_py_ui import Ui_Dialog
from src.config.config import AUDIO_PATH, FOLDER_PATH, SUM_TEXT_PATH, FULL_TEXT_PATH
from src.utils.other_utils import update_all_paths

class ChangePathDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.setWindowTitle("Смена путей к файлам")

        self.ui.lineEditAudioPath.setText(AUDIO_PATH)
        self.ui.lineEditFullTextPath.setText(FULL_TEXT_PATH)
        self.ui.lineEditSumTextPath.setText(SUM_TEXT_PATH)
        self.ui.lineEditFolderPath.setText(FOLDER_PATH)

        self.ui.pushButtonAudioPath.clicked.connect(self.change_audio_path)
        self.ui.pushButtonFullTextPath.clicked.connect(self.change_full_text_path)
        self.ui.pushButtonSumTextPath.clicked.connect(self.change_sum_text_path)
        self.ui.pushButtonFolderPath.clicked.connect(self.change_folder_path)

        self.ui.pushButtonCancel.clicked.connect(self.reject)
        self.ui.pushButtonOk.clicked.connect(self.reject)
        self.ui.pushButtonSave.clicked.connect(self.save)
        self.ui.pushButtonOk.setHidden(True)
    
    def change_audio_path(self):
        new_directory = self.select_directory()
        if new_directory:
            self.ui.lineEditAudioPath.setText(new_directory)
     
    def change_full_text_path(self):
        new_directory = self.select_directory()
        if new_directory:
            self.ui.lineEditFullTextPath.setText(new_directory)
     
    def change_sum_text_path(self):
        new_directory = self.select_directory()
        if new_directory:
            self.ui.lineEditSumTextPath.setText(new_directory)
     
    def change_folder_path(self):
        new_directory = self.select_directory()
        if new_directory:
            self.ui.lineEditFolderPath.setText(new_directory)

    def select_directory(self):
        directory = QFileDialog.getExistingDirectory(self, "Выберите директорию")
        if directory:
            return directory
        else:
            return False
    
    def save(self):
        new_paths = [self.ui.lineEditAudioPath.text(), self.ui.lineEditFullTextPath.text(),
                     self.ui.lineEditSumTextPath.text(), self.ui.lineEditFolderPath.text()]
        if new_paths != [AUDIO_PATH, FULL_TEXT_PATH, SUM_TEXT_PATH, FOLDER_PATH]:
            update_all_paths(list(map(lambda x: os.path.normpath(x), new_paths)))
            self.ui.pushButtonOk.setHidden(False)
            self.ui.labelInfo.setText("<font color='green'>Сохранено. Перезапустите приложение.</font>")
