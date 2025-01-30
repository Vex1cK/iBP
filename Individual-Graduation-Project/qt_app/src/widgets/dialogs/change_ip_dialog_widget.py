import logging
logger = logging.getLogger(__name__)

from PySide6.QtWidgets import QDialog

from src.ui_module.new_ip_dialog_py_ui import Ui_Dialog
from src.utils.other_utils import is_valid_ipv4, change_server_IP

class ChangeIPDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.setWindowTitle("Смена IP сервера")

        self.ui.pushButton.clicked.connect(self.click)
    
    def click(self):
        new_ip = self.ui.lineEdit.text()
        
        if is_valid_ipv4(new_ip):
            change_server_IP(new_ip)
            self.accept()
        else:
            self.ui.labelInfo.setText("<font color='red'>Некорректный формат IPv4!</font>")