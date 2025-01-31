import logging
logger = logging.getLogger(__name__)

import ctypes
from PySide6.QtWidgets import QWidget, QDialog, QMainWindow, QStackedWidget, QApplication, QMessageBox
from PySide6.QtCore import QTimer
from PySide6.QtGui import QIcon

from src.widgets.tabs.main_tab import MainTab
from src.widgets.tabs.audio_files_tab import AudioTab
from src.widgets.tabs.full_text_tab import FullTextTab
from src.widgets.tabs.sum_text_tab import SumTextTab
from src.widgets.dialogs.closing_while_recording_dialog_widget import ClosingDialogWhileRecording
from src.widgets.dialogs.closing_while_waiting_for_backend_dialog_widget import ClosingDialogWhileWaitingForBackend
from src.widgets.dialogs.change_ip_dialog_widget import ChangeIPDialog
from src.ui_module.login_widget_py_ui import Ui_LoginWidget
from src.ui_module.register_widget_py_ui import Ui_RegisterWidget
from src.ui_module.main_widget_py_ui import Ui_MainWidget
from src.config.config import get_current_status, PATH_TO_APP_ICON
from src.utils.validation_utils import validate_user, check_password
from src.server.auth_ping_api_client import login_request, register_request
from src.utils.other_utils import update_token_in_json_and_config

class MainApp(QMainWindow):  # Еcли разносить эти классы в разные файлы, то приложение падает с ошибкой QWidget: Must construct a QApplication before a QWidget # noqa: E501
    def __init__(self):
        logger.debug("Start initialization MainApp")
        super().__init__()

        self.setWindowTitle("BriefTalk AI")
        self.setWindowIcon(QIcon(PATH_TO_APP_ICON))

        screen_geometry = QApplication.primaryScreen().availableGeometry()
        screen_width, screen_height = screen_geometry.width(), screen_geometry.height()
        # logger.debug(f"Screen size: {screen_width=}, {screen_height=}")
        # if screen_width < 1920 or screen_height < 1050:
        #     from src.ui_module.main_widget_mini_py_ui import Ui_MainWidget
        #     logger.debug("Using mini version of ui")
        # else:
        #     from src.ui_module.main_widget_py_ui import Ui_MainWidget

        self.main_class_ui = Ui_MainWidget
        self.w, self.h = max(int(screen_width * 0.55), 1030), max(int(screen_height * 0.65), 600)
        self.setFixedSize(self.w, self.h)

        self.init_windows()

    def init_windows(self):
        logger.debug("Создаём окна в MainApp")

        self.stack_widget = QStackedWidget()

        self.main_window = MainWidget(self.main_class_ui, self.stack_widget)
        self.login_window = LoginWidget(self.w, self.h, self.stack_widget)
        self.register_window = RegisterWidget(self.w, self.h, self.stack_widget)

        self.stack_widget.addWidget(self.main_window)
        self.stack_widget.addWidget(self.login_window)
        self.stack_widget.addWidget(self.register_window)

        self.setCentralWidget(self.stack_widget)

        if get_current_status():
            self.stack_widget.setCurrentIndex(0)
        else:
            self.stack_widget.setCurrentIndex(1)

    def closeEvent(self, event):
        logger.debug("Trying to close the main window")
        self.main_window.update_waiting_for_backend_var()

        if self.main_window.main_tab.recorder_thread.recording:
            logger.debug("Recording is in progress, opening dialog")
            dialog = ClosingDialogWhileRecording(self.main_window.main_tab)
            result = dialog.exec()

            if result == QDialog.Accepted:
                choice = dialog.get_result()
                if choice == dialog.option1:
                    logger.debug("User chose save and close")
                    self.main_window.main_tab.stop_recording()
                    self.main_window.main_tab.data_started_saving()
                elif choice == dialog.option2:
                    logger.debug("User chose not save and close")
                    self.main_window.main_tab.stop_recording(need_to_save=False)
                    self.main_window.main_tab.data_started_saving()
            else:
                logger.debug("User chose to continue recording")
                event.ignore()
                return
            
        if self.main_window.waiting_for_backend_response:
            logger.debug("Waiting for backend so cant close, opening dialog")
            dialog = ClosingDialogWhileWaitingForBackend(self.main_window.main_tab)
            result = dialog.exec()

            if result == QDialog.Accepted:
                choice = dialog.get_result()
                if choice == dialog.option1:
                    logger.debug("User chose to close and abort")
                    msg = QMessageBox()
                    msg.setWindowTitle("Сообщение")
                    msg.setText("К сожалению безопасно прервать процессы нельзя. Выключайте компьютер на свой страх и риск =D")  # noqa: E501  # type: ignore
                    msg.setIcon(QMessageBox.Information)
                    msg.setStandardButtons(QMessageBox.Ok)
                    result = msg.exec()
                    event.ignore()
                    return
                elif choice == dialog.option2:
                    logger.debug("User chose to close and continue")
            else:
                logger.debug("User chose to not close window")
                event.ignore()
                return
            
        if not self.main_window.can_close:
            logger.debug("can_close is False, starting timer")
            self.timer = QTimer(self)
            self.timer.timeout.connect(self.check_can_close)
            self.timer.start(100)
            event.ignore()

        else:
            logger.debug("all good, closing the window")
            self.finish_closing(event)

    def check_can_close(self):
        if self.main_window.can_close:
            self.timer.stop()
            self.close()
            logger.debug("can_close is True, closing the window")

    def finish_closing(self, event):
        ctypes.windll.ole32.CoUninitialize()
        logger.debug("COM completed.")
        if event:
            event.accept()

