import logging
logger = logging.getLogger(__name__)

from PySide6.QtWidgets import QMenu

from src.config.config import AUDIO_PATH
from src.widgets.trees.custom_tree_widget import CustomTreeWidget


class TreeWidgetAudioFiles(CustomTreeWidget):
    def __init__(self, parent_tab, parent=None):
        super().__init__(parent)
        self.name = 'Audio'
        logger.debug(f"Starting initializating {self.name}Tree")

        self.root_path = AUDIO_PATH
        self.init_(parent_tab)

    def contextMenuEvent(self, event):
        logger.debug("Context menu opening")
        item = self.itemAt(event.pos())
        if item:
            menu = QMenu(self)
            to_text_action = menu.addAction("Преобразовать в текст")
            to_text_and_sum_action = menu.addAction("Преобразовать в текст и суммаризировать")
            rename_action = menu.addAction("Переименовать")
            delete_action = menu.addAction("Удалить")
            
            action = menu.exec_(self.mapToGlobal(event.pos()))

            if action == rename_action:
                self.edit_item(item, 0)
            elif action == delete_action:
                self.delete_item(item)
            elif action == to_text_action:
                self.parent_tab.convert_audio_to_text(item)
            elif action == to_text_and_sum_action:
                self.parent_tab.convert_audio_to_text_and_sum(item)
        else:
            menu = QMenu(self)
            refresh_action = menu.addAction("Обновить список")

            action = menu.exec_(self.mapToGlobal(event.pos()))

            if action == refresh_action:
                self.refresh_tree()