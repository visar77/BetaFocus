################################################################################
## Form generated from reading UI file 'runwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.6
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import os.path

from PyQt5.QtCore import *  # type: ignore
from PyQt5.QtGui import *  # type: ignore
from PyQt5.QtWidgets import *  # type: ignore


class Ui_RunWindow(object):

    image_path = os.path.join(os.path.dirname(__file__), "images")

    def setupUi(self, RunWindow):
        if not RunWindow.objectName():
            RunWindow.setObjectName(u"RunWindow")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHeightForWidth(RunWindow.sizePolicy().hasHeightForWidth())
        RunWindow.setSizePolicy(sizePolicy)
        RunWindow.setStyleSheet(u"background-color: black;")
        self.widget = QWidget(RunWindow)
        self.widget.setObjectName(u"widget")
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
        self.pause_button.setStyleSheet(u"image: url(images:pause.png);")

        self.gridLayout.addWidget(self.pause_button, 5, 3, 1, 1)

        self.resume_button = QPushButton(self.widget)
        self.resume_button.setObjectName(u"pause_button")
        sizePolicy.setHeightForWidth(self.pause_button.sizePolicy().hasHeightForWidth())
        self.resume_button.setSizePolicy(sizePolicy)
        self.resume_button.setMinimumSize(QSize(120, 120))
        self.resume_button.setMaximumSize(QSize(120, 120))
        self.resume_button.setStyleSheet(f"image: url(images:start.png);")

        self.gridLayout.addWidget(self.resume_button, 5, 3, 1, 1)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(60)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: white;")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 1, 1, 1, 3, Qt.AlignHCenter)

        self.time_label = QLabel(self.widget)
        self.time_label.setObjectName(u"time_label")
        sizePolicy.setHeightForWidth(self.time_label.sizePolicy().hasHeightForWidth())
        self.time_label.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(120)
        self.time_label.setFont(font1)
        self.time_label.setStyleSheet(u"color: white;")
        self.time_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.time_label, 3, 1, 1, 3, Qt.AlignHCenter)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 2, 2, 1, 1)

        self.stop_button = QPushButton(self.widget)
        self.stop_button.setObjectName(u"stop_button")
        sizePolicy.setHeightForWidth(self.stop_button.sizePolicy().hasHeightForWidth())
        self.stop_button.setSizePolicy(sizePolicy)
        self.stop_button.setMinimumSize(QSize(120, 120))
        self.stop_button.setMaximumSize(QSize(120, 120))
        self.stop_button.setStyleSheet(u"image: url(images:stop.png);")

        self.gridLayout.addWidget(self.stop_button, 5, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout.addItem(self.horizontalSpacer_3, 5, 4, 1, 1)

        self.verticalSpacer_1 = QSpacerItem(0, 100, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.gridLayout.addItem(self.verticalSpacer_1, 2, 1, 1, 3)

        self.verticalSpacer_2 = QSpacerItem(0, 100, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.gridLayout.addItem(self.verticalSpacer_2, 4, 1, 1, 3)

        self.verticalSpacer_3 = QSpacerItem(0, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.gridLayout.addItem(self.verticalSpacer_3, 6, 1, 1, 3)

        self.verticalSpacer_4 = QSpacerItem(0, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.gridLayout.addItem(self.verticalSpacer_3, 0, 1, 1, 3)


        self.retranslateUi(RunWindow)


        RunWindow.setFixedSize(self.gridLayout.totalSizeHint())

        QMetaObject.connectSlotsByName(RunWindow)
    # setupUi

    def retranslateUi(self, RunWindow):
        RunWindow.setWindowTitle(QCoreApplication.translate("RunWindow", u"BetaFocus", None))
        self.pause_button.setText("")
        self.resume_button.setText("")
        self.label.setText(QCoreApplication.translate("RunWindow", u"You BetaFocus right now!", None))
        self.time_label.setText(QCoreApplication.translate("RunWindow", u"00:00:00", None))
        self.stop_button.setText("")
    # retranslateUi

