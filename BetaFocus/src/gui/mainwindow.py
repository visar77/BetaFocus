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
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(900, 600))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_4 = QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.stats_button = QPushButton(self.centralwidget)
        self.stats_button.setObjectName(u"stats_button")
        self.stats_button.setMinimumSize(QSize(300, 75))
        self.stats_button.setMaximumSize(QSize(300, 75))
        font = QFont()
        font.setPointSize(30)
        self.stats_button.setFont(font)

        self.gridLayout.addWidget(self.stats_button, 5, 1, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(300, 100))
        self.label.setMaximumSize(QSize(300, 100))
        font1 = QFont()
        font1.setPointSize(60)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignHCenter)

        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)

        self.start_button = QPushButton(self.centralwidget)
        self.start_button.setObjectName(u"start_button")
        self.start_button.setMinimumSize(QSize(300, 300))
        self.start_button.setMaximumSize(QSize(300, 300))
        self.start_button.setFont(font)

        self.gridLayout.addWidget(self.start_button, 2, 1, 1, 1)

        self.help_button = QPushButton(self.centralwidget)
        self.help_button.setObjectName(u"help_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.help_button.sizePolicy().hasHeightForWidth())
        self.help_button.setSizePolicy(sizePolicy1)
        self.help_button.setMinimumSize(QSize(25, 25))
        self.help_button.setMaximumSize(QSize(30, 30))

        self.gridLayout.addWidget(self.help_button, 0, 2, 1, 1, Qt.AlignRight)

        self.info_button = QPushButton(self.centralwidget)
        self.info_button.setObjectName(u"info_button")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(1)
        sizePolicy2.setHeightForWidth(self.info_button.sizePolicy().hasHeightForWidth())
        self.info_button.setSizePolicy(sizePolicy2)
        self.info_button.setMinimumSize(QSize(25, 25))
        self.info_button.setMaximumSize(QSize(30, 30))

        self.gridLayout.addWidget(self.info_button, 0, 0, 1, 1, Qt.AlignLeft)


        self.gridLayout_4.addLayout(self.gridLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 900, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.stats_button.setText(QCoreApplication.translate("MainWindow", u"Statistiken", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"BetaFocus", None))
        self.start_button.setText(QCoreApplication.translate("MainWindow", u"Start", None))
#if QT_CONFIG(tooltip)
        self.help_button.setToolTip(QCoreApplication.translate("MainWindow", u"Hilfe", None))
#endif // QT_CONFIG(tooltip)
        self.help_button.setText(QCoreApplication.translate("MainWindow", u" ? ", None))
#if QT_CONFIG(tooltip)
        self.info_button.setToolTip(QCoreApplication.translate("MainWindow", u"Wie funktioniert's?", None))
#endif // QT_CONFIG(tooltip)
        self.info_button.setText(QCoreApplication.translate("MainWindow", u" i ", None))
    # retranslateUi

