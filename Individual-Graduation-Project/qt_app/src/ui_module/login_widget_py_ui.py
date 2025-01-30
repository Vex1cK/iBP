# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_widget_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_LoginWidget(object):
    def setupUi(self, LoginWidget):
        if not LoginWidget.objectName():
            LoginWidget.setObjectName(u"LoginWidget")
        LoginWidget.resize(708, 483)
        self.widgetMain = QWidget(LoginWidget)
        self.widgetMain.setObjectName(u"widgetMain")
        self.widgetMain.setGeometry(QRect(160, 80, 381, 331))
        self.layoutWidget_2 = QWidget(self.widgetMain)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(10, 10, 361, 71))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_5 = QWidget(self.layoutWidget_2)
        self.widget_5.setObjectName(u"widget_5")
        self.labelPlease = QLabel(self.widget_5)
        self.labelPlease.setObjectName(u"labelPlease")
        self.labelPlease.setGeometry(QRect(30, 10, 301, 51))

        self.verticalLayout_2.addWidget(self.widget_5)

        self.layoutWidget = QWidget(self.widgetMain)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 240, 361, 81))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.layoutWidget)
        self.widget_2.setObjectName(u"widget_2")
        self.pushButtonCreate = QPushButton(self.widget_2)
        self.pushButtonCreate.setObjectName(u"pushButtonCreate")
        self.pushButtonCreate.setGeometry(QRect(0, 10, 141, 51))

        self.horizontalLayout_2.addWidget(self.widget_2)

        self.widget = QWidget(self.layoutWidget)
        self.widget.setObjectName(u"widget")
        self.pushButtonLogin = QPushButton(self.widget)
        self.pushButtonLogin.setObjectName(u"pushButtonLogin")
        self.pushButtonLogin.setGeometry(QRect(10, 10, 141, 51))
        self.pushButtonIP = QPushButton(self.widget)
        self.pushButtonIP.setObjectName(u"pushButtonIP")
        self.pushButtonIP.setGeometry(QRect(150, 40, 21, 21))

        self.horizontalLayout_2.addWidget(self.widget)

        self.layoutWidget1 = QWidget(self.widgetMain)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 90, 361, 151))
        self.verticalLayout = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.layoutWidget1)
        self.widget_3.setObjectName(u"widget_3")
        self.lineEditEmail = QLineEdit(self.widget_3)
        self.lineEditEmail.setObjectName(u"lineEditEmail")
        self.lineEditEmail.setGeometry(QRect(0, 10, 331, 31))

        self.verticalLayout.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.layoutWidget1)
        self.widget_4.setObjectName(u"widget_4")
        self.lineEditPassword = QLineEdit(self.widget_4)
        self.lineEditPassword.setObjectName(u"lineEditPassword")
        self.lineEditPassword.setGeometry(QRect(0, 10, 331, 31))

        self.verticalLayout.addWidget(self.widget_4)

        self.widget_7 = QWidget(self.layoutWidget1)
        self.widget_7.setObjectName(u"widget_7")
        self.labelInfo = QLabel(self.widget_7)
        self.labelInfo.setObjectName(u"labelInfo")
        self.labelInfo.setGeometry(QRect(0, 10, 331, 31))

        self.verticalLayout.addWidget(self.widget_7)


        self.retranslateUi(LoginWidget)

        QMetaObject.connectSlotsByName(LoginWidget)
    # setupUi

    def retranslateUi(self, LoginWidget):
        LoginWidget.setWindowTitle(QCoreApplication.translate("LoginWidget", u"Form", None))
        self.labelPlease.setText(QCoreApplication.translate("LoginWidget", u"<html><head/><body><p><span style=\" font-size:14pt;\">\u041f\u043e\u0436\u0430\u043b\u0443\u0439\u0441\u0442\u0430, \u0432\u043e\u0439\u0434\u0438\u0442\u0435 \u0432 \u0430\u043a\u043a\u0430\u0443\u043d\u0442</span></p></body></html>", None))
        self.pushButtonCreate.setText(QCoreApplication.translate("LoginWidget", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u0430\u043a\u043a\u0430\u0443\u043d\u0442", None))
        self.pushButtonLogin.setText(QCoreApplication.translate("LoginWidget", u"\u0412\u043e\u0439\u0442\u0438", None))
        self.pushButtonIP.setText(QCoreApplication.translate("LoginWidget", u"IP", None))
        self.lineEditEmail.setInputMask("")
        self.lineEditEmail.setText("")
        self.lineEditEmail.setPlaceholderText(QCoreApplication.translate("LoginWidget", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 email", None))
        self.lineEditPassword.setPlaceholderText(QCoreApplication.translate("LoginWidget", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.labelInfo.setText(QCoreApplication.translate("LoginWidget", u"<html><head/><body><p><br/></p></body></html>", None))
    # retranslateUi

