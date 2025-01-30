# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'register_widget_ui.ui'
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

class Ui_RegisterWidget(object):
    def setupUi(self, RegisterWidget):
        if not RegisterWidget.objectName():
            RegisterWidget.setObjectName(u"RegisterWidget")
        RegisterWidget.resize(708, 483)
        self.widgetMain = QWidget(RegisterWidget)
        self.widgetMain.setObjectName(u"widgetMain")
        self.widgetMain.setGeometry(QRect(150, 50, 381, 381))
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
        self.layoutWidget.setGeometry(QRect(10, 290, 361, 81))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.layoutWidget)
        self.widget_2.setObjectName(u"widget_2")
        self.pushButtonToLogin = QPushButton(self.widget_2)
        self.pushButtonToLogin.setObjectName(u"pushButtonToLogin")
        self.pushButtonToLogin.setGeometry(QRect(0, 10, 141, 51))

        self.horizontalLayout_2.addWidget(self.widget_2)

        self.widget = QWidget(self.layoutWidget)
        self.widget.setObjectName(u"widget")
        self.pushButtonRegister = QPushButton(self.widget)
        self.pushButtonRegister.setObjectName(u"pushButtonRegister")
        self.pushButtonRegister.setGeometry(QRect(10, 10, 141, 51))
        self.pushButtonIP = QPushButton(self.widget)
        self.pushButtonIP.setObjectName(u"pushButtonIP")
        self.pushButtonIP.setGeometry(QRect(150, 40, 21, 21))

        self.horizontalLayout_2.addWidget(self.widget)

        self.layoutWidget1 = QWidget(self.widgetMain)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 80, 361, 211))
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

        self.widget_6 = QWidget(self.layoutWidget1)
        self.widget_6.setObjectName(u"widget_6")
        self.lineEditPassword_2 = QLineEdit(self.widget_6)
        self.lineEditPassword_2.setObjectName(u"lineEditPassword_2")
        self.lineEditPassword_2.setGeometry(QRect(0, 10, 331, 31))

        self.verticalLayout.addWidget(self.widget_6)

        self.widget_7 = QWidget(self.layoutWidget1)
        self.widget_7.setObjectName(u"widget_7")
        self.labelInfo = QLabel(self.widget_7)
        self.labelInfo.setObjectName(u"labelInfo")
        self.labelInfo.setGeometry(QRect(0, 10, 331, 31))

        self.verticalLayout.addWidget(self.widget_7)


        self.retranslateUi(RegisterWidget)

        QMetaObject.connectSlotsByName(RegisterWidget)
    # setupUi

    def retranslateUi(self, RegisterWidget):
        RegisterWidget.setWindowTitle(QCoreApplication.translate("RegisterWidget", u"Form", None))
        self.labelPlease.setText(QCoreApplication.translate("RegisterWidget", u"<html><head/><body><p><span style=\" font-size:14pt;\">\u041f\u043e\u0436\u0430\u043b\u0443\u0439\u0441\u0442\u0430, \u0441\u043e\u0437\u0434\u0430\u0439\u0442\u0435 \u0430\u043a\u043a\u0430\u0443\u043d\u0442</span></p></body></html>", None))
        self.pushButtonToLogin.setText(QCoreApplication.translate("RegisterWidget", u"\u0412\u043e\u0439\u0442\u0438 \u0432 \u0443\u0436\u0435\n"
"\u0441\u0443\u0449\u0435\u0441\u0442\u0432\u0443\u044e\u0449\u0438\u0439 \u0430\u043a\u043a\u0430\u0443\u043d\u0442", None))
        self.pushButtonRegister.setText(QCoreApplication.translate("RegisterWidget", u"\u0417\u0430\u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c\u0441\u044f", None))
        self.pushButtonIP.setText(QCoreApplication.translate("RegisterWidget", u"IP", None))
        self.lineEditEmail.setInputMask("")
        self.lineEditEmail.setText("")
        self.lineEditEmail.setPlaceholderText(QCoreApplication.translate("RegisterWidget", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 email", None))
        self.lineEditPassword.setPlaceholderText(QCoreApplication.translate("RegisterWidget", u"\u041f\u0440\u0438\u0434\u0443\u043c\u0430\u0439\u0442\u0435 \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.lineEditPassword_2.setPlaceholderText(QCoreApplication.translate("RegisterWidget", u"\u041f\u043e\u0432\u0442\u043e\u0440\u0438\u0442\u0435 \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.labelInfo.setText(QCoreApplication.translate("RegisterWidget", u"<html><head/><body><p><br/></p></body></html>", None))
    # retranslateUi

