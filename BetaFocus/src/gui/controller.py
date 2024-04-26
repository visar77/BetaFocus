import threading
from PyQt5.QtWidgets import QMainWindow

from .timer import Timer


class Controller:

    def __init__(self, mainWindow: QMainWindow):
        self.mainWindow = mainWindow
        self.runWindow = self.mainWindow.run_window
        # main window components
        self.start_button = self.mainWindow.start_button
        # run window components
        self.pause_button = self.runWindow.pause_button
        self.stop_button = self.runWindow.stop_button
        self.time_label = self.runWindow.time_label
        # timer
        self.timer = Timer(self.time_label)
        # add functionalities to all buttons
        self.connect()

    def connect(self):
        self.start_button.clicked.connect(self.start_session)
        self.pause_button.clicked.connect(self.timer.pause)
        self.stop_button.clicked.connect(self.stop_session)

    def start_session(self):
        """
        handles the view changes upon session start;
        launches the stopwatch in a dedicated thread
        """
        self.runWindow.show()
        self.start_button.setEnabled(False)
        threading.Thread(target=self.timer.start).start()

    def pause_session(self):
        self.timer.pause()
        self.pause_button.set_icon("./gui/images/start.png")

    def stop_session(self):
        self.runWindow.close()
        self.start_button.setEnabled(True)
        self.timer.stop()
