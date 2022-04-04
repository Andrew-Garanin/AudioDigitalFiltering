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
        MainWindow.resize(982, 429)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        MainWindow.setBaseSize(QSize(979, 423))
        icon = QIcon()
        icon.addFile(u":/icons/music-icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setSpacing(1)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_2.setContentsMargins(1, 1, 1, 1)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setLineWidth(1)
        self.tabWidget = QTabWidget(self.frame)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(300, 70, 671, 311))
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_6 = QGridLayout(self.tab_2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.blendLabel = QLabel(self.tab_2)
        self.blendLabel.setObjectName(u"blendLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.blendLabel.sizePolicy().hasHeightForWidth())
        self.blendLabel.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(11)
        self.blendLabel.setFont(font)
        self.blendLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.blendLabel, 2, 0, 1, 1)

        self.volumeWheel = QDial(self.tab_2)
        self.volumeWheel.setObjectName(u"volumeWheel")
        sizePolicy1.setHeightForWidth(self.volumeWheel.sizePolicy().hasHeightForWidth())
        self.volumeWheel.setSizePolicy(sizePolicy1)
        self.volumeWheel.setMaximum(300)
        self.volumeWheel.setNotchesVisible(True)

        self.gridLayout_3.addWidget(self.volumeWheel, 1, 3, 1, 1)

        self.blendLabelValue = QLabel(self.tab_2)
        self.blendLabelValue.setObjectName(u"blendLabelValue")
        sizePolicy1.setHeightForWidth(self.blendLabelValue.sizePolicy().hasHeightForWidth())
        self.blendLabelValue.setSizePolicy(sizePolicy1)
        self.blendLabelValue.setFont(font)
        self.blendLabelValue.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.blendLabelValue, 0, 0, 1, 1)

        self.rangLabel = QLabel(self.tab_2)
        self.rangLabel.setObjectName(u"rangLabel")
        sizePolicy1.setHeightForWidth(self.rangLabel.sizePolicy().hasHeightForWidth())
        self.rangLabel.setSizePolicy(sizePolicy1)
        self.rangLabel.setFont(font)
        self.rangLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.rangLabel, 2, 2, 1, 1)

        self.volumeLabel = QLabel(self.tab_2)
        self.volumeLabel.setObjectName(u"volumeLabel")
        sizePolicy1.setHeightForWidth(self.volumeLabel.sizePolicy().hasHeightForWidth())
        self.volumeLabel.setSizePolicy(sizePolicy1)
        self.volumeLabel.setFont(font)
        self.volumeLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.volumeLabel, 2, 3, 1, 1)

        self.driveLabel = QLabel(self.tab_2)
        self.driveLabel.setObjectName(u"driveLabel")
        sizePolicy1.setHeightForWidth(self.driveLabel.sizePolicy().hasHeightForWidth())
        self.driveLabel.setSizePolicy(sizePolicy1)
        self.driveLabel.setFont(font)
        self.driveLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.driveLabel, 2, 1, 1, 1)

        self.driveWheel = QDial(self.tab_2)
        self.driveWheel.setObjectName(u"driveWheel")
        sizePolicy1.setHeightForWidth(self.driveWheel.sizePolicy().hasHeightForWidth())
        self.driveWheel.setSizePolicy(sizePolicy1)
        self.driveWheel.setMaximum(10000)
        self.driveWheel.setNotchTarget(12.699999999999999)
        self.driveWheel.setNotchesVisible(True)

        self.gridLayout_3.addWidget(self.driveWheel, 1, 1, 1, 1)

        self.volumeLabelValue = QLabel(self.tab_2)
        self.volumeLabelValue.setObjectName(u"volumeLabelValue")
        sizePolicy1.setHeightForWidth(self.volumeLabelValue.sizePolicy().hasHeightForWidth())
        self.volumeLabelValue.setSizePolicy(sizePolicy1)
        self.volumeLabelValue.setFont(font)
        self.volumeLabelValue.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.volumeLabelValue, 0, 3, 1, 1)

        self.blendWheel = QDial(self.tab_2)
        self.blendWheel.setObjectName(u"blendWheel")
        sizePolicy1.setHeightForWidth(self.blendWheel.sizePolicy().hasHeightForWidth())
        self.blendWheel.setSizePolicy(sizePolicy1)
        self.blendWheel.setMaximum(10000)
        self.blendWheel.setSingleStep(1)
        self.blendWheel.setPageStep(10)
        self.blendWheel.setWrapping(False)
        self.blendWheel.setNotchTarget(12.699999999999999)
        self.blendWheel.setNotchesVisible(True)

        self.gridLayout_3.addWidget(self.blendWheel, 1, 0, 1, 1)

        self.driveLabelValue = QLabel(self.tab_2)
        self.driveLabelValue.setObjectName(u"driveLabelValue")
        sizePolicy1.setHeightForWidth(self.driveLabelValue.sizePolicy().hasHeightForWidth())
        self.driveLabelValue.setSizePolicy(sizePolicy1)
        self.driveLabelValue.setFont(font)
        self.driveLabelValue.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.driveLabelValue, 0, 1, 1, 1)

        self.rangeLabelValue = QLabel(self.tab_2)
        self.rangeLabelValue.setObjectName(u"rangeLabelValue")
        sizePolicy1.setHeightForWidth(self.rangeLabelValue.sizePolicy().hasHeightForWidth())
        self.rangeLabelValue.setSizePolicy(sizePolicy1)
        self.rangeLabelValue.setFont(font)
        self.rangeLabelValue.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.rangeLabelValue, 0, 2, 1, 1)

        self.rangeWheel = QDial(self.tab_2)
        self.rangeWheel.setObjectName(u"rangeWheel")
        sizePolicy1.setHeightForWidth(self.rangeWheel.sizePolicy().hasHeightForWidth())
        self.rangeWheel.setSizePolicy(sizePolicy1)
        self.rangeWheel.setMaximum(500)
        self.rangeWheel.setPageStep(100)
        self.rangeWheel.setNotchTarget(9.699999999999999)
        self.rangeWheel.setNotchesVisible(True)

        self.gridLayout_3.addWidget(self.rangeWheel, 1, 2, 1, 1)

        self.buttonFilterDistortion = QPushButton(self.tab_2)
        self.buttonFilterDistortion.setObjectName(u"buttonFilterDistortion")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/music-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonFilterDistortion.setIcon(icon1)
        self.buttonFilterDistortion.setIconSize(QSize(25, 25))

        self.gridLayout_3.addWidget(self.buttonFilterDistortion, 3, 1, 1, 2)


        self.gridLayout_6.addLayout(self.gridLayout_3, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_7 = QGridLayout(self.tab_3)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.echoLevelLabelValue = QLabel(self.tab_3)
        self.echoLevelLabelValue.setObjectName(u"echoLevelLabelValue")
        self.echoLevelLabelValue.setFont(font)
        self.echoLevelLabelValue.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.echoLevelLabelValue, 0, 1, 1, 1)

        self.delayTimeLabelValue = QLabel(self.tab_3)
        self.delayTimeLabelValue.setObjectName(u"delayTimeLabelValue")
        self.delayTimeLabelValue.setFont(font)
        self.delayTimeLabelValue.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.delayTimeLabelValue, 0, 0, 1, 1)

        self.blurIntervalLabel = QLabel(self.tab_3)
        self.blurIntervalLabel.setObjectName(u"blurIntervalLabel")
        self.blurIntervalLabel.setFont(font)
        self.blurIntervalLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.blurIntervalLabel, 2, 2, 1, 1)

        self.blurIntervalLabelValue = QLabel(self.tab_3)
        self.blurIntervalLabelValue.setObjectName(u"blurIntervalLabelValue")
        self.blurIntervalLabelValue.setFont(font)
        self.blurIntervalLabelValue.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.blurIntervalLabelValue, 0, 2, 1, 1)

        self.delayTimeLabel = QLabel(self.tab_3)
        self.delayTimeLabel.setObjectName(u"delayTimeLabel")
        self.delayTimeLabel.setFont(font)
        self.delayTimeLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.delayTimeLabel, 2, 0, 1, 1)

        self.blurIntervalWheel = QDial(self.tab_3)
        self.blurIntervalWheel.setObjectName(u"blurIntervalWheel")
        self.blurIntervalWheel.setMaximum(40)
        self.blurIntervalWheel.setNotchesVisible(True)

        self.gridLayout_4.addWidget(self.blurIntervalWheel, 1, 2, 1, 1)

        self.echoLevelLabel = QLabel(self.tab_3)
        self.echoLevelLabel.setObjectName(u"echoLevelLabel")
        self.echoLevelLabel.setFont(font)
        self.echoLevelLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.echoLevelLabel, 2, 1, 1, 1)

        self.delayTimeWheel = QDial(self.tab_3)
        self.delayTimeWheel.setObjectName(u"delayTimeWheel")
        self.delayTimeWheel.setMaximum(100)
        self.delayTimeWheel.setNotchesVisible(True)

        self.gridLayout_4.addWidget(self.delayTimeWheel, 1, 0, 1, 1)

        self.echoLevelWheel = QDial(self.tab_3)
        self.echoLevelWheel.setObjectName(u"echoLevelWheel")
        self.echoLevelWheel.setMaximum(100)
        self.echoLevelWheel.setNotchesVisible(True)

        self.gridLayout_4.addWidget(self.echoLevelWheel, 1, 1, 1, 1)

        self.buttonFilterEcho = QPushButton(self.tab_3)
        self.buttonFilterEcho.setObjectName(u"buttonFilterEcho")
        self.buttonFilterEcho.setIcon(icon1)
        self.buttonFilterEcho.setIconSize(QSize(25, 25))

        self.gridLayout_4.addWidget(self.buttonFilterEcho, 3, 1, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout_4, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayout_8 = QGridLayout(self.tab_4)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.sensitivityLabel = QLabel(self.tab_4)
        self.sensitivityLabel.setObjectName(u"sensitivityLabel")
        self.sensitivityLabel.setFont(font)
        self.sensitivityLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.sensitivityLabel, 2, 0, 1, 1)

        self.mutePowerLabel = QLabel(self.tab_4)
        self.mutePowerLabel.setObjectName(u"mutePowerLabel")
        self.mutePowerLabel.setFont(font)
        self.mutePowerLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.mutePowerLabel, 2, 2, 1, 1)

        self.mutePowerLabelValue = QLabel(self.tab_4)
        self.mutePowerLabelValue.setObjectName(u"mutePowerLabelValue")
        self.mutePowerLabelValue.setFont(font)
        self.mutePowerLabelValue.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.mutePowerLabelValue, 0, 2, 1, 1)

        self.fadeLengthLabelValue = QLabel(self.tab_4)
        self.fadeLengthLabelValue.setObjectName(u"fadeLengthLabelValue")
        self.fadeLengthLabelValue.setFont(font)
        self.fadeLengthLabelValue.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.fadeLengthLabelValue, 0, 1, 1, 1)

        self.sensitivityWheel = QDial(self.tab_4)
        self.sensitivityWheel.setObjectName(u"sensitivityWheel")
        self.sensitivityWheel.setMaximum(35)
        self.sensitivityWheel.setSingleStep(1)
        self.sensitivityWheel.setPageStep(7)
        self.sensitivityWheel.setOrientation(Qt.Horizontal)
        self.sensitivityWheel.setNotchTarget(3.000000000000000)
        self.sensitivityWheel.setNotchesVisible(True)

        self.gridLayout_5.addWidget(self.sensitivityWheel, 1, 0, 1, 1)

        self.fadeLengtLabel = QLabel(self.tab_4)
        self.fadeLengtLabel.setObjectName(u"fadeLengtLabel")
        self.fadeLengtLabel.setFont(font)
        self.fadeLengtLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.fadeLengtLabel, 2, 1, 1, 1)

        self.fadeLengthWheel = QDial(self.tab_4)
        self.fadeLengthWheel.setObjectName(u"fadeLengthWheel")
        self.fadeLengthWheel.setMaximum(1000)
        self.fadeLengthWheel.setSingleStep(1)
        self.fadeLengthWheel.setPageStep(100)
        self.fadeLengthWheel.setOrientation(Qt.Horizontal)
        self.fadeLengthWheel.setNotchTarget(10.000000000000000)
        self.fadeLengthWheel.setNotchesVisible(True)

        self.gridLayout_5.addWidget(self.fadeLengthWheel, 1, 1, 1, 1)

        self.sensitivityLabelValue = QLabel(self.tab_4)
        self.sensitivityLabelValue.setObjectName(u"sensitivityLabelValue")
        self.sensitivityLabelValue.setFont(font)
        self.sensitivityLabelValue.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.sensitivityLabelValue, 0, 0, 1, 1)

        self.mutePowerWheel = QDial(self.tab_4)
        self.mutePowerWheel.setObjectName(u"mutePowerWheel")
        self.mutePowerWheel.setMinimum(2)
        self.mutePowerWheel.setMaximum(100)
        self.mutePowerWheel.setSingleStep(1)
        self.mutePowerWheel.setPageStep(10)
        self.mutePowerWheel.setOrientation(Qt.Horizontal)
        self.mutePowerWheel.setNotchTarget(2.000000000000000)
        self.mutePowerWheel.setNotchesVisible(True)

        self.gridLayout_5.addWidget(self.mutePowerWheel, 1, 2, 1, 1)

        self.buttonFilterRemovingClicksAndPops = QPushButton(self.tab_4)
        self.buttonFilterRemovingClicksAndPops.setObjectName(u"buttonFilterRemovingClicksAndPops")
        self.buttonFilterRemovingClicksAndPops.setIcon(icon1)
        self.buttonFilterRemovingClicksAndPops.setIconSize(QSize(25, 25))

        self.gridLayout_5.addWidget(self.buttonFilterRemovingClicksAndPops, 3, 1, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_5, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.gridLayout_11 = QGridLayout(self.tab_5)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.buttonFilterTime = QPushButton(self.tab_5)
        self.buttonFilterTime.setObjectName(u"buttonFilterTime")
        self.buttonFilterTime.setIcon(icon1)
        self.buttonFilterTime.setIconSize(QSize(25, 25))

        self.gridLayout_10.addWidget(self.buttonFilterTime, 3, 0, 1, 1)

        self.timeSlider = QSlider(self.tab_5)
        self.timeSlider.setObjectName(u"timeSlider")
        self.timeSlider.setMaximum(300)
        self.timeSlider.setSingleStep(1)
        self.timeSlider.setPageStep(30)
        self.timeSlider.setOrientation(Qt.Horizontal)
        self.timeSlider.setTickPosition(QSlider.TicksAbove)

        self.gridLayout_10.addWidget(self.timeSlider, 2, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.timeLabelValue = QLabel(self.tab_5)
        self.timeLabelValue.setObjectName(u"timeLabelValue")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.timeLabelValue.sizePolicy().hasHeightForWidth())
        self.timeLabelValue.setSizePolicy(sizePolicy2)
        self.timeLabelValue.setFont(font)
        self.timeLabelValue.setTextFormat(Qt.AutoText)

        self.horizontalLayout_2.addWidget(self.timeLabelValue)


        self.gridLayout_10.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)


        self.gridLayout_11.addLayout(self.gridLayout_10, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_5, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_9 = QGridLayout(self.tab)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(6)
        self.aggressionWheel = QDial(self.tab)
        self.aggressionWheel.setObjectName(u"aggressionWheel")
        sizePolicy1.setHeightForWidth(self.aggressionWheel.sizePolicy().hasHeightForWidth())
        self.aggressionWheel.setSizePolicy(sizePolicy1)
        self.aggressionWheel.setMaximum(100)
        self.aggressionWheel.setSingleStep(1)
        self.aggressionWheel.setPageStep(5)
        self.aggressionWheel.setOrientation(Qt.Horizontal)
        self.aggressionWheel.setNotchTarget(10.000000000000000)
        self.aggressionWheel.setNotchesVisible(True)

        self.gridLayout.addWidget(self.aggressionWheel, 1, 2, 1, 1)

        self.offsetSamplesLabel = QLabel(self.tab)
        self.offsetSamplesLabel.setObjectName(u"offsetSamplesLabel")
        self.offsetSamplesLabel.setFont(font)
        self.offsetSamplesLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.offsetSamplesLabel, 2, 0, 1, 1)

        self.offsetSamplesWheel = QDial(self.tab)
        self.offsetSamplesWheel.setObjectName(u"offsetSamplesWheel")
        sizePolicy1.setHeightForWidth(self.offsetSamplesWheel.sizePolicy().hasHeightForWidth())
        self.offsetSamplesWheel.setSizePolicy(sizePolicy1)
        self.offsetSamplesWheel.setMaximum(400)
        self.offsetSamplesWheel.setSingleStep(1)
        self.offsetSamplesWheel.setPageStep(16)
        self.offsetSamplesWheel.setOrientation(Qt.Horizontal)
        self.offsetSamplesWheel.setNotchTarget(10.000000000000000)
        self.offsetSamplesWheel.setNotchesVisible(True)

        self.gridLayout.addWidget(self.offsetSamplesWheel, 1, 0, 1, 1)

        self.aggressionLabelValue = QLabel(self.tab)
        self.aggressionLabelValue.setObjectName(u"aggressionLabelValue")
        sizePolicy1.setHeightForWidth(self.aggressionLabelValue.sizePolicy().hasHeightForWidth())
        self.aggressionLabelValue.setSizePolicy(sizePolicy1)
        self.aggressionLabelValue.setFont(font)
        self.aggressionLabelValue.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.aggressionLabelValue, 0, 2, 1, 1)

        self.offsetSamplesLabelValue = QLabel(self.tab)
        self.offsetSamplesLabelValue.setObjectName(u"offsetSamplesLabelValue")
        sizePolicy.setHeightForWidth(self.offsetSamplesLabelValue.sizePolicy().hasHeightForWidth())
        self.offsetSamplesLabelValue.setSizePolicy(sizePolicy)
        self.offsetSamplesLabelValue.setFont(font)
        self.offsetSamplesLabelValue.setFocusPolicy(Qt.NoFocus)
        self.offsetSamplesLabelValue.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.offsetSamplesLabelValue, 0, 0, 1, 1)

        self.aggressionLabel = QLabel(self.tab)
        self.aggressionLabel.setObjectName(u"aggressionLabel")
        self.aggressionLabel.setFont(font)
        self.aggressionLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.aggressionLabel, 2, 2, 1, 1)

        self.buttonFilterRemoveSilence = QPushButton(self.tab)
        self.buttonFilterRemoveSilence.setObjectName(u"buttonFilterRemoveSilence")
        self.buttonFilterRemoveSilence.setIcon(icon1)
        self.buttonFilterRemoveSilence.setIconSize(QSize(25, 25))

        self.gridLayout.addWidget(self.buttonFilterRemoveSilence, 3, 1, 1, 1)


        self.gridLayout_9.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.gridLayout_13 = QGridLayout(self.tab_6)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_12 = QGridLayout()
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setHorizontalSpacing(6)
        self.leftFadeStrenghtLabel = QLabel(self.tab_6)
        self.leftFadeStrenghtLabel.setObjectName(u"leftFadeStrenghtLabel")
        self.leftFadeStrenghtLabel.setFont(font)
        self.leftFadeStrenghtLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_12.addWidget(self.leftFadeStrenghtLabel, 2, 1, 1, 1)

        self.leftFadeStrenghtWheel = QDial(self.tab_6)
        self.leftFadeStrenghtWheel.setObjectName(u"leftFadeStrenghtWheel")
        sizePolicy1.setHeightForWidth(self.leftFadeStrenghtWheel.sizePolicy().hasHeightForWidth())
        self.leftFadeStrenghtWheel.setSizePolicy(sizePolicy1)
        self.leftFadeStrenghtWheel.setMinimum(1)
        self.leftFadeStrenghtWheel.setMaximum(5)
        self.leftFadeStrenghtWheel.setSingleStep(1)
        self.leftFadeStrenghtWheel.setPageStep(1)
        self.leftFadeStrenghtWheel.setOrientation(Qt.Horizontal)
        self.leftFadeStrenghtWheel.setNotchTarget(10.000000000000000)
        self.leftFadeStrenghtWheel.setNotchesVisible(True)

        self.gridLayout_12.addWidget(self.leftFadeStrenghtWheel, 1, 1, 1, 1)

        self.rightFadeLengthWheel = QDial(self.tab_6)
        self.rightFadeLengthWheel.setObjectName(u"rightFadeLengthWheel")
        sizePolicy1.setHeightForWidth(self.rightFadeLengthWheel.sizePolicy().hasHeightForWidth())
        self.rightFadeLengthWheel.setSizePolicy(sizePolicy1)
        self.rightFadeLengthWheel.setMaximum(100)
        self.rightFadeLengthWheel.setSingleStep(1)
        self.rightFadeLengthWheel.setPageStep(10)
        self.rightFadeLengthWheel.setOrientation(Qt.Horizontal)
        self.rightFadeLengthWheel.setNotchTarget(5.000000000000000)
        self.rightFadeLengthWheel.setNotchesVisible(True)

        self.gridLayout_12.addWidget(self.rightFadeLengthWheel, 1, 2, 1, 1)

        self.leftFadeStrenghtLabelValue = QLabel(self.tab_6)
        self.leftFadeStrenghtLabelValue.setObjectName(u"leftFadeStrenghtLabelValue")
        sizePolicy.setHeightForWidth(self.leftFadeStrenghtLabelValue.sizePolicy().hasHeightForWidth())
        self.leftFadeStrenghtLabelValue.setSizePolicy(sizePolicy)
        self.leftFadeStrenghtLabelValue.setFont(font)
        self.leftFadeStrenghtLabelValue.setFocusPolicy(Qt.NoFocus)
        self.leftFadeStrenghtLabelValue.setAlignment(Qt.AlignCenter)

        self.gridLayout_12.addWidget(self.leftFadeStrenghtLabelValue, 0, 1, 1, 1)

        self.leftFadeLengthLable = QLabel(self.tab_6)
        self.leftFadeLengthLable.setObjectName(u"leftFadeLengthLable")
        self.leftFadeLengthLable.setFont(font)
        self.leftFadeLengthLable.setAlignment(Qt.AlignCenter)

        self.gridLayout_12.addWidget(self.leftFadeLengthLable, 2, 0, 1, 1)

        self.leftFadeLengthWheel = QDial(self.tab_6)
        self.leftFadeLengthWheel.setObjectName(u"leftFadeLengthWheel")
        sizePolicy1.setHeightForWidth(self.leftFadeLengthWheel.sizePolicy().hasHeightForWidth())
        self.leftFadeLengthWheel.setSizePolicy(sizePolicy1)
        self.leftFadeLengthWheel.setMaximum(100)
        self.leftFadeLengthWheel.setSingleStep(1)
        self.leftFadeLengthWheel.setPageStep(20)
        self.leftFadeLengthWheel.setOrientation(Qt.Horizontal)
        self.leftFadeLengthWheel.setNotchTarget(5.000000000000000)
        self.leftFadeLengthWheel.setNotchesVisible(True)

        self.gridLayout_12.addWidget(self.leftFadeLengthWheel, 1, 0, 1, 1)

        self.leftFadeLengthLableValue = QLabel(self.tab_6)
        self.leftFadeLengthLableValue.setObjectName(u"leftFadeLengthLableValue")
        sizePolicy.setHeightForWidth(self.leftFadeLengthLableValue.sizePolicy().hasHeightForWidth())
        self.leftFadeLengthLableValue.setSizePolicy(sizePolicy)
        self.leftFadeLengthLableValue.setFont(font)
        self.leftFadeLengthLableValue.setFocusPolicy(Qt.NoFocus)
        self.leftFadeLengthLableValue.setAlignment(Qt.AlignCenter)

        self.gridLayout_12.addWidget(self.leftFadeLengthLableValue, 0, 0, 1, 1)

        self.rightFadeLengthLable = QLabel(self.tab_6)
        self.rightFadeLengthLable.setObjectName(u"rightFadeLengthLable")
        self.rightFadeLengthLable.setFont(font)
        self.rightFadeLengthLable.setAlignment(Qt.AlignCenter)

        self.gridLayout_12.addWidget(self.rightFadeLengthLable, 2, 2, 1, 1)

        self.rightFadeLengthLableValue = QLabel(self.tab_6)
        self.rightFadeLengthLableValue.setObjectName(u"rightFadeLengthLableValue")
        sizePolicy1.setHeightForWidth(self.rightFadeLengthLableValue.sizePolicy().hasHeightForWidth())
        self.rightFadeLengthLableValue.setSizePolicy(sizePolicy1)
        self.rightFadeLengthLableValue.setFont(font)
        self.rightFadeLengthLableValue.setAlignment(Qt.AlignCenter)

        self.gridLayout_12.addWidget(self.rightFadeLengthLableValue, 0, 2, 1, 1)

        self.rightFadeStrenghtLabel = QLabel(self.tab_6)
        self.rightFadeStrenghtLabel.setObjectName(u"rightFadeStrenghtLabel")
        self.rightFadeStrenghtLabel.setFont(font)
        self.rightFadeStrenghtLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_12.addWidget(self.rightFadeStrenghtLabel, 2, 3, 1, 1)

        self.rightFadeStrenghtWheel = QDial(self.tab_6)
        self.rightFadeStrenghtWheel.setObjectName(u"rightFadeStrenghtWheel")
        sizePolicy1.setHeightForWidth(self.rightFadeStrenghtWheel.sizePolicy().hasHeightForWidth())
        self.rightFadeStrenghtWheel.setSizePolicy(sizePolicy1)
        self.rightFadeStrenghtWheel.setMinimum(1)
        self.rightFadeStrenghtWheel.setMaximum(5)
        self.rightFadeStrenghtWheel.setSingleStep(1)
        self.rightFadeStrenghtWheel.setPageStep(1)
        self.rightFadeStrenghtWheel.setOrientation(Qt.Horizontal)
        self.rightFadeStrenghtWheel.setNotchTarget(10.000000000000000)
        self.rightFadeStrenghtWheel.setNotchesVisible(True)

        self.gridLayout_12.addWidget(self.rightFadeStrenghtWheel, 1, 3, 1, 1)

        self.rightFadeStrenghtLabelValue = QLabel(self.tab_6)
        self.rightFadeStrenghtLabelValue.setObjectName(u"rightFadeStrenghtLabelValue")
        sizePolicy1.setHeightForWidth(self.rightFadeStrenghtLabelValue.sizePolicy().hasHeightForWidth())
        self.rightFadeStrenghtLabelValue.setSizePolicy(sizePolicy1)
        self.rightFadeStrenghtLabelValue.setFont(font)
        self.rightFadeStrenghtLabelValue.setAlignment(Qt.AlignCenter)

        self.gridLayout_12.addWidget(self.rightFadeStrenghtLabelValue, 0, 3, 1, 1)

        self.buttonFilterFade = QPushButton(self.tab_6)
        self.buttonFilterFade.setObjectName(u"buttonFilterFade")
        self.buttonFilterFade.setIcon(icon1)
        self.buttonFilterFade.setIconSize(QSize(25, 25))

        self.gridLayout_12.addWidget(self.buttonFilterFade, 3, 1, 1, 2)


        self.gridLayout_13.addLayout(self.gridLayout_12, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_6, "")
        self.buttonPlayFilteredSound = QPushButton(self.frame)
        self.buttonPlayFilteredSound.setObjectName(u"buttonPlayFilteredSound")
        self.buttonPlayFilteredSound.setGeometry(QRect(10, 130, 111, 51))
        self.buttonPlayFilteredSound.setContextMenuPolicy(Qt.DefaultContextMenu)
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/play-button-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonPlayFilteredSound.setIcon(icon2)
        self.buttonPlayFilteredSound.setIconSize(QSize(25, 25))
        self.buttonPlayOriginalSound = QPushButton(self.frame)
        self.buttonPlayOriginalSound.setObjectName(u"buttonPlayOriginalSound")
        self.buttonPlayOriginalSound.setGeometry(QRect(10, 70, 111, 51))
        self.buttonPlayOriginalSound.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.buttonPlayOriginalSound.setIcon(icon2)
        self.buttonPlayOriginalSound.setIconSize(QSize(25, 25))
        self.buttonStop = QPushButton(self.frame)
        self.buttonStop.setObjectName(u"buttonStop")
        self.buttonStop.setGeometry(QRect(10, 190, 271, 51))
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/stop-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonStop.setIcon(icon3)
        self.buttonStop.setIconSize(QSize(25, 25))
        self.soundInfoList = QListWidget(self.frame)
        self.soundInfoList.setObjectName(u"soundInfoList")
        self.soundInfoList.setGeometry(QRect(10, 270, 271, 111))
        self.soundInfoList.setSelectionMode(QAbstractItemView.NoSelection)
        self.soundInfoList.setSelectionRectVisible(False)
        self.buttonSelectFile = QToolButton(self.frame)
        self.buttonSelectFile.setObjectName(u"buttonSelectFile")
        self.buttonSelectFile.setGeometry(QRect(539, 18, 25, 19))
        self.lineEditFilePath = QLineEdit(self.frame)
        self.lineEditFilePath.setObjectName(u"lineEditFilePath")
        self.lineEditFilePath.setGeometry(QRect(110, 10, 421, 31))
        self.labelFilePath = QLabel(self.frame)
        self.labelFilePath.setObjectName(u"labelFilePath")
        self.labelFilePath.setGeometry(QRect(10, 14, 191, 31))
        self.labelFilePath.setFont(font)
        self.buttonGraphOriginal = QPushButton(self.frame)
        self.buttonGraphOriginal.setObjectName(u"buttonGraphOriginal")
        self.buttonGraphOriginal.setGeometry(QRect(130, 70, 151, 51))
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/line-graph-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonGraphOriginal.setIcon(icon4)
        self.buttonGraphOriginal.setIconSize(QSize(25, 25))
        self.buttonGraphFiltered = QPushButton(self.frame)
        self.buttonGraphFiltered.setObjectName(u"buttonGraphFiltered")
        self.buttonGraphFiltered.setGeometry(QRect(130, 130, 151, 51))
        self.buttonGraphFiltered.setIcon(icon4)
        self.buttonGraphFiltered.setIconSize(QSize(25, 25))
        self.buttonSave = QPushButton(self.frame)
        self.buttonSave.setObjectName(u"buttonSave")
        self.buttonSave.setGeometry(QRect(570, 10, 151, 41))
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/diskette-save-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonSave.setIcon(icon5)
        self.buttonSave.setIconSize(QSize(25, 25))
        self.soundInfoLabel = QLabel(self.frame)
        self.soundInfoLabel.setObjectName(u"soundInfoLabel")
        self.soundInfoLabel.setGeometry(QRect(10, 250, 71, 16))
        font1 = QFont()
        font1.setPointSize(10)
        self.soundInfoLabel.setFont(font1)

        self.gridLayout_2.addWidget(self.frame, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 982, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Audio digital filtering", None))
        self.blendLabel.setText(QCoreApplication.translate("MainWindow", u"Blend", None))
        self.blendLabelValue.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.rangLabel.setText(QCoreApplication.translate("MainWindow", u"Range", None))
        self.volumeLabel.setText(QCoreApplication.translate("MainWindow", u"Volume", None))
        self.driveLabel.setText(QCoreApplication.translate("MainWindow", u"Drive", None))
        self.volumeLabelValue.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.driveLabelValue.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.rangeLabelValue.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.buttonFilterDistortion.setText(QCoreApplication.translate("MainWindow", u"Apply filter", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Distortion", None))
        self.echoLevelLabelValue.setText(QCoreApplication.translate("MainWindow", u"echoLabel", None))
        self.delayTimeLabelValue.setText(QCoreApplication.translate("MainWindow", u"delayLabel", None))
        self.blurIntervalLabel.setText(QCoreApplication.translate("MainWindow", u"Blur interval", None))
        self.blurIntervalLabelValue.setText(QCoreApplication.translate("MainWindow", u"blurLabel", None))
        self.delayTimeLabel.setText(QCoreApplication.translate("MainWindow", u"Delay time", None))
        self.echoLevelLabel.setText(QCoreApplication.translate("MainWindow", u"Echo level", None))
        self.buttonFilterEcho.setText(QCoreApplication.translate("MainWindow", u"Apply filter", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Echo", None))
        self.sensitivityLabel.setText(QCoreApplication.translate("MainWindow", u"Sensitivity", None))
        self.mutePowerLabel.setText(QCoreApplication.translate("MainWindow", u"Mute Power", None))
        self.mutePowerLabelValue.setText(QCoreApplication.translate("MainWindow", u"MuteLabel", None))
        self.fadeLengthLabelValue.setText(QCoreApplication.translate("MainWindow", u"FadeLabel", None))
        self.fadeLengtLabel.setText(QCoreApplication.translate("MainWindow", u"Fade Length", None))
        self.sensitivityLabelValue.setText(QCoreApplication.translate("MainWindow", u"SensLabel", None))
        self.buttonFilterRemovingClicksAndPops.setText(QCoreApplication.translate("MainWindow", u"Apply filter", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Click/Pop Removal", None))
        self.buttonFilterTime.setText(QCoreApplication.translate("MainWindow", u"Apply filter", None))
        self.timeLabelValue.setText(QCoreApplication.translate("MainWindow", u"100%", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"Time", None))
        self.offsetSamplesLabel.setText(QCoreApplication.translate("MainWindow", u"Offset Samples", None))
        self.aggressionLabelValue.setText(QCoreApplication.translate("MainWindow", u"AggressionLabel", None))
        self.offsetSamplesLabelValue.setText(QCoreApplication.translate("MainWindow", u"OffsetSamples", None))
        self.aggressionLabel.setText(QCoreApplication.translate("MainWindow", u"Aggression", None))
        self.buttonFilterRemoveSilence.setText(QCoreApplication.translate("MainWindow", u"Apply filter", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Remove silence", None))
        self.leftFadeStrenghtLabel.setText(QCoreApplication.translate("MainWindow", u"Left Fade Strenght", None))
        self.leftFadeStrenghtLabelValue.setText(QCoreApplication.translate("MainWindow", u"leftFadeStrenght", None))
        self.leftFadeLengthLable.setText(QCoreApplication.translate("MainWindow", u"Left Fade Length", None))
        self.leftFadeLengthLableValue.setText(QCoreApplication.translate("MainWindow", u"leftFadeLength", None))
        self.rightFadeLengthLable.setText(QCoreApplication.translate("MainWindow", u"Right Fade Length", None))
        self.rightFadeLengthLableValue.setText(QCoreApplication.translate("MainWindow", u"rightFadeLength", None))
        self.rightFadeStrenghtLabel.setText(QCoreApplication.translate("MainWindow", u"Right Fade Strenght", None))
        self.rightFadeStrenghtLabelValue.setText(QCoreApplication.translate("MainWindow", u"rightFadeStrenght", None))
        self.buttonFilterFade.setText(QCoreApplication.translate("MainWindow", u"Apply filter", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"Fade", None))
        self.buttonPlayFilteredSound.setText(QCoreApplication.translate("MainWindow", u"Play filtered", None))
        self.buttonPlayOriginalSound.setText(QCoreApplication.translate("MainWindow", u"Play original", None))
        self.buttonStop.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.buttonSelectFile.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.labelFilePath.setText(QCoreApplication.translate("MainWindow", u"Enter file path:", None))
        self.buttonGraphOriginal.setText(QCoreApplication.translate("MainWindow", u"Draw graph original", None))
        self.buttonGraphFiltered.setText(QCoreApplication.translate("MainWindow", u"Draw graph filtered", None))
        self.buttonSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.soundInfoLabel.setText(QCoreApplication.translate("MainWindow", u"Sound info:", None))
    # retranslateUi

