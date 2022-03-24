# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainForm.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(575, 204)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.labelFilePath = QLabel(self.centralwidget)
        self.labelFilePath.setObjectName(u"labelFilePath")
        self.labelFilePath.setGeometry(QRect(10, 20, 171, 31))
        font = QFont()
        font.setPointSize(11)
        self.labelFilePath.setFont(font)
        self.lineEditFilePath = QLineEdit(self.centralwidget)
        self.lineEditFilePath.setObjectName(u"lineEditFilePath")
        self.lineEditFilePath.setGeometry(QRect(170, 24, 341, 31))
        self.toolButtonFilePath = QToolButton(self.centralwidget)
        self.toolButtonFilePath.setObjectName(u"toolButtonFilePath")
        self.toolButtonFilePath.setGeometry(QRect(480, 30, 25, 19))
        self.pushButtonApplyFilter = QPushButton(self.centralwidget)
        self.pushButtonApplyFilter.setObjectName(u"pushButtonApplyFilter")
        self.pushButtonApplyFilter.setGeometry(QRect(210, 100, 121, 41))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 575, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.labelFilePath.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043f\u0443\u0442\u044c \u043a \u0444\u0430\u0439\u043b\u0443:", None))
        self.toolButtonFilePath.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.pushButtonApplyFilter.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c \u0444\u0438\u043b\u044c\u0442\u0440", None))
    # retranslateUi

