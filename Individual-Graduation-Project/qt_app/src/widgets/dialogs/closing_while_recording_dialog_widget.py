import logging
logger = logging.getLogger(__name__)

from PySide6.QtWidgets import QDialog, QPushButton, QVBoxLayout, QLabel

class ClosingDialogWhileRecording(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Закрытие окна")
        self.setModal(True)

        layout = QVBoxLayout()

        # Заголовок
        self.label = QLabel("Запись всё еще ведётся.\nВы уверены что хотите закрыть окно?:")
        layout.addWidget(self.label)

        # Кастомные кнопки
        self.option1 = "Сохранить и закрыть"
        self.option2 = "Не сохранять и закрыть"
        self.option3 = "Продолжить запись"

        self.button1 = QPushButton(self.option1)
        self.button2 = QPushButton(self.option2)
        self.button3 = QPushButton(self.option3)

        # Подключение сигналов
        self.button1.clicked.connect(self.on_button1_clicked)
        self.button2.clicked.connect(self.on_button2_clicked)
        self.button3.clicked.connect(self.on_button3_clicked)

        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)

        self.setLayout(layout)

        self.result = None
    
    def on_button1_clicked(self):
        self.result = self.option1
        self.accept()

    def on_button2_clicked(self):
        self.result = self.option2
        self.accept()

    def on_button3_clicked(self):
        self.result = self.option3
        self.reject()
    
    def get_result(self):
        return self.result