class MainWidget(QWidget):
    def __init__(self, Ui_class, stack):
        logger.debug("Start initialization MainWindow")
        super().__init__()
        self.ui = Ui_class()
        self.ui.setupUi(self)
        self.stack_widget = stack

        self.can_close = True
        self.waiting_for_backend_response = False

        self.main_tab = MainTab(self.ui, self)
        self.audio_tab = AudioTab(self.ui, self)
        self.full_text_tab = FullTextTab(self.ui, self)
        self.sum_text_tab = SumTextTab(self.ui, self)
    
    def update_waiting_for_backend_var(self):
        self.audio_tab.update_active_threads()
        self.full_text_tab.update_active_threads()
        self.sum_text_tab.update_active_threads()

        summ = sum([
            self.audio_tab.active_threads,
            self.full_text_tab.active_threads,
            self.sum_text_tab.active_threads
        ])
        if summ == 0:
            self.waiting_for_backend_response = False
        elif summ > 0:
            self.waiting_for_backend_response = True

class LoginWidget(QWidget):
    def __init__(self, w, h, stack):
        super().__init__()
        self.w = w
        self.h = h
        self.stack_widget = stack

        self.ui = Ui_LoginWidget()
        self.ui.setupUi(self)

        self.ui.pushButtonCreate.clicked.connect(self.switch_to_register)
        self.ui.pushButtonLogin.clicked.connect(self.login)
        # self.ui.lineEditPassword.setEchoMode(QLineEdit.Password)

        self.ui.labelInfo.setStyleSheet("color: red; font-size: 14px;")

        self.ui.pushButtonIP.clicked.connect(self.changeIP)

        self.adjust_pos()

    def adjust_pos(self):
        X = (self.w - self.ui.widgetMain.width()) // 2
        Y = (self.h - self.ui.widgetMain.height()) // 2
        self.ui.widgetMain.move(X, Y)
        logger.debug(f"LoginWidget position: {X=}, {Y=}")
    
    def switch_to_register(self):
        logger.debug("Switching to register window")
        self.stack_widget.setCurrentIndex(2)
    
    def login(self):
        self.ui.labelInfo.setStyleSheet("color: red; font-size: 14px;")
        self.ui.labelInfo.setText("")

        ok = validate_user(self.ui.lineEditEmail.text())
        if not ok:
            logger.error("Email is not valid")
            self.ui.labelInfo.setText("Некорректный email!")
            return
        
        ok, message = check_password(self.ui.lineEditPassword.text())
        if not ok:
            logger.error("Password is not valid")
            self.ui.labelInfo.setText(message)
            return
        
        logger.debug("Email and password are valid")
        
        ok, msg = login_request(self.ui.lineEditEmail.text(), self.ui.lineEditPassword.text())
        if ok:
            update_token_in_json_and_config(msg)
            self.stack_widget.setCurrentIndex(0)
        else:
            self.ui.labelInfo.setText(msg)
            return
    
    def changeIP(self):
        dialog = ChangeIPDialog()
        dialog.exec()

class RegisterWidget(QWidget):
    def __init__(self, w, h, stack):
        super().__init__()
        self.w = w
        self.h = h
        self.stack_widget = stack

        self.ui = Ui_RegisterWidget()
        self.ui.setupUi(self)

        self.ui.pushButtonToLogin.clicked.connect(self.switch_to_login)
        self.ui.pushButtonRegister.clicked.connect(self.register)

        self.ui.pushButtonIP.clicked.connect(self.changeIP)

        self.adjust_pos()

    def adjust_pos(self):
        X = (self.w - self.ui.widgetMain.width()) // 2
        Y = (self.h - self.ui.widgetMain.height()) // 2
        self.ui.widgetMain.move(X, Y)
        logger.debug(f"RegisterWidget position: {X=}, {Y=}")
    
    def switch_to_login(self):
        logger.debug("Switching to login window")
        self.stack_widget.setCurrentIndex(1)
    
    def register(self):
        self.ui.labelInfo.setStyleSheet("color: red; font-size: 14px;")
        self.ui.labelInfo.setText("")

        ok = validate_user(self.ui.lineEditEmail.text())
        if not ok:
            logger.error("Email is not valid")
            self.ui.labelInfo.setText("Некорректный email!")
            return
        
        ok, message = check_password(self.ui.lineEditPassword.text())
        if not ok:
            logger.error("Password is not valid")
            self.ui.labelInfo.setText(message)
            return
        
        ok = self.ui.lineEditPassword.text() == self.ui.lineEditPassword_2.text()
        if not ok:
            logger.error("Passwords do not match")
            self.ui.labelInfo.setText("Пароли не совпадают!")
            return

        logger.debug("Email and password are valid")
        
        ok, msg = register_request(self.ui.lineEditEmail.text(), self.ui.lineEditPassword.text())
        if ok:
            login_widget = self.stack_widget.widget(1)
            login_widget.ui.labelInfo.setStyleSheet("color: green; font-size: 14px;")
            login_widget.ui.labelInfo.setText(msg)
            self.stack_widget.setCurrentIndex(1)
            # self.ui.labelInfo.setStyleSheet("color: green; font-size: 14px;")
            # self.ui.labelInfo.setText(msg)
        else:
            self.ui.labelInfo.setText(msg)
            return

    def changeIP(self):
        dialog = ChangeIPDialog()
        dialog.exec()