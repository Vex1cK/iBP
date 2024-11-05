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
        self.buttonSettings = QPushButton(self.widget)
        self.buttonSettings.setObjectName(u"buttonSettings")
        self.buttonSettings.setGeometry(QRect(120, 10, 181, 51))
        sizePolicy.setHeightForWidth(self.buttonSettings.sizePolicy().hasHeightForWidth())
        self.buttonSettings.setSizePolicy(sizePolicy)

        self.verticalLayout_4.addWidget(self.widget)


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
        self.buttonRefresh_2 = QPushButton(self.widget_10)
        self.buttonRefresh_2.setObjectName(u"buttonRefresh_2")
        self.buttonRefresh_2.setGeometry(QRect(30, 20, 211, 41))

        self.verticalLayout_5.addWidget(self.widget_10)

        self.widget_11 = QWidget(self.tabAudio)
        self.widget_11.setObjectName(u"widget_11")
        self.buttonRefresh_3 = QPushButton(self.widget_11)
        self.buttonRefresh_3.setObjectName(u"buttonRefresh_3")
        self.buttonRefresh_3.setGeometry(QRect(30, 20, 211, 41))

        self.verticalLayout_5.addWidget(self.widget_11)


        self.gridLayout_5.addLayout(self.verticalLayout_5, 0, 1, 1, 1)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.widget_12 = QWidget(self.tabAudio)
        self.widget_12.setObjectName(u"widget_12")

        self.verticalLayout_6.addWidget(self.widget_12)


        self.gridLayout_5.addLayout(self.verticalLayout_6, 1, 1, 1, 1)

        self.gridLayout_5.setColumnStretch(0, 3)
        self.gridLayout_5.setColumnStretch(1, 1)
        self.tabs.addTab(self.tabAudio, "")

        self.gridLayout.addWidget(self.tabs, 0, 1, 1, 1)


        self.retranslateUi(MainWidget)

        self.tabs.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWidget)
    # setupUi

    def retranslateUi(self, MainWidget):
        MainWidget.setWindowTitle(QCoreApplication.translate("MainWidget", u"MainWidget", None))
        self.buttonStart.setText(QCoreApplication.translate("MainWidget", u"\u041d\u0430\u0447\u0430\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c", None))
        self.buttonStop.setText(QCoreApplication.translate("MainWidget", u"\u041e\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c", None))
        self.buttonSettings.setText(QCoreApplication.translate("MainWidget", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.labelServerStatus.setText(QCoreApplication.translate("MainWidget", u"<html><head/><body><p><span style=\" font-size:14pt;\">\u0414\u043e\u0441\u0442\u0443\u043f \u043a \u0441\u0435\u0440\u0432\u0435\u0440\u0443: %%</span></p></body></html>", None))
        self.labelCountAudio.setText(QCoreApplication.translate("MainWidget", u"<html><head/><body><p><span style=\" font-size:14pt;\">\u0412\u0441\u0435\u0433\u043e \u0430\u0443\u0434\u0438\u043e \u0444\u0430\u0439\u043b\u043e\u0432: %%</span></p></body></html>", None))
        self.labelCountFolders.setText(QCoreApplication.translate("MainWidget", u"<html><head/><body><p><span style=\" font-size:14pt;\">\u0412\u0441\u0435\u0433\u043e \u043f\u0430\u043f\u043e\u043a \u0441 \u0437\u0430\u043f\u0438\u0441\u044f\u043c\u0438</span></p><p><span style=\" font-size:14pt;\">\u0441\u043e\u0437\u0432\u043e\u043d\u043e\u0432: %%</span></p></body></html>", None))
        self.labelPing.setText(QCoreApplication.translate("MainWidget", u"<html><head/><body><p><span style=\" font-size:14pt;\">\u0417\u0430\u0434\u0435\u0440\u0436\u043a\u0430 \u0434\u043e \u0441\u0435\u0440\u0432\u0435\u0440\u0430: %%</span></p></body></html>", None))
        self.tabs.setTabText(self.tabs.indexOf(self.tabMain), QCoreApplication.translate("MainWidget", u"\u0413\u043b\u0430\u0432\u043d\u0430\u044f", None))
        self.buttonRefresh.setText(QCoreApplication.translate("MainWidget", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c \u0441\u043f\u0438\u0441\u043e\u043a \u0444\u0430\u0439\u043b\u043e\u0432", None))
        self.buttonRefresh_2.setText(QCoreApplication.translate("MainWidget", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c \u0441\u043f\u0438\u0441\u043e\u043a \u0444\u0430\u0439\u043b\u043e\u0432", None))
        self.buttonRefresh_3.setText(QCoreApplication.translate("MainWidget", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c \u0441\u043f\u0438\u0441\u043e\u043a \u0444\u0430\u0439\u043b\u043e\u0432", None))
        self.tabs.setTabText(self.tabs.indexOf(self.tabAudio), QCoreApplication.translate("MainWidget", u"\u0410\u0443\u0434\u0438\u043e \u0437\u0430\u043f\u0438\u0441\u0438", None))
    # retranslateUi

