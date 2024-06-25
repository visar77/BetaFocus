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

from pyqtgraph import PlotWidget


class Ui_Archive(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Archive")
        Form.resize(920, 620)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(920, 620))
        Form.setMaximumSize(QSize(920, 620))
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
        self.top_label.setMaximumSize(QSize(16777215, 150))
        self.top_label.setAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
        font = QFont()
        font.setPointSize(60)
        self.top_label.setFont(font)
        self.top_label.setStyleSheet(u"color: white;")

        self.gridLayout_2.addWidget(self.top_label, 0, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(30, -1, 30, -1)
        self.label_1 = QLabel(self.widget)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setMaximumSize(QSize(16777215, 100))
        self.label_1.setStyleSheet(u"color: white;")

        self.gridLayout.addWidget(self.label_1, 0, 0, 1, 1)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 100))
        self.label_2.setStyleSheet(u"color: white;")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 100))
        self.label_3.setStyleSheet(u"color: white;")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 100))
        self.label_4.setStyleSheet(u"color: white;")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 100))
        self.label_5.setStyleSheet(u"color: white;")

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.widget1 = PlotWidget(self.widget)
        self.widget1.setObjectName(u"widget1")
        sizePolicy.setHeightForWidth(self.widget1.sizePolicy().hasHeightForWidth())
        self.widget1.setSizePolicy(sizePolicy)
        self.widget1.setMinimumSize(QSize(400, 300))

        self.gridLayout.addWidget(self.widget1, 0, 1, 4, 1)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setContentsMargins(0, 40, 0, 0)
        font1 = QFont()
        font1.setPointSize(20)
        self.pushButton.setFont(font1)
        self.pushButton.setStyleSheet(u"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: white;\n"
"min-width: 15em;\n"
"min-height: 3em;\n"
"padding: 7px;\n"
"margin-top: 15px;\n"
"color: white;")

        self.gridLayout.addWidget(self.pushButton, 4, 1, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)


        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.top_label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:40pt;\">Archiv</span></p></body></html>", None))
        self.label_1.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:20pt;\">Session vom 00.00.0000 00:00:00</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:20pt;\">Session vom 00.00.0000 00:00:00</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:20pt;\">Session vom 00.00.0000 00:00:00</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:20pt;\">Session vom 00.00.0000 00:00:00</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:20pt;\">Session vom 00.00.0000 00:00:00</span></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Jetzt starten!", None))
    # retranslateUi

