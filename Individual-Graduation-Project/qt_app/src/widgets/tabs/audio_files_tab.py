import logging
logger = logging.getLogger(__name__)

from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtCore import QThreadPool, QTimer

from src.widgets.trees.audio_tree_widget import TreeWidgetAudioFiles
from src.server.ml_api_client import MLClient
from src.config.config import SERVER_URL, FULL_TEXT_PATH
from src.widgets.tabs.custom_tab import CustomTab

class AudioTab(CustomTab):
    def __init__(self, ui, main_self):
        super().__init__()

        logger.debug("AudioTab starting initialization")

        self.ui = ui
        self.main_self = main_self

        custom_tree = TreeWidgetAudioFiles(self, self.ui.treeContainer)
        layout = QVBoxLayout(self.ui.treeContainer)
        layout.addWidget(custom_tree)
        self.ui.treeContainer.setLayout(layout)

        self.ui.buttonRefresh.clicked.connect(custom_tree.refresh_tree)
        self.custom_tree = custom_tree

        self.ui.buttonAudio2Text.clicked.connect(self.a2t_by_button)
        self.ui.buttonAudio2TextAndSum.clicked.connect(self.a2t_and_sum_by_button)

        self.treadpool = QThreadPool()
        self.active_threads = self.treadpool.activeThreadCount()

        self.timer_label = QTimer(self)
        self.timer_label.timeout.connect(self.updates)
        self.timer_label.start(20000)

        logger.debug("AudioTab initialized")

    def updates(self):
        self.update_active_threads()
        self.update_labels()

    def update_labels(self):
        if self.active_threads == 0:
            if self.ui.labelInfoAudioTab.text() == "<font color='red'>Ведётся обработка ваших файлов</font>":
                self.ui.labelInfoAudioTab.setText("")
                self.ui.labelInfoAudioTab.repaint()
        else:
            self.ui.labelInfoAudioTab.setText("<font color='red'>Ведётся обработка ваших файлов</font>")
            self.ui.labelInfoAudioTab.repaint()

    def convert_audio_to_text(self, item, output_path=None, output_extension=".txt"):
        self.ui.labelInfoAudioTab.setText('<font color="#FFA500">Проверяем доступ к серверу</font>')
        self.ui.labelInfoAudioTab.repaint()
        status = self.check_server(self.ui.labelInfoAudioTab)
        if not status:
            logger.info("Нет доступа к серверу невозможно выполнить преобразование")
            return
        file_path, output_path = self.get_paths_for_ml_api(item, FULL_TEXT_PATH, 
                                                           output_path=output_path, output_extension=output_extension)
        
        logger.debug(f"Starting evaluating audio2text, {file_path=}, {output_path=}")

        client = MLClient(SERVER_URL + "/ml/transcribe_audio", file_path, output_path, self.callback1)
        self.treadpool.start(client)
        self.updates()
    
    def convert_audio_to_text_and_sum(self, item, output_path=None, output_extension=".txt"):
        self.ui.labelInfoAudioTab.setText("<font color='orange'>Проверяем доступ к серверу</font>")
        self.ui.labelInfoAudioTab.repaint()
        status = self.check_server(self.ui.labelInfoAudioTab)
        if not status:
            logger.info("Нет доступа к серверу невозможно выполнить преобразование")
            return
        file_path, output_path, output_path_sum = self.get_paths_for_ml_api(item, FULL_TEXT_PATH, 
                                                                            output_path=output_path, 
                                                                            output_extension=output_extension, 
                                                                            both=True)
        
        logger.debug(f"Starting evaluating audio2text_and_sum, {file_path=}, {output_path=}")

        client = MLClient(SERVER_URL + "/ml/transcribe_audio", file_path, output_path, 
                          self.sum_text_after_a2t, json_to_give=("summary", output_path, output_path_sum))
        self.treadpool.start(client)
        self.updates()
    
    def sum_text_after_a2t(self, status, msg, json):
        if status:
            logger.info("Запускаем суммирование")
            if json[0] == 'summary':
                file_path = json[1]
                output_path_sum = json[2]
            else:
                logger.error(f"Ошибка: {json}\nПервый элемент должен быть 'summary'")
                return
            try:
                client = MLClient(SERVER_URL + "/ml/sum_text", file_path, output_path_sum, self.callback1)
                self.treadpool.start(client)
            except RuntimeError as e:
                logger.error(e.__str__())
        else:
            logger.error(f"Ошибка: {msg}")
    
    def a2t_by_button(self):
        item = self.chose_file(self.custom_tree, "Аудио файлы (*.wav)")
        if item:
            self.convert_audio_to_text(item)
    
    def a2t_and_sum_by_button(self):
        item = self.chose_file(self.custom_tree, "Аудио файлы (*.wav)")
        if item:
            self.convert_audio_to_text_and_sum(item)