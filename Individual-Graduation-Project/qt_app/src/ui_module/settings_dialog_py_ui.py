# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings_dialog_ui.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.pushButtonIP = QPushButton(self.widget)
        self.pushButtonIP.setObjectName(u"pushButtonIP")
        self.pushButtonIP.setGeometry(QRect(110, 40, 151, 41))

        self.verticalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(Dialog)
        self.widget_2.setObjectName(u"widget_2")
        self.pushButtonPaths = QPushButton(self.widget_2)
        self.pushButtonPaths.setObjectName(u"pushButtonPaths")
        self.pushButtonPaths.setGeometry(QRect(110, 50, 151, 41))

        self.verticalLayout.addWidget(self.widget_2)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.pushButtonIP.setText(QCoreApplication.translate("Dialog", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c IP \u0441\u0435\u0440\u0432\u0435\u0440\u0430", None))
        self.pushButtonPaths.setText(QCoreApplication.translate("Dialog", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u043f\u0443\u0442\u0438 \u043a \u0444\u0430\u0439\u043b\u0430\u043c", None))
    # retranslateUi

