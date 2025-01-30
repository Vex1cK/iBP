import logging
logger = logging.getLogger(__name__)

import os
from PySide6.QtWidgets import QDialog, QFileDialog, QTreeWidgetItem
from PySide6.QtCore import Qt
from datetime import datetime

from src.ui_module.chose_file_dialog_py_ui import Ui_Dialog

class ChoseFileDialog(QDialog):
    def __init__(self, which):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.setWindowTitle("Выбор файла")

        self.selected_file = None
        self.which = which

        self.ui.pushButtonChoseFile.clicked.connect(self.select_file)
        self.ui.pushButtonOk.clicked.connect(self.accept)
        self.ui.pushButtonCancel.clicked.connect(self.reject)
    
    def select_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Выберите файл", "", self.which)
        if file_path:
            self.selected_file = file_path
            self.ui.lineEdit.setText(file_path)

    def get_selected_file(self):
        return self.selected_file
    
    def get_selected_file_as_item(self, some_tree):
        item = os.path.basename(self.selected_file)
        item_path = self.selected_file

        item_name = item[:item.find(".")]
        creation_time = os.path.getctime(item_path)
        creation_date = datetime.fromtimestamp(creation_time).strftime("%Y-%m-%d %H:%M:%S")

        # Получаем расширение файла
        file_extension = os.path.splitext(item)[1]

        # Получаем размер файла
        file_size = some_tree.format_file_size(os.path.getsize(item_path))

        # Создаем элемент дерева
        strings = [0] * some_tree.columns_count
        strings[some_tree.file_name_index] = item_name
        strings[some_tree.file_extension_index] = file_extension
        strings[some_tree.file_creation_date_index] = creation_date
        strings[some_tree.file_size_index] = file_size

        tree_item = QTreeWidgetItem(strings)
        
        # Разрешаем редактирование только первого столбца
        tree_item.setFlags(tree_item.flags() | Qt.ItemIsEditable)
        
        # Сохраняем исходное название файла в качестве данных
        tree_item.setData(some_tree.file_name_index, Qt.UserRole, item_name)
        tree_item.setData(some_tree.file_extension_index, Qt.UserRole, file_extension)
        tree_item.setData(some_tree.file_creation_date_index, Qt.UserRole, creation_date)
        tree_item.setData(some_tree.file_size_index, Qt.UserRole, file_size)
    
        return tree_item
        
    