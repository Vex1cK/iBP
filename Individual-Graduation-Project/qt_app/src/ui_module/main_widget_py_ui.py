# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_widget_ui.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QPushButton,
    QSizePolicy, QTabWidget, QVBoxLayout, QWidget)

class Ui_MainWidget(object):
    def setupUi(self, MainWidget):
        if not MainWidget.objectName():
            MainWidget.setObjectName(u"MainWidget")
        MainWidget.resize(998, 622)
        self.gridLayout = QGridLayout(MainWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabs = QTabWidget(MainWidget)
        self.tabs.setObjectName(u"tabs")
        self.tabMain = QWidget()
        self.tabMain.setObjectName(u"tabMain")
        self.gridLayout_4 = QGridLayout(self.tabMain)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_2 = QWidget(self.tabMain)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.buttonStart = QPushButton(self.widget_2)
        self.buttonStart.setObjectName(u"buttonStart")
        self.buttonStart.setGeometry(QRect(120, 30, 181, 91))
        sizePolicy.setHeightForWidth(self.buttonStart.sizePolicy().hasHeightForWidth())
        self.buttonStart.setSizePolicy(sizePolicy)
        self.buttonStart.setMinimumSize(QSize(0, 0))

        self.verticalLayout.addWidget(self.widget_2)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_3 = QWidget(self.tabMain)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.buttonStop = QPushButton(self.widget_3)
        self.buttonStop.setObjectName(u"buttonStop")
        self.buttonStop.setGeometry(QRect(120, 10, 181, 91))
        sizePolicy.setHeightForWidth(self.buttonStop.sizePolicy().hasHeightForWidth())
        self.buttonStop.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.widget_3)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.gridLayout_4.addLayout(self.verticalLayout_3, 1, 1, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.widget = QWidget(self.tabMain)
        self.widget.setObjectName(u"widget")
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.buttonLogOut = QPushButton(self.widget)
        self.buttonLogOut.setObjectName(u"buttonLogOut")
        self.buttonLogOut.setGeometry(QRect(120, 10, 181, 51))
        sizePolicy.setHeightForWidth(self.buttonLogOut.sizePolicy().hasHeightForWidth())
        self.buttonLogOut.setSizePolicy(sizePolicy)

        self.verticalLayout_4.addWidget(self.widget)

        self.widget_18 = QWidget(self.tabMain)
        self.widget_18.setObjectName(u"widget_18")
        self.buttonSettings = QPushButton(self.widget_18)
        self.buttonSettings.setObjectName(u"buttonSettings")
        self.buttonSettings.setGeometry(QRect(120, 30, 181, 51))
        sizePolicy.setHeightForWidth(self.buttonSettings.sizePolicy().hasHeightForWidth())
        self.buttonSettings.setSizePolicy(sizePolicy)

        self.verticalLayout_4.addWidget(self.widget_18)

        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(1, 1)

        self.gridLayout_4.addLayout(self.verticalLayout_4, 0, 1, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.widget_7 = QWidget(self.tabMain)
        self.widget_7.setObjectName(u"widget_7")
        self.labelServerStatus = QLabel(self.widget_7)
        self.labelServerStatus.setObjectName(u"labelServerStatus")
        self.labelServerStatus.setGeometry(QRect(0, 10, 311, 81))

        self.gridLayout_3.addWidget(self.widget_7, 0, 0, 1, 1)

        self.widget_6 = QWidget(self.tabMain)
        self.widget_6.setObjectName(u"widget_6")
        self.labelCountAudio = QLabel(self.widget_6)
        self.labelCountAudio.setObjectName(u"labelCountAudio")
        self.labelCountAudio.setGeometry(QRect(0, 20, 311, 115))

        self.gridLayout_3.addWidget(self.widget_6, 1, 0, 1, 1)

        self.widget_5 = QWidget(self.tabMain)
        self.widget_5.setObjectName(u"widget_5")
        self.labelCountFolders = QLabel(self.widget_5)
        self.labelCountFolders.setObjectName(u"labelCountFolders")
        self.labelCountFolders.setGeometry(QRect(0, 20, 311, 111))

        self.gridLayout_3.addWidget(self.widget_5, 1, 1, 1, 1)

        self.widget_4 = QWidget(self.tabMain)
        self.widget_4.setObjectName(u"widget_4")
        self.labelPing = QLabel(self.widget_4)
        self.labelPing.setObjectName(u"labelPing")
        self.labelPing.setGeometry(QRect(0, 10, 311, 81))

        self.gridLayout_3.addWidget(self.widget_4, 0, 1, 1, 1)

        self.gridLayout_3.setRowStretch(0, 1)
        self.gridLayout_3.setRowStretch(1, 2)

        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 2, 1)

        self.gridLayout_4.setColumnStretch(0, 2)
        self.gridLayout_4.setColumnStretch(1, 1)
        self.tabs.addTab(self.tabMain, "")
        self.tabAudio = QWidget()
        self.tabAudio.setObjectName(u"tabAudio")
        self.gridLayout_5 = QGridLayout(self.tabAudio)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.treeContainer = QWidget(self.tabAudio)
        self.treeContainer.setObjectName(u"treeContainer")

        self.verticalLayout_7.addWidget(self.treeContainer)


        self.gridLayout_5.addLayout(self.verticalLayout_7, 0, 0, 2, 1)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.widget_8 = QWidget(self.tabAudio)
        self.widget_8.setObjectName(u"widget_8")
        self.buttonRefresh = QPushButton(self.widget_8)
        self.buttonRefresh.setObjectName(u"buttonRefresh")
        self.buttonRefresh.setGeometry(QRect(30, 20, 211, 41))

        self.verticalLayout_5.addWidget(self.widget_8)

        self.widget_10 = QWidget(self.tabAudio)
        self.widget_10.setObjectName(u"widget_10")
        self.buttonAudio2Text = QPushButton(self.widget_10)
        self.buttonAudio2Text.setObjectName(u"buttonAudio2Text")
        self.buttonAudio2Text.setGeometry(QRect(30, 20, 211, 41))

        self.verticalLayout_5.addWidget(self.widget_10)

        self.widget_11 = QWidget(self.tabAudio)
        self.widget_11.setObjectName(u"widget_11")
        self.buttonAudio2TextAndSum = QPushButton(self.widget_11)
        self.buttonAudio2TextAndSum.setObjectName(u"buttonAudio2TextAndSum")
        self.buttonAudio2TextAndSum.setGeometry(QRect(30, 20, 211, 41))

        self.verticalLayout_5.addWidget(self.widget_11)


        self.gridLayout_5.addLayout(self.verticalLayout_5, 0, 1, 1, 1)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.widget_12 = QWidget(self.tabAudio)
        self.widget_12.setObjectName(u"widget_12")
        self.labelInfoAudioTab = QLabel(self.widget_12)
        self.labelInfoAudioTab.setObjectName(u"labelInfoAudioTab")
        self.labelInfoAudioTab.setGeometry(QRect(10, 10, 221, 131))

        self.verticalLayout_6.addWidget(self.widget_12)


        self.gridLayout_5.addLayout(self.verticalLayout_6, 1, 1, 1, 1)

        self.gridLayout_5.setColumnStretch(0, 3)
        self.gridLayout_5.setColumnStretch(1, 1)
        self.tabs.addTab(self.tabAudio, "")
        self.tabFullText = QWidget()
        self.tabFullText.setObjectName(u"tabFullText")
        self.gridLayout_2 = QGridLayout(self.tabFullText)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.treeContainer_2 = QWidget(self.tabFullText)
        self.treeContainer_2.setObjectName(u"treeContainer_2")

        self.verticalLayout_9.addWidget(self.treeContainer_2)


        self.gridLayout_2.addLayout(self.verticalLayout_9, 0, 0, 2, 1)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setSpacing(5)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(-1, 0, -1, 0)
        self.widget_9 = QWidget(self.tabFullText)
        self.widget_9.setObjectName(u"widget_9")
        self.buttonRefreshFullText = QPushButton(self.widget_9)
        self.buttonRefreshFullText.setObjectName(u"buttonRefreshFullText")
        self.buttonRefreshFullText.setGeometry(QRect(30, 20, 211, 41))

        self.verticalLayout_8.addWidget(self.widget_9)

        self.widget_13 = QWidget(self.tabFullText)
        self.widget_13.setObjectName(u"widget_13")
        self.buttonSumText = QPushButton(self.widget_13)
        self.buttonSumText.setObjectName(u"buttonSumText")
        self.buttonSumText.setGeometry(QRect(30, 20, 211, 41))

        self.verticalLayout_8.addWidget(self.widget_13)

        self.verticalLayout_8.setStretch(0, 1)
        self.verticalLayout_8.setStretch(1, 2)

        self.gridLayout_2.addLayout(self.verticalLayout_8, 0, 1, 1, 1)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.widget_15 = QWidget(self.tabFullText)
        self.widget_15.setObjectName(u"widget_15")
        self.labelInfoFullTextTab = QLabel(self.widget_15)
        self.labelInfoFullTextTab.setObjectName(u"labelInfoFullTextTab")
        self.labelInfoFullTextTab.setGeometry(QRect(10, 10, 221, 131))

        self.verticalLayout_10.addWidget(self.widget_15)

        self.verticalLayout_10.setStretch(0, 1)

        self.gridLayout_2.addLayout(self.verticalLayout_10, 1, 1, 1, 1)

        self.gridLayout_2.setColumnStretch(0, 3)
        self.gridLayout_2.setColumnStretch(1, 1)
        self.tabs.addTab(self.tabFullText, "")
        self.tabSumText = QWidget()
        self.tabSumText.setObjectName(u"tabSumText")
        self.gridLayout_6 = QGridLayout(self.tabSumText)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.treeContainer_3 = QWidget(self.tabSumText)
        self.treeContainer_3.setObjectName(u"treeContainer_3")

        self.verticalLayout_11.addWidget(self.treeContainer_3)


        self.gridLayout_6.addLayout(self.verticalLayout_11, 0, 0, 2, 1)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setSpacing(5)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(-1, 0, -1, 0)
        self.widget_14 = QWidget(self.tabSumText)
        self.widget_14.setObjectName(u"widget_14")
        self.buttonRefreshSumText = QPushButton(self.widget_14)
        self.buttonRefreshSumText.setObjectName(u"buttonRefreshSumText")
        self.buttonRefreshSumText.setGeometry(QRect(30, 20, 211, 41))

        self.verticalLayout_12.addWidget(self.widget_14)

        self.widget_16 = QWidget(self.tabSumText)
        self.widget_16.setObjectName(u"widget_16")

        self.verticalLayout_12.addWidget(self.widget_16)


        self.gridLayout_6.addLayout(self.verticalLayout_12, 0, 1, 1, 1)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.widget_17 = QWidget(self.tabSumText)
        self.widget_17.setObjectName(u"widget_17")
        self.labelInfoSumTextTab = QLabel(self.widget_17)
        self.labelInfoSumTextTab.setObjectName(u"labelInfoSumTextTab")
        self.labelInfoSumTextTab.setGeometry(QRect(10, 10, 221, 131))

        self.verticalLayout_13.addWidget(self.widget_17)


        self.gridLayout_6.addLayout(self.verticalLayout_13, 1, 1, 1, 1)

        self.gridLayout_6.setColumnStretch(0, 3)
        self.gridLayout_6.setColumnStretch(1, 1)
        self.tabs.addTab(self.tabSumText, "")
        self.tabFolder = QWidget()
        self.tabFolder.setObjectName(u"tabFolder")
        self.tabs.addTab(self.tabFolder, "")

        self.gridLayout.addWidget(self.tabs, 0, 1, 1, 1)


        self.retranslateUi(MainWidget)

        self.tabs.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWidget)
    # setupUi

    def retranslateUi(self, MainWidget):
        MainWidget.setWindowTitle(QCoreApplication.translate("MainWidget", u"MainWidget", None))
        self.buttonStart.setText(QCoreApplication.translate("MainWidget", u"\u041d\u0430\u0447\u0430\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c", None))
        self.buttonStop.setText(QCoreApplication.translate("MainWidget", u"\u041e\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c", None))
        self.buttonLogOut.setText(QCoreApplication.translate("MainWidget", u"\u0412\u044b\u0439\u0442\u0438 \u0438\u0437 \u0430\u043a\u043a\u0430\u0443\u043d\u0442\u0430", None))
        self.buttonSettings.setText(QCoreApplication.translate("MainWidget", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.labelServerStatus.setText(QCoreApplication.translate("MainWidget", u"<html><head/><body><p><span style=\" font-size:14pt;\">\u0414\u043e\u0441\u0442\u0443\u043f \u043a \u0441\u0435\u0440\u0432\u0435\u0440\u0443: %%</span></p></body></html>", None))
        self.labelCountAudio.setText(QCoreApplication.translate("MainWidget", u"<html><head/><body><p><span style=\" font-size:14pt;\">\u0412\u0441\u0435\u0433\u043e \u0430\u0443\u0434\u0438\u043e \u0444\u0430\u0439\u043b\u043e\u0432: %%</span></p></body></html>", None))
        self.labelCountFolders.setText(QCoreApplication.translate("MainWidget", u"<html><head/><body><p><span style=\" font-size:14pt;\">\u0412\u0441\u0435\u0433\u043e \u043f\u0430\u043f\u043e\u043a \u0441 \u0437\u0430\u043f\u0438\u0441\u044f\u043c\u0438</span></p><p><span style=\" font-size:14pt;\">\u0441\u043e\u0437\u0432\u043e\u043d\u043e\u0432: %%</span></p></body></html>", None))
        self.labelPing.setText(QCoreApplication.translate("MainWidget", u"<html><head/><body><p><span style=\" font-size:14pt;\">\u0417\u0430\u0434\u0435\u0440\u0436\u043a\u0430 \u0434\u043e \u0441\u0435\u0440\u0432\u0435\u0440\u0430: %%</span></p></body></html>", None))
        self.tabs.setTabText(self.tabs.indexOf(self.tabMain), QCoreApplication.translate("MainWidget", u"\u0413\u043b\u0430\u0432\u043d\u0430\u044f", None))
        self.buttonRefresh.setText(QCoreApplication.translate("MainWidget", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c \u0441\u043f\u0438\u0441\u043e\u043a \u0444\u0430\u0439\u043b\u043e\u0432", None))
        self.buttonAudio2Text.setText(QCoreApplication.translate("MainWidget", u"\u041f\u0440\u0435\u043e\u0431\u0440\u0430\u0437\u043e\u0432\u0430\u0442\u044c \u0430\u0443\u0434\u0438\u043e \u0432 \u0442\u0435\u043a\u0441\u0442", None))
        self.buttonAudio2TextAndSum.setText(QCoreApplication.translate("MainWidget", u"\u041f\u0440\u0435\u043e\u0431\u0440\u0430\u0437\u043e\u0432\u0430\u0442\u044c \u0430\u0443\u0434\u0438\u043e\u0432 \u0442\u0435\u043a\u0441\u0442\n"
"       \u0438 \u0441\u0443\u043c\u043c\u0430\u0440\u0438\u0437\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.labelInfoAudioTab.setText("")
        self.tabs.setTabText(self.tabs.indexOf(self.tabAudio), QCoreApplication.translate("MainWidget", u"\u0410\u0443\u0434\u0438\u043e \u0437\u0430\u043f\u0438\u0441\u0438", None))
        self.buttonRefreshFullText.setText(QCoreApplication.translate("MainWidget", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c \u0441\u043f\u0438\u0441\u043e\u043a \u0444\u0430\u0439\u043b\u043e\u0432", None))
        self.buttonSumText.setText(QCoreApplication.translate("MainWidget", u"\u0421\u0443\u043c\u043c\u0430\u0440\u0438\u0437\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0442\u0435\u043a\u0441\u0442", None))
        self.labelInfoFullTextTab.setText("")
        self.tabs.setTabText(self.tabs.indexOf(self.tabFullText), QCoreApplication.translate("MainWidget", u"\u041f\u043e\u043b\u043d\u044b\u0435 \u0442\u0435\u043a\u0441\u0442\u043e\u0432\u044b\u0435 \u0440\u0430\u0441\u0448\u0438\u0444\u0440\u043e\u0432\u043a\u0438", None))
        self.buttonRefreshSumText.setText(QCoreApplication.translate("MainWidget", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c \u0441\u043f\u0438\u0441\u043e\u043a \u0444\u0430\u0439\u043b\u043e\u0432", None))
        self.labelInfoSumTextTab.setText("")
        self.tabs.setTabText(self.tabs.indexOf(self.tabSumText), QCoreApplication.translate("MainWidget", u"\u0421\u0443\u043c\u043c\u0430\u0440\u0438\u0437\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0435 \u0442\u0435\u043a\u0441\u0442\u043e\u0432\u044b\u0435 \u0440\u0430\u0441\u0448\u0438\u0444\u0440\u043e\u0432\u043a\u0438", None))
        self.tabs.setTabText(self.tabs.indexOf(self.tabFolder), QCoreApplication.translate("MainWidget", u"\u041f\u0430\u043f\u043a\u0438", None))
    # retranslateUi

