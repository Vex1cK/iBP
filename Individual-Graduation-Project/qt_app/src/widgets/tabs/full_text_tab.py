import logging
logger = logging.getLogger(__name__)

from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtCore import QThreadPool, QTimer

from src.widgets.trees.full_text_tree_widget import TreeWidgetFullTextFiles
from src.server.ml_api_client import MLClient
from src.config.config import SERVER_URL, SUM_TEXT_PATH
from src.widgets.tabs.custom_tab import CustomTab

class FullTextTab(CustomTab):
    def __init__(self, ui, main_self):
        super().__init__()

        logger.debug("FullTextTab starting initialization")

        self.ui = ui
        self.main_self = main_self

        custom_tree = TreeWidgetFullTextFiles(self, self.ui.treeContainer_2)
        layout = QVBoxLayout(self.ui.treeContainer_2)
        layout.addWidget(custom_tree)
        self.ui.treeContainer_2.setLayout(layout)

        self.ui.buttonRefreshFullText.clicked.connect(custom_tree.refresh_tree)
        self.custom_tree = custom_tree

        self.ui.buttonSumText.clicked.connect(self.sum_text_by_button)

        self.treadpool = QThreadPool()
        self.active_threads = self.treadpool.activeThreadCount()

        self.timer_label = QTimer(self)
        self.timer_label.timeout.connect(self.updates)
        self.timer_label.start(20000)

        logger.debug("FullTextTab initialized")

    def updates(self):
        self.update_active_threads()
        self.update_labels()
    
    def update_labels(self):
        if self.active_threads == 0:
            if self.ui.labelInfoFullTextTab.text() == "<font color='red'>Ведётся обработка ваших файлов</font>":
                self.ui.labelInfoFullTextTab.setText("")
                self.ui.labelInfoFullTextTab.repaint()
        else:
            self.ui.labelInfoFullTextTab.setText("<font color='red'>Ведётся обработка ваших файлов</font>")
            self.ui.labelInfoFullTextTab.repaint()
    
    def summarize_text(self, item, output_path=None, output_extension=".txt"):
        self.ui.labelInfoFullTextTab.setText("<font color='orange'>Проверяем доступ к серверу</font>")
        self.ui.labelInfoFullTextTab.repaint()
        status = self.check_server(self.ui.labelInfoFullTextTab)
        if not status:
            logger.info("Нет доступа к серверу невозможно выполнить преобразование")
            return
        file_path, output_path = self.get_paths_for_ml_api(item, SUM_TEXT_PATH, 
                                                           output_path=output_path, output_extension=output_extension)
        
        logger.debug(f"Starting evaluating sum text, {file_path=}, {output_path=}")

        client = MLClient(SERVER_URL + "/ml/sum_text", file_path, output_path, self.callback1)
        self.treadpool.start(client)
        self.updates()
    
    def sum_text_by_button(self):
        item = self.chose_file(self.custom_tree, "Текстовые файлы (*.txt)")
        if item:
            self.summarize_text(item)