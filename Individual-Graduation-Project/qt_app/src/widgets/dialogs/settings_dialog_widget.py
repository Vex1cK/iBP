import logging
logger = logging.getLogger(__name__)

from PySide6.QtWidgets import QDialog

from src.ui_module.settings_dialog_py_ui import Ui_Dialog
from src.widgets.dialogs.change_ip_dialog_widget import ChangeIPDialog
from src.widgets.dialogs.change_paths_dialog_widget import ChangePathDialog


class SettingsDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.setWindowTitle("Смена IP сервера")

        self.ui.pushButtonPaths.clicked.connect(self.change_paths)
        self.ui.pushButtonIP.clicked.connect(self.change_ip)
    
    def change_ip(self):
        dialog = ChangeIPDialog()
        dialog.exec()

    def change_paths(self):
        dialog = ChangePathDialog()
        dialog.exec()