import sys

from PyQt5.QtWidgets import QMainWindow, QGridLayout, QWidget, QPushButton, QLabel, QDesktopWidget, QVBoxLayout, \
    QApplication
from PyQt5.QtGui import QFont, QIcon, QPixmap
from PyQt5.QtCore import Qt, QSize

from .mainwindow import Ui_MainWindow


class ControlButton(QPushButton):

    def __init__(self, text: str, url: str):
        super(ControlButton, self).__init__()
        # self.setText(text)
        self.setFont(QFont("Times New Roman", 30, QFont.Bold))
        self.setStyleSheet(f"image: url({url});")


class RunWindow(QWidget):

    def __init__(self):
        super(RunWindow, self).__init__()
        self.setFixedSize(900, 600)
        self.center()
        self.setWindowTitle("BetaFocus")
        self.setStyleSheet("background-color: black;")
        layout = QGridLayout()
        layout.setAlignment(Qt.AlignHCenter)
        layout.setContentsMargins(20, 20, 20, 20)
        # label at the top of the window
        self.label = QLabel("You BetaFocus right now!", self)
        self.label.setFont(QFont("Times New Roman", 60, QFont.Bold))
        self.label.setStyleSheet("color: white;")
        self.label.setAlignment(Qt.AlignHCenter)
        layout.addWidget(self.label, 0, 1, 1, 1)
        # label that displays the time passed
        self.time_label = QLabel("00:00:00:00", self)
        layout.addWidget(self.time_label, 1, 1, 1, 1)
        self.time_label.setAlignment(Qt.AlignHCenter)
        self.time_label.setFont(QFont("Times New Roman", 125, QFont.Bold))
        # set info button and help button
        # TODO: entscheiden ob die da hin müssen oder hässlich sind
        # self.info_button = MiniButton("i")
        # self.info_button.setParent(self)
        # layout.addWidget(self.info_button, 0, 0, 1, 1)
        # self.help_button = MiniButton("?")
        # self.help_button.setParent(self)
        # layout.addWidget(self.help_button, 0, 2, 1, 1)
        # set control buttons
        self.stop_button = ControlButton("Stop", "./gui/images/stop.png")
        self.stop_button.setParent(self)
        layout.addWidget(self.stop_button, 2, 0, 1, 1)
        self.pause_icon = QLabel(self)
        self.pause_pixmap = QPixmap('pause.png')
        self.pause_icon.setPixmap(self.pause_pixmap)
        layout.addWidget(self.pause_icon, 2, 2, 1, 1)
        self.pause_button = ControlButton("Pause", "./gui/images/pause.png")
        self.pause_button.setParent(self)
        layout.addWidget(self.pause_button, 2, 2, 1, 1)
        # set layout to window widget
        self.setLayout(layout)

    def center(self):
        """
        centers the main window according to the desktop size of the device used
        """
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        # top left of rectangle becomes top left of window centering it
        self.move(qr.topLeft())


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.mainWindow_ui = Ui_MainWindow()
        self.mainWindow_ui.setupUi(self)
        self.center()
        self.setWindowTitle("BetaFocus")
        self.setStyleSheet("background-color: black;")
        # # triangular start button
        self.start_button = self.mainWindow_ui.start_button
        self.start_button.setStyleSheet("image: url(./gui/images/start.png);"
                                        "padding-left: 30px;"
                                        "padding-top: 20px;"
                                        "padding-bottom: 50px;"
                                        "text-align: center;")
        # # statistics button at the bottom
        self.stats_button = self.mainWindow_ui.stats_button
        self.stats_button.setStyleSheet("border-style: outset;"
                                        "border-width: 2px;"
                                        "border-radius: 10px;"
                                        "border-color: white;"
                                        "min-width: 15em;")
        self.stats_button.setContentsMargins(0, 30, 0, 10)
        pic = QPixmap("./gui/images/stats.png")
        self.stats_button.setIcon(QIcon(pic))
        self.stats_button.setIconSize(QSize(20, 20))
        # # information button in the top left corner
        self.info_button = self.mainWindow_ui.info_button
        self.info_button.setStyleSheet("border-style: outset;"
                                       "border-width: 2px;"
                                       "border-radius: 10px;"
                                       "border-color: white;"
                                       "padding: 7px;")
        # # help button in the top right corner
        self.help_button = self.mainWindow_ui.help_button
        self.help_button.setStyleSheet("border-style: outset;"
                                       "border-width: 2px;"
                                       "border-radius: 15px;"
                                       "border-color: white;"
                                       "padding: 7px;")
        # # other windows are widgets and children of the main window
        self.run_window = RunWindow()

    def center(self):
        """
        centers the main window according to the desktop size of the device used
        """
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        # top left of rectangle becomes top left of window centering it
        self.move(qr.topLeft())

    @staticmethod
    def center_widget(button: QPushButton) -> QWidget:
        """
        takes the passed button and adds it the box layout of a widget which is then returned;
        enables the button to be centered within a grid layout
        """
        widget = QWidget()
        box = QVBoxLayout()
        box.setAlignment(Qt.AlignCenter)
        box.addWidget(button, stretch=1, alignment=Qt.AlignCenter)
        box.setContentsMargins(0, 60, 0, 20)
        widget.setLayout(box)
        return widget


class App(QApplication):

    def __init__(self):
        super().__init__(sys.argv)
        self.mainWindow = MainWindow()
