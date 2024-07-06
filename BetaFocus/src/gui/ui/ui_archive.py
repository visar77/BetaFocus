################################################################################
## Form generated from reading UI file 'archive.ui'
##
## Created by: Qt User Interface Compiler version 5.15.6
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *  # type: ignore
from PyQt5.QtGui import *  # type: ignore
from PyQt5.QtWidgets import *  # type: ignore

from pyqtgraph import PlotWidget, DateAxisItem


class Ui_Archive(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Archive")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        Form.setSizePolicy(sizePolicy)

        Form.setStyleSheet(u"background-color: black;")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.top_label = QLabel(self.widget)
        self.top_label.setObjectName(u"top_label")
        sizePolicy.setHeightForWidth(self.top_label.sizePolicy().hasHeightForWidth())
        self.top_label.setSizePolicy(sizePolicy)
        self.top_label.setMinimumSize(QSize(920, 150))
        self.top_label.setMaximumSize(QSize(16777215, 200))
        self.top_label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        font = QFont()
        font.setPointSize(60)
        self.top_label.setFont(font)
        self.top_label.setStyleSheet(u"color: white;")

        self.gridLayout_2.addWidget(self.top_label, 0, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(30, -1, 30, -1)
        font1 = QFont()
        font1.setPointSize(20)
        self.label_1 = QLabel(self.widget)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setMaximumSize(QSize(16777215, 100))
        self.label_1.setFont(font1)
        self.label_1.setStyleSheet(u"color: white;")

        self.gridLayout.addWidget(self.label_1, 0, 0, 1, 1)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 100))
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: white;")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 100))
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"color: white;")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 100))
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"color: white;")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 100))
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"color: white;")

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setContentsMargins(0, 0, 0,
                                                 20)  # Add a bottom margin to bring the buttons closer to the labels
        self.prev_button = QPushButton("<", self.widget)
        self.prev_button.setObjectName(u"prev_button")
        self.prev_button.setFont(font1)
        self.prev_button.hide()
        self.prev_button.setStyleSheet(u"border-style: outset;\n"
                                       "border-width: 2px;\n"
                                       "border-radius: 10px;\n"
                                       "border-color: white;\n"
                                       "min-width: 5em;\n"
                                       "min-height: 1em;\n"
                                       "padding: 7px;\n"
                                       "margin-top: 40px;\n"
                                       "color: white;")

        self.horizontalLayout.addWidget(self.prev_button)

        self.next_button = QPushButton(">", self.widget)
        self.next_button.setObjectName(u"next_button")
        self.next_button.setFont(font1)
        self.next_button.setStyleSheet(u"border-style: outset;\n"
                                       "border-width: 2px;\n"
                                       "border-radius: 10px;\n"
                                       "border-color: white;\n"
                                       "min-width: 5em;\n"
                                       "min-height: 1em;\n"
                                       "padding: 7px;\n"
                                       "margin-top: 40px;\n"
                                       "color: white;")

        self.horizontalLayout.addWidget(self.next_button)

        self.gridLayout.addLayout(self.horizontalLayout, 5, 0, 1, 1)

        self.widget1 = PlotWidget(self.widget, axisItems={'bottom': DateAxisItem()})
        self.widget1.setObjectName(u"widget1")
        self.widget1.setBackground('black')
        self.widget1.setTitle("<span style=\"color:white;\">Konzentrationszeit nach Session</span>")
        self.widget1.setLabel('left', "<span style=\"color:white;\">Konzentrierte Zeit in Min.</span>")
        self.widget1.setLabel('bottom', "<span style=\"color:white;\">Session</span>")
        sizePolicy.setHeightForWidth(self.widget1.sizePolicy().hasHeightForWidth())
        self.widget1.setSizePolicy(sizePolicy)
        self.widget1.setMinimumSize(QSize(400, 300))

        self.gridLayout.addWidget(self.widget1, 0, 1, 4, 1)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setContentsMargins(0, 40, 0, 0)
        self.pushButton.setFont(font1)
        self.pushButton.setStyleSheet(u"border-style: outset;\n"
                                      "border-width: 2px;\n"
                                      "border-radius: 10px;\n"
                                      "border-color: white;\n"
                                      "min-width: 15em;\n"
                                      "min-height: 3em;\n"
                                      "padding: 7px;\n"
                                      "margin-top: 40px;\n"
                                      "color: white;")

        self.gridLayout.addWidget(self.pushButton, 4, 1, 1, 1, Qt.AlignHCenter | Qt.AlignVCenter)

        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)

        self.retranslateUi(Form)

        Form.setFixedSize(self.gridLayout_2.sizeHint())

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.top_label.setText(QCoreApplication.translate("Form",
                                                          u"<html><head/><body><p align=\"center\"><span style=\" font-size:40pt;\">Archiv</span></p></body></html>",
                                                          None))
        self.label_1.setText(QCoreApplication.translate("Form",
                                                        u"<html><head/><body><p><span style=\" font-size:20pt;\"> </span></p></body></html>",
                                                        None))
        self.label_2.setText(QCoreApplication.translate("Form",
                                                        u"<html><head/><body><p><span style=\" font-size:20pt;\"> </span></p></body></html>",
                                                        None))
        self.label_3.setText(QCoreApplication.translate("Form",
                                                        u"<html><head/><body><p><span style=\" font-size:20pt;\"> </span></p></body></html>",
                                                        None))
        self.label_4.setText(QCoreApplication.translate("Form",
                                                        u"<html><head/><body><p><span style=\" font-size:20pt;\"> </span></p></body></html>",
                                                        None))
        self.label_5.setText(QCoreApplication.translate("Form",
                                                        u"<html><head/><body><p><span style=\" font-size:20pt;\"> </span></p></body></html>",
                                                        None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Go Focus Now!", None))
    # retranslateUi
