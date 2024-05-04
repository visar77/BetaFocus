################################################################################
## Form generated from reading UI file 'runwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.6
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *  # type: ignore
from PyQt5.QtGui import *  # type: ignore
from PyQt5.QtWidgets import *  # type: ignore


class Ui_RunWindow(object):
    def setupUi(self, RunWindow):
        if not RunWindow.objectName():
            RunWindow.setObjectName(u"RunWindow")
        RunWindow.resize(920, 620)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(RunWindow.sizePolicy().hasHeightForWidth())
        RunWindow.setSizePolicy(sizePolicy)
        RunWindow.setMinimumSize(QSize(920, 620))
        RunWindow.setMaximumSize(QSize(920, 620))
        RunWindow.setStyleSheet(u"background-color: black;")
        self.widget = QWidget(RunWindow)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 901, 601))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(7)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 2, 0, 1, 1)

        self.pause_button = QPushButton(self.widget)
        self.pause_button.setObjectName(u"pause_button")
        sizePolicy.setHeightForWidth(self.pause_button.sizePolicy().hasHeightForWidth())
        self.pause_button.setSizePolicy(sizePolicy)
        self.pause_button.setMinimumSize(QSize(120, 120))
        self.pause_button.setMaximumSize(QSize(120, 120))
        self.pause_button.setStyleSheet(u"image: url(./gui/images/pause.png);")

        self.gridLayout.addWidget(self.pause_button, 2, 3, 1, 1)

        self.resume_button = QPushButton(self.widget)
        self.resume_button.setObjectName(u"pause_button")
        sizePolicy.setHeightForWidth(self.pause_button.sizePolicy().hasHeightForWidth())
        self.resume_button.setSizePolicy(sizePolicy)
        self.resume_button.setMinimumSize(QSize(120, 120))
        self.resume_button.setMaximumSize(QSize(120, 120))
        self.resume_button.setStyleSheet(u"image: url(./gui/images/start.png);")

        self.gridLayout.addWidget(self.resume_button, 2, 3, 1, 1)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(800, 150))
        self.label.setMaximumSize(QSize(800, 150))
        font = QFont()
        font.setPointSize(60)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: white;")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 1, 1, 3, Qt.AlignHCenter)

        self.time_label = QLabel(self.widget)
        self.time_label.setObjectName(u"time_label")
        sizePolicy.setHeightForWidth(self.time_label.sizePolicy().hasHeightForWidth())
        self.time_label.setSizePolicy(sizePolicy)
        self.time_label.setMinimumSize(QSize(650, 150))
        self.time_label.setMaximumSize(QSize(650, 150))
        font1 = QFont()
        font1.setPointSize(120)
        self.time_label.setFont(font1)
        self.time_label.setStyleSheet(u"color: white;")
        self.time_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.time_label, 1, 1, 1, 3, Qt.AlignHCenter)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 2, 2, 1, 1)

        self.stop_button = QPushButton(self.widget)
        self.stop_button.setObjectName(u"stop_button")
        sizePolicy.setHeightForWidth(self.stop_button.sizePolicy().hasHeightForWidth())
        self.stop_button.setSizePolicy(sizePolicy)
        self.stop_button.setMinimumSize(QSize(120, 120))
        self.stop_button.setMaximumSize(QSize(120, 120))
        self.stop_button.setStyleSheet(u"image: url(./gui/images/stop.png);")

        self.gridLayout.addWidget(self.stop_button, 2, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 2, 4, 1, 1)


        self.retranslateUi(RunWindow)

        QMetaObject.connectSlotsByName(RunWindow)
    # setupUi

    def retranslateUi(self, RunWindow):
        RunWindow.setWindowTitle(QCoreApplication.translate("RunWindow", u"BetaFocus", None))
        self.pause_button.setText("")
        self.resume_button.setText("")
        self.label.setText(QCoreApplication.translate("RunWindow", u"You BetaFocus right now!", None))
        self.time_label.setText(QCoreApplication.translate("RunWindow", u"00:00:00:00", None))
        self.stop_button.setText("")
    # retranslateUi

