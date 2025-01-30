# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'chose_file_dialog_ui.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(669, 238)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 441, 51))

        self.horizontalLayout_3.addWidget(self.widget)

        self.widget_7 = QWidget(Dialog)
        self.widget_7.setObjectName(u"widget_7")

        self.horizontalLayout_3.addWidget(self.widget_7)

        self.horizontalLayout_3.setStretch(0, 3)
        self.horizontalLayout_3.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.widget_2 = QWidget(Dialog)
        self.widget_2.setObjectName(u"widget_2")
        self.lineEdit = QLineEdit(self.widget_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setEnabled(False)
        self.lineEdit.setGeometry(QRect(10, 20, 451, 31))

        self.horizontalLayout_2.addWidget(self.widget_2)

        self.widget_3 = QWidget(Dialog)
        self.widget_3.setObjectName(u"widget_3")
        self.pushButtonChoseFile = QPushButton(self.widget_3)
        self.pushButtonChoseFile.setObjectName(u"pushButtonChoseFile")
        self.pushButtonChoseFile.setGeometry(QRect(40, 20, 91, 31))

        self.horizontalLayout_2.addWidget(self.widget_3)

        self.horizontalLayout_2.setStretch(0, 3)
        self.horizontalLayout_2.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget_4 = QWidget(Dialog)
        self.widget_4.setObjectName(u"widget_4")
        self.pushButtonCancel = QPushButton(self.widget_4)
        self.pushButtonCancel.setObjectName(u"pushButtonCancel")
        self.pushButtonCancel.setGeometry(QRect(10, 20, 71, 31))

        self.horizontalLayout.addWidget(self.widget_4)

        self.widget_5 = QWidget(Dialog)
        self.widget_5.setObjectName(u"widget_5")

        self.horizontalLayout.addWidget(self.widget_5)

        self.widget_6 = QWidget(Dialog)
        self.widget_6.setObjectName(u"widget_6")
        self.pushButtonOk = QPushButton(self.widget_6)
        self.pushButtonOk.setObjectName(u"pushButtonOk")
        self.pushButtonOk.setGeometry(QRect(110, 20, 71, 31))

        self.horizontalLayout.addWidget(self.widget_6)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:14pt;\">\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0444\u0430\u0439\u043b</span></p></body></html>", None))
        self.pushButtonChoseFile.setText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0444\u0430\u0439\u043b", None))
        self.pushButtonCancel.setText(QCoreApplication.translate("Dialog", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.pushButtonOk.setText(QCoreApplication.translate("Dialog", u"\u041e\u041a", None))
    # retranslateUi

