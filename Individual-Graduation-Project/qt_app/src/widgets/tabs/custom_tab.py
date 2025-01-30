import logging
logger = logging.getLogger(__name__)

from PySide6.QtWidgets import QWidget, QDialog
from PySide6.QtCore import Qt
import platform
import os

from src.config.config import FULL_TEXT_PATH, SUM_TEXT_PATH
from src.server.auth_ping_api_client import ping
from src.widgets.dialogs.chose_file_dialog_widget import ChoseFileDialog

class CustomTab(QWidget):
    def update_active_threads(self):
        self.active_threads = self.treadpool.activeThreadCount()
    
    def check_server(self, label):
        status, _ = ping()
        if status:
            return True
        else:
            label.setText("""<font color='red'>Нет доступа к серверу,<br>
                          невозможно выполнить<br>преобразование</font>""")
            label.repaint()
            return False
    
    def open_file(self, file_path):
        logger.debug("Opening file")
        system = platform.system()
        if system == "Windows":
            os.startfile(file_path)  # Windows
        else:
            import subprocess
            if system == "Linux":
                subprocess.call(['xdg-open', file_path])  # Linux
            elif system == "Darwin":
                subprocess.call(['open', file_path])  # macOS
            else:
                raise OSError(f"Unsupported operating system: {system}")
    
    def get_paths_for_ml_api(self, item, output_folder_path, output_path=None, output_extension=".txt", both=False):
        file_name = item.text(0)
        file_extension = item.data(self.custom_tree.file_extension_index, Qt.UserRole)
        # file_data_created = item.data(self.custom_tree.file_creation_date_index, Qt.UserRole)
        # print(f"{file_name=}\n{file_extension=}\n{file_data_created=}")
        file_path = os.path.join(self.custom_tree.root_path, file_name + file_extension)
        if not output_path:
            if both:
                output_path = os.path.join(FULL_TEXT_PATH, "Text from " + file_name + output_extension)
                output_path_sum = os.path.join(SUM_TEXT_PATH, "Sum Text from " + file_name + output_extension)

                return (file_path, output_path, output_path_sum)
            else:
                if output_folder_path == FULL_TEXT_PATH:
                    output_path = os.path.join(output_folder_path, "Text from " + file_name + output_extension)
                else:
                    output_path = os.path.join(output_folder_path, "Sum Text from " + file_name + output_extension)
                return (file_path, output_path)
    
    def callback1(self, status, msg, *args, **kwargs):
        if status:
            logger.info("Преобразованно!")
        else:
            logger.error(f"Ошибка: {msg}")
        
    def chose_file(self, some_tree, which):
        dialog = ChoseFileDialog(which)
        if dialog.exec() == QDialog.Accepted:
            file_path = dialog.get_selected_file()
            if file_path:
                file_item = dialog.get_selected_file_as_item(some_tree)
                return file_item