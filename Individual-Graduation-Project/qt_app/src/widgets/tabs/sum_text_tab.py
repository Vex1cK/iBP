import logging
logger = logging.getLogger(__name__)

from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtCore import QThreadPool

from src.widgets.trees.sum_text_tree_widget import TreeWidgetSumTextFiles
from src.widgets.tabs.custom_tab import CustomTab

class SumTextTab(CustomTab):
    def __init__(self, ui, main_self):
        super().__init__()

        logger.debug("SumTextTab starting initialization")

        self.ui = ui
        self.main_self = main_self

        custom_tree = TreeWidgetSumTextFiles(self, self.ui.treeContainer_3)
        layout = QVBoxLayout(self.ui.treeContainer_3)
        layout.addWidget(custom_tree)
        self.ui.treeContainer_3.setLayout(layout)

        self.ui.buttonRefreshSumText.clicked.connect(custom_tree.refresh_tree)
        self.custom_tree = custom_tree

        self.treadpool = QThreadPool()
        self.active_threads = self.treadpool.activeThreadCount()

        logger.debug("SumTextTab initialized")