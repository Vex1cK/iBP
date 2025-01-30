# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'change_paths_dialog_ui.ui'
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
        Dialog.resize(623, 438)
        self.verticalLayout_8 = QVBoxLayout(Dialog)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.label1 = QLabel(self.widget)
        self.label1.setObjectName(u"label1")
        self.label1.setGeometry(QRect(0, 0, 431, 31))

        self.verticalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(Dialog)
        self.widget_2.setObjectName(u"widget_2")
        self.lineEditAudioPath = QLineEdit(self.widget_2)
        self.lineEditAudioPath.setObjectName(u"lineEditAudioPath")
        self.lineEditAudioPath.setEnabled(False)
        self.lineEditAudioPath.setGeometry(QRect(0, 0, 441, 31))

        self.verticalLayout.addWidget(self.widget_2)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.widget_9 = QWidget(Dialog)
        self.widget_9.setObjectName(u"widget_9")
        self.pushButtonAudioPath = QPushButton(self.widget_9)
        self.pushButtonAudioPath.setObjectName(u"pushButtonAudioPath")
        self.pushButtonAudioPath.setGeometry(QRect(20, 40, 111, 31))

        self.horizontalLayout.addWidget(self.widget_9)

        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(1, 1)

        self.verticalLayout_8.addLayout(self.horizontalLayout)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.widget_13 = QWidget(Dialog)
        self.widget_13.setObjectName(u"widget_13")
        self.label2 = QLabel(self.widget_13)
        self.label2.setObjectName(u"label2")
        self.label2.setGeometry(QRect(0, 0, 431, 31))

        self.verticalLayout_5.addWidget(self.widget_13)

        self.widget_14 = QWidget(Dialog)
        self.widget_14.setObjectName(u"widget_14")
        self.lineEditFullTextPath = QLineEdit(self.widget_14)
        self.lineEditFullTextPath.setObjectName(u"lineEditFullTextPath")
        self.lineEditFullTextPath.setEnabled(False)
        self.lineEditFullTextPath.setGeometry(QRect(0, 0, 441, 31))

        self.verticalLayout_5.addWidget(self.widget_14)


        self.horizontalLayout_5.addLayout(self.verticalLayout_5)

        self.widget_15 = QWidget(Dialog)
        self.widget_15.setObjectName(u"widget_15")
        self.pushButtonFullTextPath = QPushButton(self.widget_15)
        self.pushButtonFullTextPath.setObjectName(u"pushButtonFullTextPath")
        self.pushButtonFullTextPath.setGeometry(QRect(20, 40, 111, 31))

        self.horizontalLayout_5.addWidget(self.widget_15)

        self.horizontalLayout_5.setStretch(0, 3)
        self.horizontalLayout_5.setStretch(1, 1)

        self.verticalLayout_8.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.widget_16 = QWidget(Dialog)
        self.widget_16.setObjectName(u"widget_16")
        self.label3 = QLabel(self.widget_16)
        self.label3.setObjectName(u"label3")
        self.label3.setGeometry(QRect(0, 0, 431, 31))

        self.verticalLayout_6.addWidget(self.widget_16)

        self.widget_17 = QWidget(Dialog)
        self.widget_17.setObjectName(u"widget_17")
        self.lineEditSumTextPath = QLineEdit(self.widget_17)
        self.lineEditSumTextPath.setObjectName(u"lineEditSumTextPath")
        self.lineEditSumTextPath.setEnabled(False)
        self.lineEditSumTextPath.setGeometry(QRect(0, 0, 441, 31))

        self.verticalLayout_6.addWidget(self.widget_17)


        self.horizontalLayout_6.addLayout(self.verticalLayout_6)

        self.widget_18 = QWidget(Dialog)
        self.widget_18.setObjectName(u"widget_18")
        self.pushButtonSumTextPath = QPushButton(self.widget_18)
        self.pushButtonSumTextPath.setObjectName(u"pushButtonSumTextPath")
        self.pushButtonSumTextPath.setGeometry(QRect(20, 40, 111, 31))

        self.horizontalLayout_6.addWidget(self.widget_18)

        self.horizontalLayout_6.setStretch(0, 3)
        self.horizontalLayout_6.setStretch(1, 1)

        self.verticalLayout_8.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.widget_19 = QWidget(Dialog)
        self.widget_19.setObjectName(u"widget_19")
        self.label4 = QLabel(self.widget_19)
        self.label4.setObjectName(u"label4")
        self.label4.setGeometry(QRect(0, 0, 431, 31))

        self.verticalLayout_7.addWidget(self.widget_19)

        self.widget_20 = QWidget(Dialog)
        self.widget_20.setObjectName(u"widget_20")
        self.lineEditFolderPath = QLineEdit(self.widget_20)
        self.lineEditFolderPath.setObjectName(u"lineEditFolderPath")
        self.lineEditFolderPath.setEnabled(False)
        self.lineEditFolderPath.setGeometry(QRect(0, 0, 441, 31))

        self.verticalLayout_7.addWidget(self.widget_20)


        self.horizontalLayout_7.addLayout(self.verticalLayout_7)

        self.widget_21 = QWidget(Dialog)
        self.widget_21.setObjectName(u"widget_21")
        self.pushButtonFolderPath = QPushButton(self.widget_21)
        self.pushButtonFolderPath.setObjectName(u"pushButtonFolderPath")
        self.pushButtonFolderPath.setGeometry(QRect(20, 40, 111, 31))

        self.horizontalLayout_7.addWidget(self.widget_21)

        self.horizontalLayout_7.setStretch(0, 3)
        self.horizontalLayout_7.setStretch(1, 1)

        self.verticalLayout_8.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.widget_22 = QWidget(Dialog)
        self.widget_22.setObjectName(u"widget_22")
        self.pushButtonCancel = QPushButton(self.widget_22)
        self.pushButtonCancel.setObjectName(u"pushButtonCancel")
        self.pushButtonCancel.setGeometry(QRect(10, 40, 91, 31))

        self.horizontalLayout_8.addWidget(self.widget_22)

        self.widget_3 = QWidget(Dialog)
        self.widget_3.setObjectName(u"widget_3")
        self.pushButtonOk = QPushButton(self.widget_3)
        self.pushButtonOk.setObjectName(u"pushButtonOk")
        self.pushButtonOk.setGeometry(QRect(130, 40, 91, 31))
        self.labelInfo = QLabel(self.widget_3)
        self.labelInfo.setObjectName(u"labelInfo")
        self.labelInfo.setGeometry(QRect(50, 10, 241, 31))

        self.horizontalLayout_8.addWidget(self.widget_3)

        self.widget_23 = QWidget(Dialog)
        self.widget_23.setObjectName(u"widget_23")
        self.pushButtonSave = QPushButton(self.widget_23)
        self.pushButtonSave.setObjectName(u"pushButtonSave")
        self.pushButtonSave.setGeometry(QRect(20, 40, 91, 31))

        self.horizontalLayout_8.addWidget(self.widget_23)

        self.horizontalLayout_8.setStretch(0, 1)
        self.horizontalLayout_8.setStretch(1, 3)
        self.horizontalLayout_8.setStretch(2, 1)

        self.verticalLayout_8.addLayout(self.horizontalLayout_8)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label1.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:12pt;\">\u041f\u0443\u0442\u044c \u043a \u043f\u0430\u043f\u043a\u0435 \u0441 \u0430\u0443\u0434\u0438\u043e \u0444\u0430\u0439\u043b\u0430\u043c\u0438:</span></p></body></html>", None))
        self.pushButtonAudioPath.setText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
        self.label2.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:12pt;\">\u041f\u0443\u0442\u044c \u043a \u043f\u0430\u043f\u043a\u0435 \u0441 \u043f\u043e\u043b\u043d\u044b\u043c\u0438 \u0442\u0435\u043a\u0441\u0442\u043e\u0432\u044b\u043c\u0438 \u0440\u0430\u0441\u0448\u0438\u0444\u0440\u043e\u0432\u043a\u0430\u043c\u0438:</span></p></body></html>", None))
        self.pushButtonFullTextPath.setText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
        self.label3.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:12pt;\">\u041f\u0443\u0442\u044c \u043a \u043f\u0430\u043f\u043a\u0435 \u0441 \u0441\u0443\u043c\u043c\u0430\u0440\u0438\u0437\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u043c\u0438 \u0440\u0430\u0441\u0448\u0438\u0444\u0440\u043e\u0432\u043a\u0430\u043c\u0438:</span></p></body></html>", None))
        self.pushButtonSumTextPath.setText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
        self.label4.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:12pt;\">\u041f\u0443\u0442\u044c \u043a \u043f\u0430\u043f\u043a\u0435 \u0441 \u043f\u0430\u043f\u043a\u0430\u043c\u0438 \u0441\u043e\u0437\u0432\u043e\u043d\u043e\u0432:</span></p></body></html>", None))
        self.pushButtonFolderPath.setText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
        self.pushButtonCancel.setText(QCoreApplication.translate("Dialog", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.pushButtonOk.setText(QCoreApplication.translate("Dialog", u"\u0413\u043e\u0442\u043e\u0432\u043e", None))
        self.labelInfo.setText("")
        self.pushButtonSave.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
    # retranslateUi

