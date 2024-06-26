# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerMOvpLa.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Ui_ConnectDialog(object):
    def setupUi(self, ConnectDialog):
        if not ConnectDialog.objectName():
            ConnectDialog.setObjectName(u"ConnectDialog")
        ConnectDialog.resize(452, 305)
        ConnectDialog.setStyleSheet(u"background-color: black;")
        self.gridLayout = QGridLayout(ConnectDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(10, 10, 20, 10)
        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 6, 0, 1, 2)

        self.verbindungs_label = QLabel(ConnectDialog)
        self.verbindungs_label.setObjectName(u"verbindungs_label")
        font = QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.verbindungs_label.setFont(font)
        self.verbindungs_label.setAutoFillBackground(False)
        self.verbindungs_label.setStyleSheet(u"QLabel {background: black; color: white;}")
        self.verbindungs_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.verbindungs_label, 0, 0, 1, 2)

        self.button_box = QDialogButtonBox(ConnectDialog)
        self.button_box.setObjectName(u"button_box")
        self.button_box.setStyleSheet(u"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: white;\n"
"min-width: 10em;\n"
"margin-right: 5px;\n"
"padding: 7px;\n"
"color: white;")
        self.button_box.setOrientation(Qt.Horizontal)
        self.button_box.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.button_box, 7, 0, 1, 2)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 1, 0, 1, 2)

        self.ports_label = QLabel(ConnectDialog)
        self.ports_label.setObjectName(u"ports_label")
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(False)
        font1.setWeight(50)
        self.ports_label.setFont(font1)
        self.ports_label.setStyleSheet(u"background: black; color: white;")
        self.ports_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.ports_label, 2, 0, 4, 1)

        self.combo_box = QComboBox(ConnectDialog)
        self.combo_box.addItem("")
        self.combo_box.addItem("")
        self.combo_box.setObjectName(u"combo_box")
        font2 = QFont()
        font2.setPointSize(14)
        self.combo_box.setFont(font2)
        self.combo_box.setStyleSheet(u"QComboBox\n"
"{\n"
"    color:white;\n"
"    background-color: black;\n"
"    border-color: rgba(255,255,255,255);\n"
"    border-width: 1px;\n"
"    border-style: outset;\n"
"    border-radius: 10px;\n"
"}\n"
"QComboBox:editable {\n"
"    background: white;\n"
"    color:white;\n"
"}\n"
"QCombobox:!editable\n"
"{\n"
"    color:white;\n"
"}\n"
"QComboBox QListView\n"
"{\n"
"    color: white;\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"    width: 20px;\n"
"    border: 1px;\n"
"    border-color:white;\n"
"    border-left-style:outset;\n"
"    border-radius: 10px;\n"
"    border-top-style: none;\n"
"    border-bottom-style: none;\n"
"    border-right-style: none;\n"
"}")
        self.combo_box.setEditable(False)

        self.gridLayout.addWidget(self.combo_box, 2, 1, 4, 1)

        self.gridLayout.setRowStretch(0, 4)
        self.gridLayout.setRowStretch(2, 3)

        self.retranslateUi(ConnectDialog)
        self.button_box.accepted.connect(ConnectDialog.accept)
        self.button_box.rejected.connect(ConnectDialog.reject)

        QMetaObject.connectSlotsByName(ConnectDialog)
    # setupUi

    def retranslateUi(self, ConnectDialog):
        ConnectDialog.setWindowTitle(QCoreApplication.translate("ConnectDialog", u"BetaFocus - Verbinden", None))
        self.verbindungs_label.setText(QCoreApplication.translate("ConnectDialog", u"Verbindung", None))
        self.ports_label.setText(QCoreApplication.translate("ConnectDialog", u"Port ausw\u00e4hlen:", None))
        self.combo_box.setItemText(0, QCoreApplication.translate("ConnectDialog", u"COM1", None))
        self.combo_box.setItemText(1, QCoreApplication.translate("ConnectDialog", u"COM2", None))

    # retranslateUi

