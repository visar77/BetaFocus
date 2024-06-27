import os
import sys
import matplotlib

matplotlib.use('Qt5Agg')

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt, QSize, pyqtSignal
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

from .ui.ui_mainwindow import Ui_MainWindow
from .ui.ui_runwindow import Ui_RunWindow
from .ui.ui_connectdialog import Ui_ConnectDialog
from .ui.ui_eval import Ui_Eval
from .ui.ui_archive import Ui_Archive


class MarkDownViewer(QWidget):

    def __init__(self, path, title):
        super().__init__()
        self.setFixedSize(920, 620)
        self.setWindowTitle(f"BetaFocus - {title}")
        self.textedit = QTextEdit()
        self.textedit.setReadOnly(True)
        self.textedit.setMarkdown(''.join(open(path).readlines()))
        layout = QGridLayout()
        layout.setAlignment(Qt.AlignHCenter)
        layout.setContentsMargins(20, 40, 20, 20)
        layout.addWidget(self.textedit, 0, 0)
        self.setLayout(layout)


class PDFViewer(QWebEngineView):
    """
    Creates a PDFViewer, which displays a PDF given a file path to it.
    """

    def __init__(self, path, title):
        """
        Creates
        :param path: relative path to view.py
        :param title: title of window, title will be "BetaFocus - {title}"
        """
        super().__init__()
        self.setFixedSize(920, 620)
        self.setWindowTitle(f"BetaFocus - {title}")
        self.setStyleSheet("background-color: black;")
        self.settings().setAttribute(self.settings().WebAttribute.PluginsEnabled, True)
        self.settings().setAttribute(self.settings().WebAttribute.PdfViewerEnabled, True)
        self.pdf_path = f'file://{"%20".join(path)}'
        self.load(QUrl(f'file://{os.path.abspath(path)}'))


class ConnectDialog(QDialog):

    def __init__(self):
        super(ConnectDialog, self).__init__()
        self.ui = Ui_ConnectDialog()
        self.ui.setupUi(self)
        self.combo_box = self.ui.combo_box

    def reject(self):
        self.hide()


class StatsWindow(QWidget):
    double_clicked = pyqtSignal(int)

    def __init__(self):
        super(StatsWindow, self).__init__()
        self.ui = Ui_Archive()
        self.ui.setupUi(self)
        self.setWindowTitle("BetaFocus - Archiv")
        # canvas
        self.plotWidget = self.ui.widget1
        # labels
        self.labels = [self.ui.label_1, self.ui.label_2, self.ui.label_3, self.ui.label_4, self.ui.label_5]
        self.labels_font = [label.font() for label in self.labels]
        # button
        self.start_button = self.ui.pushButton
        self.next_button = self.ui.next_button
        self.prev_button = self.ui.prev_button

    def mouseDoubleClickEvent(self, event):
        # Check if the widget at the mouse position is one of the labels
        child = self.childAt(event.pos())
        if child in self.labels:
            index = self.labels.index(child)
            self.double_clicked.emit(index)


class EvalWindow(QWidget):

    def __init__(self, parent=None):
        super(EvalWindow, self).__init__(parent)
        self.ui = Ui_Eval()
        self.ui.setupUi(self)
        self.setWindowTitle("BetaFocus - Auswertung")
        # top canvas
        self.plotWidget1 = self.ui.canvas_1
        # bottom canvas
        self.plotWidget2 = self.ui.canvas_2
        # labels
        self.time_label = self.ui.label_r1
        self.max_label = self.ui.label_r2
        # buttons
        self.archiv_button = self.ui.archiv_button
        self.fertig_button = self.ui.pushButton
        # line edit
        self.line_edit = self.ui.lineEdit


class RunWindow(QWidget):
    close_signal = pyqtSignal()

    def __init__(self):
        super(RunWindow, self).__init__()
        self.ui = Ui_RunWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("BetaFocus - Timer")
        # label at the top of the window
        self.label = self.ui.label
        # label that displays the time passed
        self.time_label = self.ui.time_label
        # set control buttons
        self.stop_button = self.ui.stop_button
        self.stop_button.clicked.connect(self.close)
        self.pause_button = self.ui.pause_button
        self.resume_button = self.ui.resume_button
        self.resume_button.hide()  # needs to be hidden, only shown when
        self.session_name = None

    def closeEvent(self, event):
        self.close_signal.emit()


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.center_window()
        # triangular start button
        self.start_button = self.ui.start_button
        # statistics button at the bottom right
        self.stats_button = self.ui.stats_button
        pic = QPixmap("./gui/images/stats.png")
        self.stats_button.setIcon(QIcon(pic))
        self.stats_button.setIconSize(QSize(20, 20))
        # connect button at the bottom left
        self.connect_button = self.ui.connect_button
        pic = QPixmap("./gui/images/connect.jpeg")
        self.connect_button.setIcon(QIcon(pic))
        self.connect_button.setIconSize(QSize(20, 20))
        # information button in the top left corner
        self.info_button = self.ui.info_button
        # help button in the top right corner
        self.help_button = self.ui.help_button
        # other windows are children of main window
        self.run_window = RunWindow()
        self.eval_window = EvalWindow()
        self.eval_window.hide()
        self.connect_dialog = ConnectDialog()
        self.connect_button.clicked.connect(self.connect_dialog.show)
        self.stats_window = StatsWindow()
        self.info_window = MarkDownViewer(os.path.join(os.path.dirname(os.path.dirname((os.getcwd()))), "README.md"),
                                          "Info")
        self.info_button.clicked.connect(self.info_window.show)
        self.help_window = MarkDownViewer(os.path.join(os.path.dirname(os.path.dirname((os.getcwd()))), "README.md"),
                                          "Hilfe")
        self.help_button.clicked.connect(self.help_window.show)
        self.temporary_windows = []
        self.show()

    def center_window(self):
        """
        centers the main window according to the desktop size of the device used
        """
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        # top left of rectangle becomes top left of window centering it
        self.move(qr.topLeft())

    def add_window(self, window: QWidget):
        self.temporary_windows.append(window)


class App(QApplication):

    def __init__(self):
        super().__init__(sys.argv)
        self.main_window = MainWindow()
