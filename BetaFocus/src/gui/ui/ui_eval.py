################################################################################
## Form generated from reading UI file 'auswertung.ui'
##
## Created by: Qt User Interface Compiler version 5.15.6
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *  # type: ignore
from PyQt5.QtGui import *  # type: ignore
from PyQt5.QtWidgets import *  # type: ignore

from pyqtgraph import PlotWidget


class Ui_Eval(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Eval")
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
        self.widget.setGeometry(QRect(10, 10, 901, 601))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.top_label = QLabel(self.widget)
        self.top_label.setObjectName(u"top_label")
        self.top_label.setMaximumSize(QSize(920, 150))
        font = QFont()
        font.setPointSize(40)
        self.top_label.setFont(font)
        self.top_label.setStyleSheet(u"color: white;")

        self.verticalLayout.addWidget(self.top_label)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(20, -1, 10, -1)
        self.label_r1 = QLabel(self.widget)
        self.label_r1.setObjectName(u"label_r1")
        self.label_r1.setMaximumSize(QSize(10000000, 100))
        self.label_r1.setStyleSheet(u"color: white;")

        self.gridLayout.addWidget(self.label_r1, 0, 1, 1, 3)

        self.label_l2 = QLabel(self.widget)
        self.label_l2.setObjectName(u"label_l2")
        self.label_l2.setMinimumSize(QSize(150, 0))
        self.label_l2.setMaximumSize(QSize(16777215, 100))
        self.label_l2.setStyleSheet(u"color: white;")

        self.gridLayout.addWidget(self.label_l2, 1, 0, 1, 1)

        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMaximumSize(QSize(16777215, 80))
        font1 = QFont()
        font1.setPointSize(14)
        self.lineEdit.setFont(font1)
        self.lineEdit.setStyleSheet(u"color: white;")

        self.gridLayout.addWidget(self.lineEdit, 2, 1, 1, 2)

        self.label_r2 = QLabel(self.widget)
        self.label_r2.setObjectName(u"label_r2")
        self.label_r2.setMaximumSize(QSize(16777215, 100))
        self.label_r2.setStyleSheet(u"color: white;")

        self.gridLayout.addWidget(self.label_r2, 1, 1, 1, 3)

        self.label_l3 = QLabel(self.widget)
        self.label_l3.setObjectName(u"label_l3")
        self.label_l3.setMinimumSize(QSize(150, 0))
        self.label_l3.setMaximumSize(QSize(16777215, 100))
        self.label_l3.setStyleSheet(u"color: white;")

        self.gridLayout.addWidget(self.label_l3, 2, 0, 1, 1)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font1)
        self.pushButton.setStyleSheet(u"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: white;\n"
"min-width: 8em;\n"
"padding: 7px;\n"
"color:white;")

        self.gridLayout.addWidget(self.pushButton, 2, 3, 1, 1)

        self.label_l1 = QLabel(self.widget)
        self.label_l1.setObjectName(u"label_l1")
        self.label_l1.setMinimumSize(QSize(150, 0))
        self.label_l1.setMaximumSize(QSize(10000000, 100))
        self.label_l1.setStyleSheet(u"color: white;")

        self.gridLayout.addWidget(self.label_l1, 0, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout, 1, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(10, -1, 10, -1)
        self.canvas_2 = PlotWidget(self.widget)
        self.canvas_2.setObjectName(u"canvas_2")
        sizePolicy.setHeightForWidth(self.canvas_2.sizePolicy().hasHeightForWidth())
        self.canvas_2.setSizePolicy(sizePolicy)
        self.canvas_2.setMinimumSize(QSize(350, 210))

        self.gridLayout_2.addWidget(self.canvas_2, 1, 0, 1, 1)

        self.canvas_1 = PlotWidget(self.widget)
        self.canvas_1.setObjectName(u"canvas_1")
        sizePolicy.setHeightForWidth(self.canvas_1.sizePolicy().hasHeightForWidth())
        self.canvas_1.setSizePolicy(sizePolicy)
        self.canvas_1.setMinimumSize(QSize(350, 210))

        self.gridLayout_2.addWidget(self.canvas_1, 0, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 1, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_3)

        self.archiv_button = QPushButton(self.widget)
        self.archiv_button.setObjectName(u"archiv_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.archiv_button.sizePolicy().hasHeightForWidth())
        self.archiv_button.setSizePolicy(sizePolicy1)
        self.archiv_button.setMaximumSize(QSize(300, 80))
        font2 = QFont()
        font2.setPointSize(15)
        self.archiv_button.setFont(font2)
        self.archiv_button.setStyleSheet(u"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: white;\n"
"min-width: 15em;\n"
"padding: 7px;\n"
"color: white;")

        self.verticalLayout.addWidget(self.archiv_button, 0, Qt.AlignHCenter)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.top_label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">Auswertung</p></body></html>", None))
        self.label_r1.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">00:00:00</span></p></body></html>", None))
        self.label_l2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:14pt;\">Maximale Konzentration</span></p></body></html>", None))
        self.lineEdit.setText("")
        self.label_r2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">%</span></p></body></html>", None))
        self.label_l3.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:14pt;\">Gib der Session<br/>einen Namen:</span></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Fertig", None))
        self.label_l1.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:14pt;\">	Konzentrierte Zeit</span></p></body></html>", None))
        self.archiv_button.setText(QCoreApplication.translate("Form", u"zum Archiv", None))
    # retranslateUi

