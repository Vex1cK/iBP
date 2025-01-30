import logging
logger = logging.getLogger(__name__)

from PySide6.QtWidgets import QTreeWidget, QTreeWidgetItem, QMessageBox
from PySide6.QtCore import Qt, Slot
from datetime import datetime
import os

class CustomTreeWidget(QTreeWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.name = 'None'
        # logger.debug(f"Starting initializating {self.name}Tree")

        self.root_path = None
        # self.init_(parent_tab)
    
    def init_(self, parent_tab, need_init_2=True):
        self.parent_tab = parent_tab

        self.columns_count = 4
        self.file_name_index          = 0  # noqa: E221
        self.file_extension_index     = 1  # noqa: E221
        self.file_creation_date_index = 2  # noqa: E221
        self.file_size_index          = 3  # noqa: E221

        if need_init_2:
            self.init_2()
    
    def init_2(self):
        self.setColumnCount(self.columns_count)  # Устанавливаем количество столбцов
        self.setHeaderLabels(["Название файла", "Расширение", "Дата создания", "Размер файла"])  # Устанавливаем заголовки столбцов # noqa: E501

        self.setEditTriggers(QTreeWidget.NoEditTriggers)
        self.itemDoubleClicked.connect(self.on_item_double_clicked)
        self.itemChanged.connect(self.rename_file)

        logger.debug(f"{self.name}Tree initialized, starting populating tree")
        self.populate_tree()
        logger.debug(f"{self.name}Tree tree populated")

    @staticmethod
    def format_file_size(size_in_bytes):
        # Единицы измерения
        units = ["байт", "КБ", "МБ", "ГБ", "ТБ", "ПБ", "ЭБ", "ЗБ", "ЙБ"]
        # Начальный индекс для единицы измерения
        index = 0
        
        # Последовательно делим размер на 1024, пока не найдём подходящую единицу
        while size_in_bytes >= 1024 and index < len(units) - 1:
            size_in_bytes /= 1024.0
            index += 1
        
        # Возвращаем строку с округлённым значением и единицей измерения
        return f"{size_in_bytes:.2f} {units[index]}"

    def populate_tree(self):
        self.itemChanged.disconnect()
        for item in os.listdir(self.root_path):
            item_path = os.path.join(self.root_path, item)
            if os.path.isfile(item_path):
                # Получаем дату создания файла
                item_name = item[:item.find(".")]
                creation_time = os.path.getctime(item_path)
                creation_date = datetime.fromtimestamp(creation_time).strftime("%Y-%m-%d %H:%M:%S")

                # Получаем расширение файла
                file_extension = os.path.splitext(item)[1]

                # Получаем размер файла
                file_size = self.format_file_size(os.path.getsize(item_path))

                # Создаем элемент дерева
                strings = [0] * self.columns_count
                strings[self.file_name_index] = item_name
                strings[self.file_extension_index] = file_extension
                strings[self.file_creation_date_index] = creation_date
                strings[self.file_size_index] = file_size

                tree_item = QTreeWidgetItem(self, strings)
                
                # Разрешаем редактирование только первого столбца
                tree_item.setFlags(tree_item.flags() | Qt.ItemIsEditable)
                
                # Сохраняем исходное название файла в качестве данных
                tree_item.setData(self.file_name_index, Qt.UserRole, item_name)
                tree_item.setData(self.file_extension_index, Qt.UserRole, file_extension)
                tree_item.setData(self.file_creation_date_index, Qt.UserRole, creation_date)
                tree_item.setData(self.file_size_index, Qt.UserRole, file_size)
        
        for i in range(self.columns_count):
            self.resizeColumnToContents(i)

        self.itemChanged.connect(self.rename_file)
    
    @Slot()
    def refresh_tree(self):
        logger.debug("Refreshing tree")
        self.clear()
        self.populate_tree()

    def edit_item(self, item, column):
        self.editItem(item, column)

    def contextMenuEvent(self, event):
        raise NotImplementedError("Method contextMenuEvent must be implemented in child class")
        # logger.debug("Context menu opening")
        # item = self.itemAt(event.pos())
        # if item:
        #     menu = QMenu(self)
        #     to_text_action = menu.addAction("Преобразовать в текст")
        #     rename_action = menu.addAction("Переименовать")
        #     delete_action = menu.addAction("Удалить")
            
        #     action = menu.exec_(self.mapToGlobal(event.pos()))

        #     if action == rename_action:
        #         self.edit_item(item, 0)
        #     elif action == delete_action:
        #         self.delete_item(item)
        #     elif action == to_text_action:
        #         self.parent_tab.convert_audio_to_text(item)
        # else:
        #     menu = QMenu(self)
        #     refresh_action = menu.addAction("Обновить список")

        #     action = menu.exec_(self.mapToGlobal(event.pos()))

        #     if action == refresh_action:
        #         self.refresh_tree()
    
    def rename_file(self, item: QTreeWidgetItem, column):
        logger.debug("Renaming file")
        self.itemChanged.disconnect()
        old_name = item.data(column, Qt.UserRole)
        new_name = item.text(column)
        if old_name != new_name:
            file_extension = item.data(self.file_extension_index, Qt.UserRole)
            old_path = os.path.join(self.root_path, old_name + file_extension)
            new_path = os.path.join(self.root_path, new_name + file_extension)
            try:
                os.rename(old_path, new_path)
                item.setData(column, Qt.UserRole, new_name)
                self.resizeColumnToContents(0)
                logger.debug("File renamed")
            except Exception as e:
                logger.error(f"Failed to rename file: {e}")
                QMessageBox.critical(self, "Error", f"Failed to rename file: {e}")
                item.setText(column, old_name)
        self.itemChanged.connect(self.rename_file)
    
    def delete_item(self, item):
        logger.debug("Deleting file")
        file_name = item.text(0)
        file_extension = item.data(self.file_extension_index, Qt.UserRole)
        file_path = os.path.join(self.root_path, file_name + file_extension)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
            elif os.path.isdir(file_path):
                os.rmdir(file_path)
            self.takeTopLevelItem(self.indexOfTopLevelItem(item))
            self.resizeColumnToContents(0)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to delete file: {e}")
    
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_F2:
            logger.debug("F2 pressed")
            current_item = self.currentItem()
            if current_item:
                self.editItem(current_item, 0)
        else:
            super().keyPressEvent(event)
        
    def on_item_double_clicked(self, item, column):
        logger.debug("Item double clicked")
        file_name = item.text(column)
        file_extension = item.data(self.file_extension_index, Qt.UserRole)
        file_path = os.path.join(self.root_path, file_name + file_extension)
        
        if os.path.isfile(file_path):
            try:
                self.parent_tab.open_file(file_path)
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to open file: {e}")
        else:
            QMessageBox.information(self, "Info", "Selected item is not a file.")

    