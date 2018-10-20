# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(698, 521)
        MainWindow.setMinimumSize(QtCore.QSize(698, 521))
        MainWindow.setMaximumSize(QtCore.QSize(698, 521))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/player.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout_2 = QtGui.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.frame_2 = QtGui.QFrame(self.frame)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.gridLayout_3 = QtGui.QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.videoPlayer = phonon.Phonon.VideoPlayer(self.frame_2)
        self.videoPlayer.setMinimumSize(QtCore.QSize(640, 360))
        self.videoPlayer.setObjectName(_fromUtf8("videoPlayer"))
        self.gridLayout_3.addWidget(self.videoPlayer, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_2, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.volumeSlider = phonon.Phonon.VolumeSlider(self.frame)
        self.volumeSlider.setMinimumSize(QtCore.QSize(20, 0))
        self.volumeSlider.setMaximumSize(QtCore.QSize(150, 16777215))
        self.volumeSlider.setObjectName(_fromUtf8("volumeSlider"))
        self.horizontalLayout_2.addWidget(self.volumeSlider)
        self.seekSlider = phonon.Phonon.SeekSlider(self.frame)
        self.seekSlider.setObjectName(_fromUtf8("seekSlider"))
        self.horizontalLayout_2.addWidget(self.seekSlider)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.play_PB = QtGui.QPushButton(self.frame)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/play.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.play_PB.setIcon(icon1)
        self.play_PB.setObjectName(_fromUtf8("play_PB"))
        self.horizontalLayout.addWidget(self.play_PB)
        self.pause_PB = QtGui.QPushButton(self.frame)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/pause.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pause_PB.setIcon(icon2)
        self.pause_PB.setObjectName(_fromUtf8("pause_PB"))
        self.horizontalLayout.addWidget(self.pause_PB)
        self.stop_PB = QtGui.QPushButton(self.frame)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/stop.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stop_PB.setIcon(icon3)
        self.stop_PB.setObjectName(_fromUtf8("stop_PB"))
        self.horizontalLayout.addWidget(self.stop_PB)
        self.gridLayout_2.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 698, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.menuFile.addAction(self.actionOpen)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "My Player", None))
        self.play_PB.setText(_translate("MainWindow", "Play", None))
        self.pause_PB.setText(_translate("MainWindow", "Pause", None))
        self.stop_PB.setText(_translate("MainWindow", "Stop", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionOpen.setText(_translate("MainWindow", "Open", None))

from PyQt4 import phonon
import icons_rc
