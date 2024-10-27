from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtCore import Qt, Slot
from src.custom_tree_widget import TreeWidgetAudioFiles
import logging
import platform
import os
from datetime import datetime

class AudioTab(QWidget):
    def __init__(self, ui, main_self):
        super().__init__()

        logging.info("AudioTab starting initialization")

        self.ui = ui
        self.main_self = main_self

        tree_container = self.ui.treeContainer
        custom_tree = TreeWidgetAudioFiles(self)
        layout = QVBoxLayout(tree_container)
        layout.addWidget(custom_tree)
        tree_container.setLayout(layout)

        self.ui.buttonRefresh.clicked.connect(custom_tree.refresh_tree)
        self.custom_tree = custom_tree


        logging.info("AudioTab initialized")
    
    def open_file(self, file_path):
        logging.info("Opening file")
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
    
    def convert_audio_to_text(self, item, output_path = None, output_extension = ".txt"):
        file_name = item.text(0)
        file_extension = item.data(self.custom_tree.file_extension_index, Qt.UserRole)
        file_data_created = item.data(self.custom_tree.file_creation_date_index, Qt.UserRole)
        print(f"{file_name=}\n{file_extension=}\n{file_data_created=}")
        file_path = os.path.join(self.custom_tree.audio_root, file_name + file_extension)
        if not output_path:
            now = datetime.now().__str__().split('.')[0].replace(':', '-')
            output_path = os.path.join(self.custom_tree.audio_root, "Text from " + file_name + output_extension)
        
        logging.info(f"Starting evaluating audio2text, {file_path=}, {output_path=}")

        # Преобразование