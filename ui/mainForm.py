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
        MainWindow.resize(712, 378)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(self.frame)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.buttonGraph = QPushButton(self.tab)
        self.buttonGraph.setObjectName(u"buttonGraph")
        self.buttonGraph.setGeometry(QRect(470, 180, 91, 51))
        self.buttonPlay = QPushButton(self.tab)
        self.buttonPlay.setObjectName(u"buttonPlay")
        self.buttonPlay.setGeometry(QRect(170, 180, 91, 51))
        self.buttonPlay.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.buttonSave = QPushButton(self.tab)
        self.buttonSave.setObjectName(u"buttonSave")
        self.buttonSave.setGeometry(QRect(370, 180, 91, 51))
        self.labelFilePath = QLabel(self.tab)
        self.labelFilePath.setObjectName(u"labelFilePath")
        self.labelFilePath.setGeometry(QRect(70, 70, 171, 31))
        font = QFont()
        font.setPointSize(11)
        self.labelFilePath.setFont(font)
        self.lineEditFilePath = QLineEdit(self.tab)
        self.lineEditFilePath.setObjectName(u"lineEditFilePath")
        self.lineEditFilePath.setGeometry(QRect(230, 74, 341, 31))
        self.pushButtonApplyFilter = QPushButton(self.tab)
        self.pushButtonApplyFilter.setObjectName(u"pushButtonApplyFilter")
        self.pushButtonApplyFilter.setGeometry(QRect(320, 130, 121, 41))
        self.buttonStop = QPushButton(self.tab)
        self.buttonStop.setObjectName(u"buttonStop")
        self.buttonStop.setGeometry(QRect(270, 180, 91, 51))
        self.toolButtonFilePath = QToolButton(self.tab)
        self.toolButtonFilePath.setObjectName(u"toolButtonFilePath")
        self.toolButtonFilePath.setGeometry(QRect(580, 80, 25, 19))
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.widget = QWidget(self.tab_2)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(40, 60, 254, 102))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.blendWheel = QDial(self.widget)
        self.blendWheel.setObjectName(u"blendWheel")
        self.blendWheel.setMaximum(10000)
        self.blendWheel.setSingleStep(1)
        self.blendWheel.setPageStep(10)
        self.blendWheel.setWrapping(False)
        self.blendWheel.setNotchTarget(12.699999999999999)
        self.blendWheel.setNotchesVisible(True)

        self.horizontalLayout.addWidget(self.blendWheel)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.driveWheel = QDial(self.widget)
        self.driveWheel.setObjectName(u"driveWheel")
        self.driveWheel.setMaximum(10000)
        self.driveWheel.setNotchTarget(12.699999999999999)
        self.driveWheel.setNotchesVisible(True)

        self.horizontalLayout.addWidget(self.driveWheel)

        self.widget1 = QWidget(self.tab_2)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(350, 67, 254, 102))
        self.horizontalLayout_2 = QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.rangeWheel = QDial(self.widget1)
        self.rangeWheel.setObjectName(u"rangeWheel")
        self.rangeWheel.setMaximum(3000)
        self.rangeWheel.setNotchTarget(12.699999999999999)
        self.rangeWheel.setNotchesVisible(True)

        self.horizontalLayout_2.addWidget(self.rangeWheel)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.volumeWheel = QDial(self.widget1)
        self.volumeWheel.setObjectName(u"volumeWheel")
        self.volumeWheel.setMaximum(300)
        self.volumeWheel.setNotchesVisible(True)

        self.horizontalLayout_2.addWidget(self.volumeWheel)

        self.widget2 = QWidget(self.tab_2)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(70, 170, 201, 22))
        self.horizontalLayout_3 = QHBoxLayout(self.widget2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.blendLabel = QLabel(self.widget2)
        self.blendLabel.setObjectName(u"blendLabel")
        self.blendLabel.setFont(font)

        self.horizontalLayout_3.addWidget(self.blendLabel)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.driveLabel = QLabel(self.widget2)
        self.driveLabel.setObjectName(u"driveLabel")
        self.driveLabel.setFont(font)

        self.horizontalLayout_3.addWidget(self.driveLabel)

        self.widget3 = QWidget(self.tab_2)
        self.widget3.setObjectName(u"widget3")
        self.widget3.setGeometry(QRect(380, 180, 191, 22))
        self.horizontalLayout_4 = QHBoxLayout(self.widget3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.rangLabel = QLabel(self.widget3)
        self.rangLabel.setObjectName(u"rangLabel")
        self.rangLabel.setFont(font)

        self.horizontalLayout_4.addWidget(self.rangLabel)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.volumeLabel = QLabel(self.widget3)
        self.volumeLabel.setObjectName(u"volumeLabel")
        self.volumeLabel.setFont(font)

        self.horizontalLayout_4.addWidget(self.volumeLabel)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tabWidget.addTab(self.tab_3, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 712, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.buttonGraph.setText(QCoreApplication.translate("MainWindow", u"Draw Graph", None))
        self.buttonPlay.setText(QCoreApplication.translate("MainWindow", u"Play a sound", None))
        self.buttonSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.labelFilePath.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043f\u0443\u0442\u044c \u043a \u0444\u0430\u0439\u043b\u0443:", None))
        self.pushButtonApplyFilter.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c \u0444\u0438\u043b\u044c\u0442\u0440", None))
        self.buttonStop.setText(QCoreApplication.translate("MainWindow", u"Stop Sound", None))
        self.toolButtonFilePath.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u041e\u0441\u043d\u043e\u0432\u043d\u043e\u0439", None))
        self.blendLabel.setText(QCoreApplication.translate("MainWindow", u"Blend", None))
        self.driveLabel.setText(QCoreApplication.translate("MainWindow", u"Drive", None))
        self.rangLabel.setText(QCoreApplication.translate("MainWindow", u"Range", None))
        self.volumeLabel.setText(QCoreApplication.translate("MainWindow", u"Volume", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Distortion", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Page", None))
    # retranslateUi

