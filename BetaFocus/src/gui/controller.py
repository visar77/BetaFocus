import sys
import threading

from PyQt5.QtWidgets import QApplication

from .view import MainWindow
from .timer import Timer


class App(QApplication):

    def __init__(self):
        super().__init__(sys.argv)
        self.mainWindow = MainWindow()
        self.runWindow = self.mainWindow.run_window
        self.mainWindow.show()
        # main window components
        self.start_button = self.mainWindow.start_button
        self.start_button.clicked.connect(self.start_session)
        # run window components
        self.time_label = self.runWindow.time_label
        self.timer = Timer()
        # run gui
        self.exec_()

    def stopwatch(self):
        """
        starts the actual timer;
        gives stopwatch functionality to the time label of the run window
        """
        self.timer.start(self.time_label)
        self.time_label.setText(self.timer.format_time_string(self.timer.passed))

    def start_session(self):
        """
        handles the view changes upon session start;
        launches the stopwatch in a dedicated thread
        """
        self.runWindow.show()
        self.start_button.setEnabled(False)
        threading.Thread(target=self.stopwatch).start()
