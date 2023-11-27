import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QGridLayout, QWidget


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
<<<<<<< HEAD
        self.resize(1000, 550)
=======
        self.resize(1200, 750)
>>>>>>> b267fd746a1aeb028a84342307243ac8a63efa14
        self.setWindowTitle("BetaFocus")
        self.layout = QGridLayout(self)

        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)


class App(QApplication):

    def __init__(self):
        super().__init__(sys.argv)
        self.mainWindow = MainWindow()
        self.mainWindow.show()
        self.exec_()
        