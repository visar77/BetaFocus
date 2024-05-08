import sys

from PyQt5.QtWidgets import QMainWindow, QGridLayout, QWidget, QDesktopWidget, QApplication
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt, QSize

from .ui.ui_mainwindow import Ui_MainWindow
from .ui.ui_runwindow import Ui_RunWindow


class HelpWindow(QWidget):

    def __init__(self):
        super(HelpWindow, self).__init__()
        self.setFixedSize(920, 620)
        self.setWindowTitle("BetaFocus")
        self.setStyleSheet("background-color: black;")
        layout = QGridLayout()
        layout.setAlignment(Qt.AlignHCenter)
        layout.setContentsMargins(20, 40, 20, 20)


class InfoWindow(QWidget):

    def __init__(self):
        super(InfoWindow, self).__init__()
        self.setFixedSize(920, 620)
        self.setWindowTitle("BetaFocus")
        self.setStyleSheet("background-color: black;")
        layout = QGridLayout()
        layout.setAlignment(Qt.AlignHCenter)
        layout.setContentsMargins(20, 40, 20, 20)


class StatsWindow(QWidget):
    def __init__(self):
        super(StatsWindow, self).__init__()
        self.setFixedSize(920, 620)
        self.setWindowTitle("BetaFocus")
        self.setStyleSheet("background-color: black;")
        layout = QGridLayout()
        layout.setAlignment(Qt.AlignHCenter)
        layout.setContentsMargins(20, 40, 20, 20)


class RunWindow(QWidget):

    def __init__(self, start_button):
        super(RunWindow, self).__init__()
        self.runWindow_ui = Ui_RunWindow()
        self.runWindow_ui.setupUi(self)
        # start button
        self.start_button = start_button
        # label at the top of the window
        self.label = self.runWindow_ui.label
        # label that displays the time passed
        self.time_label = self.runWindow_ui.time_label
        # set control buttons
        self.stop_button = self.runWindow_ui.stop_button
        self.pause_button = self.runWindow_ui.pause_button
        self.resume_button = self.runWindow_ui.resume_button
        self.resume_button.hide()


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.mainWindow_ui = Ui_MainWindow()
        self.mainWindow_ui.setupUi(self)
        self.center()
        # triangular start button
        self.start_button = self.mainWindow_ui.start_button
        # statistics button at the bottom right
        self.stats_button = self.mainWindow_ui.stats_button
        pic = QPixmap("./gui/images/stats.png")
        self.stats_button.setIcon(QIcon(pic))
        self.stats_button.setIconSize(QSize(20, 20))
        # connect button at the bottom left
        self.connect_button = self.mainWindow_ui.connect_button
        pic = QPixmap("./gui/images/connect.jpeg")
        self.connect_button.setIcon(QIcon(pic))
        self.connect_button.setIconSize(QSize(20, 20))
        # information button in the top left corner
        self.info_button = self.mainWindow_ui.info_button
        # help button in the top right corner
        self.help_button = self.mainWindow_ui.help_button
        # other windows are widgets and children of the main window
        self.run_window = RunWindow(self.start_button)
        self.stats_window = StatsWindow()
        self.info_window = InfoWindow()
        self.help_window = HelpWindow()

    def center(self):
        """
        centers the main window according to the desktop size of the device used
        """
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        # top left of rectangle becomes top left of window centering it
        self.move(qr.topLeft())


class App(QApplication):

    def __init__(self):
        super().__init__(sys.argv)
        self.mainWindow = MainWindow()
