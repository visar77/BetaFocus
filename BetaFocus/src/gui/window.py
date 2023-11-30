import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QGridLayout, QWidget, QPushButton, QLabel
from PyQt5.QtGui import QFont, QPainter, QColor, QPainterPath, QBrush
from PyQt5.QtCore import Qt, QRectF


class StartButton(QPushButton):
    def paintEvent(self, event):
        p = QPainter(self)
        path = QPainterPath()
        rect = QRectF(0, 0, 300, 300)

        # path.moveTo(rect.left() + (rect.width() / 2), rect.top())
        # path.lineTo(rect.bottomLeft())
        # path.lineTo(rect.bottomRight())
        # path.lineTo(rect.left() + (rect.width() / 2), rect.top())

        path.moveTo(rect.topLeft())                 # starting top left corner
        path.lineTo(rect.right(), rect.top() / 2)   # line to outer right corner
        path.lineTo(rect.bottomLeft())              # line to bottom left corner
        path.lineTo((rect.topLeft()))               # line to top left corner

        p.fillPath(path, QBrush(QColor("green")))


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.resize(1000, 600)
        self.setWindowTitle("BetaFocus")
        layout = QGridLayout()
        layout.setAlignment(Qt.AlignHCenter)
        layout.setContentsMargins(20, 20, 20, 100)
        start_font = QFont("Times New Roman", 60, QFont.Bold)

        self.start_label = QLabel("BetaFocus", self)
        self.start_label.setFont(start_font)
        layout.addWidget(self.start_label, 0, 0, 1, 2)

        self.start_button = StartButton(self)
        # self.start_button.setStyleSheet("width: 0;"
        #                                 "height: 0;"
        #                                 "border-top: 100px solid transparent;"
        #                                 "border-left: 200px solid green;"
        #                                 "border-bottom: 100px solid transparent;")
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
