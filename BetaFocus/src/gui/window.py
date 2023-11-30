import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QGridLayout, QWidget, QPushButton, QLabel
from PyQt5.QtGui import QFont, QPainter, QColor, QPainterPath, QBrush
from PyQt5.QtCore import Qt, QRectF, QPoint


class StartButton(QPushButton):

    def __int__(self):
        super().__init__()

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

        self.start_label = QLabel("BetaFocus", self)
        self.start_label.setFont(start_font)
        self.start_label.setStyleSheet("color: white;")
        layout.addWidget(self.start_label, 0, 0, 1, 2)

        self.start_button = StartButton(self)
        self.start_button.setFixedSize(300, 300)
        layout.addWidget(self.start_button, 2, 0, 1, 2)

        self.widget = QWidget()
        self.widget.setLayout(layout)
        self.setCentralWidget(self.widget)


class App(QApplication):

    def __init__(self):
        super().__init__(sys.argv)
        self.mainWindow = MainWindow()
        self.mainWindow.show()
        self.exec_()
