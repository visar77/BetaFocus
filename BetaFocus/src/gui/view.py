import sys
import matplotlib

matplotlib.use('Qt5Agg')

from PyQt5.QtWidgets import QMainWindow, QGridLayout, QWidget, QDesktopWidget, QApplication, QDialog
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt, QSize, pyqtSignal
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure

from .ui.ui_mainwindow import Ui_MainWindow
from .ui.ui_runwindow import Ui_RunWindow


class HelpWindow(QWidget):

    def __init__(self):
        super(HelpWindow, self).__init__()
        self.setFixedSize(920, 620)
        self.setWindowTitle("BetaFocus - Hilfe")
        self.setStyleSheet("background-color: black;")
        layout = QGridLayout()
        layout.setAlignment(Qt.AlignHCenter)
        layout.setContentsMargins(20, 40, 20, 20)


class InfoWindow(QWidget):

    def __init__(self):
        super(InfoWindow, self).__init__()
        self.setFixedSize(920, 620)
        self.setWindowTitle("BetaFocus - Info")
        self.setStyleSheet("background-color: black;")
        layout = QGridLayout()
        layout.setAlignment(Qt.AlignHCenter)
        layout.setContentsMargins(20, 40, 20, 20)


class StatsWindow(QWidget):
    def __init__(self):
        super(StatsWindow, self).__init__()
        self.setFixedSize(920, 620)
        self.setWindowTitle("BetaFocus - Archiv")
        self.setStyleSheet("background-color: black;")
        layout = QGridLayout()
        layout.setAlignment(Qt.AlignHCenter)
        layout.setContentsMargins(20, 40, 20, 20)


class ConnectDialog(QDialog):

    def __init__(self):
        super(ConnectDialog, self).__init__()
        self.setFixedSize(400, 200)
        self.setWindowTitle("BetaFocus - Verbinden")
        self.setStyleSheet("background-color: black;")
        layout = QGridLayout()
        layout.setAlignment(Qt.AlignHCenter)
        layout.setContentsMargins(20, 40, 20, 20)


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class EvalWindow(QWidget):

    def __init__(self):
        super(EvalWindow, self).__init__()
        self.setFixedSize(920, 620)
        self.setWindowTitle("BetaFocus - Auswertung")
        self.setStyleSheet("background-color: black;")
        layout = QGridLayout()
        layout.setAlignment(Qt.AlignHCenter)
        layout.setContentsMargins(20, 40, 20, 20)
        self.upper_canvas = MplCanvas(self, width=5, height=4, dpi=100)
        self.upper_canvas.axes.plot([0, 1, 2, 3, 4], [10, 1, 20, 3, 40])
        layout.addWidget(self.upper_canvas, 0, 0, 1, 1)


class RunWindow(QWidget):
    close_signal = pyqtSignal()

    def __init__(self):
        super(RunWindow, self).__init__()
        self.run_window_ui = Ui_RunWindow()
        self.run_window_ui.setupUi(self)
        self.setWindowTitle("BetaFocus - Timer")
        # label at the top of the window
        self.label = self.run_window_ui.label
        # label that displays the time passed
        self.time_label = self.run_window_ui.time_label
        # set control buttons
        self.stop_button = self.run_window_ui.stop_button
        self.stop_button.clicked.connect(self.close)
        self.pause_button = self.run_window_ui.pause_button
        self.resume_button = self.run_window_ui.resume_button
        self.resume_button.hide()  # needs to be hidden, only shown when

    def closeEvent(self, a0):
        self.close_signal.emit()


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.main_window_ui = Ui_MainWindow()
        self.main_window_ui.setupUi(self)
        self.center()
        # triangular start button
        self.start_button = self.main_window_ui.start_button
        # statistics button at the bottom right
        self.stats_button = self.main_window_ui.stats_button
        pic = QPixmap("./gui/images/stats.png")
        self.stats_button.setIcon(QIcon(pic))
        self.stats_button.setIconSize(QSize(20, 20))
        # connect button at the bottom left
        self.connect_button = self.main_window_ui.connect_button
        pic = QPixmap("./gui/images/connect.jpeg")
        self.connect_button.setIcon(QIcon(pic))
        self.connect_button.setIconSize(QSize(20, 20))
        # information button in the top left corner
        self.info_button = self.main_window_ui.info_button
        # help button in the top right corner
        self.help_button = self.main_window_ui.help_button
        # other windows are children of main window
        self.run_window = RunWindow()
        self.eval_window = EvalWindow()
        self.connect_dialog = ConnectDialog()
        self.connect_button.clicked.connect(self.connect_dialog.show)
        self.stats_window = StatsWindow()
        self.stats_button.clicked.connect(self.stats_window.show)
        self.info_window = InfoWindow()
        self.info_button.clicked.connect(self.info_window.show)
        self.help_window = HelpWindow()
        self.help_button.clicked.connect(self.help_window.show)
        self.show()

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
        self.main_window = MainWindow()
