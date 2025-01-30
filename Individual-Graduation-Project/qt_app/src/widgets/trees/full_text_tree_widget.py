import logging
logger = logging.getLogger(__name__)

from PySide6.QtWidgets import QMenu

from src.config.config import FULL_TEXT_PATH
from src.widgets.trees.custom_tree_widget import CustomTreeWidget


class TreeWidgetFullTextFiles(CustomTreeWidget):
    def __init__(self, parent_tab, parent=None):
        super().__init__(parent)
        self.name = 'FullText'
        logger.debug(f"Starting initializating {self.name}Tree")

        self.root_path = FULL_TEXT_PATH
        self.init_(parent_tab)

    def contextMenuEvent(self, event):
        logger.debug("Context menu opening")
        item = self.itemAt(event.pos())
        if item:
            menu = QMenu(self)
            sum_text_action = menu.addAction("Суммировать текст")
            rename_action = menu.addAction("Переименовать")
            delete_action = menu.addAction("Удалить")
            
            action = menu.exec_(self.mapToGlobal(event.pos()))

            if action == rename_action:
                self.edit_item(item, 0)
            elif action == delete_action:
                self.delete_item(item)
            elif action == sum_text_action:
                self.parent_tab.summarize_text(item)
        else:
            menu = QMenu(self)
            refresh_action = menu.addAction("Обновить список")

            action = menu.exec_(self.mapToGlobal(event.pos()))

            if action == refresh_action:
                self.refresh_tree()