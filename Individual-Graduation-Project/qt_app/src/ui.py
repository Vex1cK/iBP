# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui.ui'
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QSizePolicy,
    QStatusBar, QTabWidget, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(998, 622)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabs = QTabWidget(self.centralwidget)
        self.tabs.setObjectName(u"tabs")
        self.tabs.setGeometry(QRect(0, 0, 991, 611))
        self.tabMain = QWidget()
        self.tabMain.setObjectName(u"tabMain")
        self.buttonStart = QPushButton(self.tabMain)
        self.buttonStart.setObjectName(u"buttonStart")
        self.buttonStart.setGeometry(QRect(210, 30, 261, 161))
        self.buttonStop = QPushButton(self.tabMain)
        self.buttonStop.setObjectName(u"buttonStop")
        self.buttonStop.setGeometry(QRect(210, 290, 261, 231))
        self.buttonSettings = QPushButton(self.tabMain)
        self.buttonSettings.setObjectName(u"buttonSettings")
        self.buttonSettings.setGeometry(QRect(620, 30, 231, 201))
        self.tabs.addTab(self.tabMain, "")
        self.tabAudio = QWidget()
        self.tabAudio.setObjectName(u"tabAudio")
        self.buttonRefresh = QPushButton(self.tabAudio)
        self.buttonRefresh.setObjectName(u"buttonRefresh")
        self.buttonRefresh.setGeometry(QRect(760, 20, 211, 41))
        self.treeContainer = QWidget(self.tabAudio)
        self.treeContainer.setObjectName(u"treeContainer")
        self.treeContainer.setGeometry(QRect(20, 10, 711, 531))
        self.tabs.addTab(self.tabAudio, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabs.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.buttonStart.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447\u0430\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c", None))
        self.buttonStop.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c", None))
        self.buttonSettings.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.tabs.setTabText(self.tabs.indexOf(self.tabMain), QCoreApplication.translate("MainWindow", u"\u0413\u043b\u0430\u0432\u043d\u0430\u044f", None))
        self.buttonRefresh.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c \u0441\u043f\u0438\u0441\u043e\u043a \u0444\u0430\u0439\u043b\u043e\u0432", None))
        self.tabs.setTabText(self.tabs.indexOf(self.tabAudio), QCoreApplication.translate("MainWindow", u"\u0410\u0443\u0434\u0438\u043e \u0437\u0430\u043f\u0438\u0441\u0438", None))
    # retranslateUi

