################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.6
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *  # type: ignore
from PyQt5.QtGui import *  # type: ignore
from PyQt5.QtWidgets import *  # type: ignore


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(900, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(900, 600))
        MainWindow.setMaximumSize(QSize(900, 600))
        MainWindow.setStyleSheet(u"background-color: black;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 0, 881, 541))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.info_button = QPushButton(self.layoutWidget)
        self.info_button.setObjectName(u"info_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.info_button.sizePolicy().hasHeightForWidth())
        self.info_button.setSizePolicy(sizePolicy1)
        self.info_button.setMinimumSize(QSize(25, 25))
        self.info_button.setMaximumSize(QSize(30, 30))
        self.info_button.setStyleSheet(u"border-style: outset;\n"
                                       "border-width: 2px;\n"
                                       "border-radius: 14px;\n"
                                       "border-color: white;\n"
                                       "padding: 7px;\n"
                                       "color: white;")

        self.gridLayout.addWidget(self.info_button, 0, 0, 1, 1, Qt.AlignTop)

        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(500, 100))
        self.label.setMaximumSize(QSize(500, 100))
        font = QFont()
        font.setPointSize(60)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: white;")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 1, 1, 3, Qt.AlignHCenter)

        self.help_button = QPushButton(self.layoutWidget)
        self.help_button.setObjectName(u"help_button")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.help_button.sizePolicy().hasHeightForWidth())
        self.help_button.setSizePolicy(sizePolicy2)
        self.help_button.setMinimumSize(QSize(25, 25))
        self.help_button.setMaximumSize(QSize(30, 30))
        self.help_button.setStyleSheet(u"border-style: outset;\n"
                                       "border-width: 2px;\n"
                                       "border-radius: 14px;\n"
                                       "border-color: white;\n"
                                       "padding: 7px;\n"
                                       "color: white;")

        self.gridLayout.addWidget(self.help_button, 0, 4, 1, 1, Qt.AlignTop)

        self.start_button = QPushButton(self.layoutWidget)
        self.start_button.setObjectName(u"start_button")
        sizePolicy.setHeightForWidth(self.start_button.sizePolicy().hasHeightForWidth())
        self.start_button.setSizePolicy(sizePolicy)
        self.start_button.setMinimumSize(QSize(300, 300))
        self.start_button.setMaximumSize(QSize(300, 300))
        font1 = QFont()
        font1.setPointSize(25)
        self.start_button.setFont(font1)
        self.start_button.setStyleSheet(u"image: url(images:start.png);\n"
                                        "padding-left: 20px;\n"
                                        "padding-top: 20px;\n"
                                        "padding-bottom: 50px;\n"
                                        "text-align: center;\n"
                                        "color: white;")

        self.gridLayout.addWidget(self.start_button, 1, 2, 1, 1)

        self.connect_button = QPushButton(self.layoutWidget)
        self.connect_button.setObjectName(u"pushButton")
        sizePolicy.setHeightForWidth(self.connect_button.sizePolicy().hasHeightForWidth())
        self.connect_button.setSizePolicy(sizePolicy)
        self.connect_button.setMinimumSize(QSize(250, 75))
        self.connect_button.setMaximumSize(QSize(250, 75))
        self.connect_button.setFont(font1)
        self.connect_button.setStyleSheet(u"border-style: outset;\n"
                                          "border-width: 2px;\n"
                                          "border-radius: 10px;\n"
                                          "border-color: white;\n"
                                          "min-width:15em;\n"
                                          "color: white;")

        self.gridLayout.addWidget(self.connect_button, 2, 1, 1, 1)

        self.stats_button = QPushButton(self.layoutWidget)
        self.stats_button.setObjectName(u"stats_button")
        sizePolicy.setHeightForWidth(self.stats_button.sizePolicy().hasHeightForWidth())
        self.stats_button.setSizePolicy(sizePolicy)
        self.stats_button.setMinimumSize(QSize(250, 75))
        self.stats_button.setMaximumSize(QSize(250, 75))
        self.stats_button.setFont(font1)
        self.stats_button.setStyleSheet(u"border-style: outset;\n"
                                        "border-width: 2px;\n"
                                        "border-radius: 10px;\n"
                                        "border-color: white;\n"
                                        "min-width:15em;\n"
                                        "color: white;")

        self.gridLayout.addWidget(self.stats_button, 2, 3, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        MainWindow.adjustSize()

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"BetaFocus", None))
        self.info_button.setToolTip(QCoreApplication.translate("MainWindow", u"Wie funktioniert's?", None))
        self.info_button.setText(QCoreApplication.translate("MainWindow", u"i", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"BetaFocus", None))
        self.help_button.setToolTip(QCoreApplication.translate("MainWindow", u"Hilfe", None))
        self.help_button.setText(QCoreApplication.translate("MainWindow", u"?", None))
        self.start_button.setText(QCoreApplication.translate("MainWindow", u"Los geht's!\t\t\t", None))
        self.connect_button.setText(QCoreApplication.translate("MainWindow", u"Verbinden", None))
        self.stats_button.setText(QCoreApplication.translate("MainWindow", u"Statistiken", None))
    # retranslateUi
