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
        MainWindow.resize(710, 465)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.tabWidget = QTabWidget(self.frame)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 10, 671, 311))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.buttonGraphOriginal = QPushButton(self.tab)
        self.buttonGraphOriginal.setObjectName(u"buttonGraphOriginal")
        self.buttonGraphOriginal.setGeometry(QRect(500, 130, 151, 51))
        self.buttonSave = QPushButton(self.tab)
        self.buttonSave.setObjectName(u"buttonSave")
        self.buttonSave.setGeometry(QRect(270, 120, 191, 131))
        self.labelFilePath = QLabel(self.tab)
        self.labelFilePath.setObjectName(u"labelFilePath")
        self.labelFilePath.setGeometry(QRect(10, 70, 191, 31))
        font = QFont()
        font.setPointSize(11)
        self.labelFilePath.setFont(font)
        self.lineEditFilePath = QLineEdit(self.tab)
        self.lineEditFilePath.setObjectName(u"lineEditFilePath")
        self.lineEditFilePath.setGeometry(QRect(200, 70, 421, 31))
        self.buttonSelectFile = QToolButton(self.tab)
        self.buttonSelectFile.setObjectName(u"buttonSelectFile")
        self.buttonSelectFile.setGeometry(QRect(630, 76, 25, 19))
        self.buttonGraphFiltered = QPushButton(self.tab)
        self.buttonGraphFiltered.setObjectName(u"buttonGraphFiltered")
        self.buttonGraphFiltered.setGeometry(QRect(500, 190, 151, 51))
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.layoutWidget = QWidget(self.tab_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(40, 60, 254, 102))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.blendWheel = QDial(self.layoutWidget)
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

        self.driveWheel = QDial(self.layoutWidget)
        self.driveWheel.setObjectName(u"driveWheel")
        self.driveWheel.setMaximum(10000)
        self.driveWheel.setNotchTarget(12.699999999999999)
        self.driveWheel.setNotchesVisible(True)

        self.horizontalLayout.addWidget(self.driveWheel)

        self.layoutWidget1 = QWidget(self.tab_2)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(350, 60, 254, 102))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.rangeWheel = QDial(self.layoutWidget1)
        self.rangeWheel.setObjectName(u"rangeWheel")
        self.rangeWheel.setMaximum(3000)
        self.rangeWheel.setNotchTarget(12.699999999999999)
        self.rangeWheel.setNotchesVisible(True)

        self.horizontalLayout_2.addWidget(self.rangeWheel)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.volumeWheel = QDial(self.layoutWidget1)
        self.volumeWheel.setObjectName(u"volumeWheel")
        self.volumeWheel.setMaximum(300)
        self.volumeWheel.setNotchesVisible(True)

        self.horizontalLayout_2.addWidget(self.volumeWheel)

        self.layoutWidget2 = QWidget(self.tab_2)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(70, 170, 191, 25))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.blendLabel = QLabel(self.layoutWidget2)
        self.blendLabel.setObjectName(u"blendLabel")
        self.blendLabel.setFont(font)

        self.horizontalLayout_3.addWidget(self.blendLabel)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.driveLabel = QLabel(self.layoutWidget2)
        self.driveLabel.setObjectName(u"driveLabel")
        self.driveLabel.setFont(font)

        self.horizontalLayout_3.addWidget(self.driveLabel)

        self.layoutWidget3 = QWidget(self.tab_2)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(380, 170, 191, 24))
        self.horizontalLayout_4 = QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.rangLabel = QLabel(self.layoutWidget3)
        self.rangLabel.setObjectName(u"rangLabel")
        self.rangLabel.setFont(font)

        self.horizontalLayout_4.addWidget(self.rangLabel)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.volumeLabel = QLabel(self.layoutWidget3)
        self.volumeLabel.setObjectName(u"volumeLabel")
        self.volumeLabel.setFont(font)

        self.horizontalLayout_4.addWidget(self.volumeLabel)

        self.blendLabelValue = QLabel(self.tab_2)
        self.blendLabelValue.setObjectName(u"blendLabelValue")
        self.blendLabelValue.setGeometry(QRect(60, 30, 81, 21))
        self.blendLabelValue.setFont(font)
        self.driveLabelValue = QLabel(self.tab_2)
        self.driveLabelValue.setObjectName(u"driveLabelValue")
        self.driveLabelValue.setGeometry(QRect(220, 30, 81, 21))
        self.driveLabelValue.setFont(font)
        self.rangeLabelValue = QLabel(self.tab_2)
        self.rangeLabelValue.setObjectName(u"rangeLabelValue")
        self.rangeLabelValue.setGeometry(QRect(380, 30, 81, 21))
        self.rangeLabelValue.setFont(font)
        self.volumeLabelValue = QLabel(self.tab_2)
        self.volumeLabelValue.setObjectName(u"volumeLabelValue")
        self.volumeLabelValue.setGeometry(QRect(510, 30, 81, 21))
        self.volumeLabelValue.setFont(font)
        self.buttonFilterDistortion = QPushButton(self.tab_2)
        self.buttonFilterDistortion.setObjectName(u"buttonFilterDistortion")
        self.buttonFilterDistortion.setGeometry(QRect(370, 220, 151, 41))
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.buttonFilterEcho = QPushButton(self.tab_3)
        self.buttonFilterEcho.setObjectName(u"buttonFilterEcho")
        self.buttonFilterEcho.setGeometry(QRect(360, 200, 151, 51))
        self.delayTimeWheel = QDial(self.tab_3)
        self.delayTimeWheel.setObjectName(u"delayTimeWheel")
        self.delayTimeWheel.setGeometry(QRect(70, 60, 100, 100))
        self.delayTimeWheel.setMaximum(100)
        self.delayTimeWheel.setNotchesVisible(True)
        self.echoLevelWheel = QDial(self.tab_3)
        self.echoLevelWheel.setObjectName(u"echoLevelWheel")
        self.echoLevelWheel.setGeometry(QRect(250, 60, 100, 100))
        self.echoLevelWheel.setMaximum(100)
        self.echoLevelWheel.setNotchesVisible(True)
        self.blurIntervalWheel = QDial(self.tab_3)
        self.blurIntervalWheel.setObjectName(u"blurIntervalWheel")
        self.blurIntervalWheel.setGeometry(QRect(430, 60, 100, 100))
        self.blurIntervalWheel.setMaximum(20)
        self.blurIntervalWheel.setNotchesVisible(True)
        self.echoLevelLabelValue = QLabel(self.tab_3)
        self.echoLevelLabelValue.setObjectName(u"echoLevelLabelValue")
        self.echoLevelLabelValue.setGeometry(QRect(260, 30, 81, 21))
        self.echoLevelLabelValue.setFont(font)
        self.delayTimeLabelValue = QLabel(self.tab_3)
        self.delayTimeLabelValue.setObjectName(u"delayTimeLabelValue")
        self.delayTimeLabelValue.setGeometry(QRect(60, 30, 81, 21))
        self.delayTimeLabelValue.setFont(font)
        self.blurIntervalLabelValue = QLabel(self.tab_3)
        self.blurIntervalLabelValue.setObjectName(u"blurIntervalLabelValue")
        self.blurIntervalLabelValue.setGeometry(QRect(420, 30, 81, 21))
        self.blurIntervalLabelValue.setFont(font)
        self.delayTimeLabel = QLabel(self.tab_3)
        self.delayTimeLabel.setObjectName(u"delayTimeLabel")
        self.delayTimeLabel.setGeometry(QRect(80, 170, 101, 20))
        self.delayTimeLabel.setFont(font)
        self.echoLevelLabel = QLabel(self.tab_3)
        self.echoLevelLabel.setObjectName(u"echoLevelLabel")
        self.echoLevelLabel.setGeometry(QRect(260, 170, 101, 20))
        self.echoLevelLabel.setFont(font)
        self.blurIntervalLabel = QLabel(self.tab_3)
        self.blurIntervalLabel.setObjectName(u"blurIntervalLabel")
        self.blurIntervalLabel.setGeometry(QRect(430, 170, 101, 20))
        self.blurIntervalLabel.setFont(font)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.buttonFilterRemovingClicksAndPops = QPushButton(self.tab_4)
        self.buttonFilterRemovingClicksAndPops.setObjectName(u"buttonFilterRemovingClicksAndPops")
        self.buttonFilterRemovingClicksAndPops.setGeometry(QRect(430, 220, 131, 41))
        self.sensitivityWheel = QDial(self.tab_4)
        self.sensitivityWheel.setObjectName(u"sensitivityWheel")
        self.sensitivityWheel.setGeometry(QRect(80, 60, 100, 100))
        self.sensitivityWheel.setMaximum(35)
        self.sensitivityWheel.setSingleStep(1)
        self.sensitivityWheel.setPageStep(7)
        self.sensitivityWheel.setOrientation(Qt.Horizontal)
        self.sensitivityWheel.setNotchTarget(3.000000000000000)
        self.sensitivityWheel.setNotchesVisible(True)
        self.mutePowerLabelValue = QLabel(self.tab_4)
        self.mutePowerLabelValue.setObjectName(u"mutePowerLabelValue")
        self.mutePowerLabelValue.setGeometry(QRect(400, 30, 81, 21))
        self.mutePowerLabelValue.setFont(font)
        self.mutePowerWheel = QDial(self.tab_4)
        self.mutePowerWheel.setObjectName(u"mutePowerWheel")
        self.mutePowerWheel.setGeometry(QRect(410, 60, 100, 100))
        self.mutePowerWheel.setMinimum(2)
        self.mutePowerWheel.setMaximum(100)
        self.mutePowerWheel.setSingleStep(1)
        self.mutePowerWheel.setPageStep(10)
        self.mutePowerWheel.setOrientation(Qt.Horizontal)
        self.mutePowerWheel.setNotchTarget(2.000000000000000)
        self.mutePowerWheel.setNotchesVisible(True)
        self.sensitivityLabel = QLabel(self.tab_4)
        self.sensitivityLabel.setObjectName(u"sensitivityLabel")
        self.sensitivityLabel.setGeometry(QRect(90, 170, 101, 20))
        self.sensitivityLabel.setFont(font)
        self.sensitivityLabelValue = QLabel(self.tab_4)
        self.sensitivityLabelValue.setObjectName(u"sensitivityLabelValue")
        self.sensitivityLabelValue.setGeometry(QRect(70, 30, 81, 21))
        self.sensitivityLabelValue.setFont(font)
        self.fadeLengthWheel = QDial(self.tab_4)
        self.fadeLengthWheel.setObjectName(u"fadeLengthWheel")
        self.fadeLengthWheel.setGeometry(QRect(240, 60, 100, 100))
        self.fadeLengthWheel.setMaximum(1000)
        self.fadeLengthWheel.setSingleStep(1)
        self.fadeLengthWheel.setPageStep(100)
        self.fadeLengthWheel.setOrientation(Qt.Horizontal)
        self.fadeLengthWheel.setNotchTarget(10.000000000000000)
        self.fadeLengthWheel.setNotchesVisible(True)
        self.fadeLengthLabelValue = QLabel(self.tab_4)
        self.fadeLengthLabelValue.setObjectName(u"fadeLengthLabelValue")
        self.fadeLengthLabelValue.setGeometry(QRect(230, 30, 81, 21))
        self.fadeLengthLabelValue.setFont(font)
        self.fadeLengtLabel = QLabel(self.tab_4)
        self.fadeLengtLabel.setObjectName(u"fadeLengtLabel")
        self.fadeLengtLabel.setGeometry(QRect(250, 170, 101, 20))
        self.fadeLengtLabel.setFont(font)
        self.mutePowerLabel = QLabel(self.tab_4)
        self.mutePowerLabel.setObjectName(u"mutePowerLabel")
        self.mutePowerLabel.setGeometry(QRect(420, 170, 101, 20))
        self.mutePowerLabel.setFont(font)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.timeSlider = QSlider(self.tab_5)
        self.timeSlider.setObjectName(u"timeSlider")
        self.timeSlider.setGeometry(QRect(80, 100, 511, 31))
        self.timeSlider.setMaximum(300)
        self.timeSlider.setSingleStep(1)
        self.timeSlider.setPageStep(30)
        self.timeSlider.setOrientation(Qt.Horizontal)
        self.timeSlider.setTickPosition(QSlider.TicksAbove)
        self.buttonFilterTime = QPushButton(self.tab_5)
        self.buttonFilterTime.setObjectName(u"buttonFilterTime")
        self.buttonFilterTime.setGeometry(QRect(270, 190, 131, 41))
        self.timeLabelValue = QLabel(self.tab_5)
        self.timeLabelValue.setObjectName(u"timeLabelValue")
        self.timeLabelValue.setGeometry(QRect(320, 60, 71, 21))
        self.timeLabelValue.setFont(font)
        self.timeLabelValue.setTextFormat(Qt.AutoText)
        self.tabWidget.addTab(self.tab_5, "")
        self.buttonPlayFilteredSound = QPushButton(self.frame)
        self.buttonPlayFilteredSound.setObjectName(u"buttonPlayFilteredSound")
        self.buttonPlayFilteredSound.setGeometry(QRect(290, 340, 111, 51))
        self.buttonPlayFilteredSound.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.buttonPlayOriginalSound = QPushButton(self.frame)
        self.buttonPlayOriginalSound.setObjectName(u"buttonPlayOriginalSound")
        self.buttonPlayOriginalSound.setGeometry(QRect(170, 340, 111, 51))
        self.buttonPlayOriginalSound.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.buttonStop = QPushButton(self.frame)
        self.buttonStop.setObjectName(u"buttonStop")
        self.buttonStop.setGeometry(QRect(410, 340, 101, 51))

        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 710, 21))
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
        self.buttonGraphOriginal.setText(QCoreApplication.translate("MainWindow", u"Draw graph original", None))
        self.buttonSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.labelFilePath.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043f\u0443\u0442\u044c \u043a \u0444\u0430\u0439\u043b\u0443:", None))
        self.buttonSelectFile.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.buttonGraphFiltered.setText(QCoreApplication.translate("MainWindow", u"Draw graph filtered", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u041e\u0441\u043d\u043e\u0432\u043d\u043e\u0439", None))
        self.blendLabel.setText(QCoreApplication.translate("MainWindow", u"Blend", None))
        self.driveLabel.setText(QCoreApplication.translate("MainWindow", u"Drive", None))
        self.rangLabel.setText(QCoreApplication.translate("MainWindow", u"Range", None))
        self.volumeLabel.setText(QCoreApplication.translate("MainWindow", u"Volume", None))
        self.blendLabelValue.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.driveLabelValue.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.rangeLabelValue.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.volumeLabelValue.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.buttonFilterDistortion.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c \u0444\u0438\u043b\u044c\u0442\u0440", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Distortion", None))
        self.buttonFilterEcho.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c \u0444\u0438\u043b\u044c\u0442\u0440", None))
        self.echoLevelLabelValue.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.delayTimeLabelValue.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.blurIntervalLabelValue.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.delayTimeLabel.setText(QCoreApplication.translate("MainWindow", u"Delay time", None))
        self.echoLevelLabel.setText(QCoreApplication.translate("MainWindow", u"Echo level", None))
        self.blurIntervalLabel.setText(QCoreApplication.translate("MainWindow", u"Blur interval", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Echo", None))
        self.buttonFilterRemovingClicksAndPops.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c \u0444\u0438\u043b\u044c\u0442\u0440", None))
        self.mutePowerLabelValue.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.sensitivityLabel.setText(QCoreApplication.translate("MainWindow", u"Sensitivity", None))
        self.sensitivityLabelValue.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.fadeLengthLabelValue.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.fadeLengtLabel.setText(QCoreApplication.translate("MainWindow", u"Fade Length", None))
        self.mutePowerLabel.setText(QCoreApplication.translate("MainWindow", u"Mute Power", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Removing Clicks and Pops", None))
        self.buttonFilterTime.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c \u0444\u0438\u043b\u044c\u0442\u0440", None))
        self.timeLabelValue.setText(QCoreApplication.translate("MainWindow", u"100%", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"Time", None))
        self.buttonPlayFilteredSound.setText(QCoreApplication.translate("MainWindow", u"Play filtered", None))
        self.buttonPlayOriginalSound.setText(QCoreApplication.translate("MainWindow", u"Play original", None))
        self.buttonStop.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
    # retranslateUi

