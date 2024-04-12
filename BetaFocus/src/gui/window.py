import sys
import threading
from PyQt5.QtWidgets import QMainWindow, QApplication, QGridLayout, QWidget, QPushButton, QLabel
from PyQt5.QtGui import QFont, QPainter, QColor, QPainterPath, QBrush, QWindow
from PyQt5.QtCore import Qt, QRectF, QPoint

from .timer import Timer


class RunWindow(QWindow):

    def __init__(self):
        super(RunWindow).__init__()
        self.resize(800, 500)
        self.setWindowTitle("BetaFocus")
        self.setStyleSheet("background-color: black;")
        layout = QGridLayout()
        layout.setAlignment(Qt.AlignHCenter)
        layout.setContentsMargins(20, 20, 20, 100)
        start_font = QFont("Times New Roman", 60, QFont.Bold)

        self.label = QLabel("You BetaFocus right now!", self)
        self.label.setFont(start_font)
        self.label.setStyleSheet("color: white;")
        self.label.setAlignment(Qt.AlignHCenter)
        layout.addWidget(self.label, 0, 1, 1, 1)

        self.time_label = QLabel("00:00:00:00", self)
        layout.addWidget(self.time_label, 1, 1, 1, 3)
        self.time_label.setAlignment(Qt.AlignHCenter)
        self.time_label.setFont(start_font)
        self.time_label.setStyleSheet("font-size:80px;")

        self.timer = Timer()

        self.widget = QWidget()
        self.widget.setLayout(layout)
        self.setCentralWidget(self.widget)

    def stopwatch(self):
        self.timer.start(self.time_label)
        self.time_label.setText(self.timer.format_time_string(self.timer.passed))

    def start_time(self):
        self.start_button.close()
        self.time_label.show()
        threading.Thread(target=self.stopwatch).start()


class StartButton(QPushButton):

    def __int__(self):
        super(StartButton).__init__()

    def paintEvent(self, event):
        p = QPainter(self)
        path = QPainterPath()
        rect = QRectF(0, 0, self.size().width(), self.size().height())
        button_font = QFont("Times New Roman", 30)

        path.moveTo(rect.topLeft())                     # starting top left corner
        path.lineTo(rect.bottomLeft())                  # line to bottom left corner
        path.lineTo(rect.width(), rect.height() / 2)    # line to outer right corner

        p.fillPath(path, QBrush(QColor("green")))
        p.setFont(button_font)
        p.setPen(QColor("white"))
        p.drawText(QPoint(int(rect.width() / 3.5), int(rect.height() / 2)), "Start")


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.resize(1000, 600)
        self.setWindowTitle("BetaFocus")
        self.setStyleSheet("background-color: black;")
        layout = QGridLayout()
        layout.setAlignment(Qt.AlignHCenter)
        layout.setContentsMargins(20, 20, 20, 100)
        start_font = QFont("Times New Roman", 60, QFont.Bold)

        self.label = QLabel("BetaFocus", self)
        self.label.setFont(start_font)
        self.label.setStyleSheet("color: white;")
        self.label.setAlignment(Qt.AlignHCenter)
        layout.addWidget(self.label, 0, 1, 1, 1)

        self.start_button = StartButton(self)
        self.start_button.setFixedSize(300, 300)
        self.start_button.clicked.connect()
        layout.addWidget(self.start_button, 1, 1, 1, 1)

        self.widget = QWidget()
        self.widget.setLayout(layout)
        self.setCentralWidget(self.widget)


class App(QApplication):

    def __init__(self):
        super().__init__(sys.argv)
        self.mainWindow = MainWindow()
        self.mainWindow.show()
        self.exec_()
