import threading
from PyQt5.QtWidgets import QMainWindow

from .timer import Timer


class Controller:

    def __init__(self, mainWindow: QMainWindow):
        # main window components
        self.mainWindow = mainWindow
        self.start_button = self.mainWindow.start_button
        self.stats_button = self.mainWindow.stats_button
        # run window components
        self.runWindow = self.mainWindow.run_window
        self.stop_button = self.runWindow.stop_button
        self.pause_button = self.runWindow.pause_button
        self.resume_button = self.runWindow.resume_button
        self.time_label = self.runWindow.time_label
        # timer
        self.timer = Timer(self.time_label)
        # stats window
        self.statsWindow = self.mainWindow.stats_window
        # add functionalities to all buttons
        self.connect()

    def connect(self):
        self.start_button.clicked.connect(self.start_session)
        self.stats_button.clicked.connect(self.show_stats)
        self.pause_button.clicked.connect(self.pause_session)
        self.resume_button.clicked.connect(self.resume_session)
        self.stop_button.clicked.connect(self.stop_session)

    def start_session(self):
        """
        handles the view changes upon session start;
        launches the stopwatch in a dedicated thread
        """
        self.runWindow.show()
        self.start_button.setEnabled(False)
        threading.Thread(target=self.timer.start).start()

    def show_stats(self):
        self.statsWindow.show()

    def pause_session(self):
        self.timer.pause()
        self.pause_button.hide()
        self.resume_button.show()

    def resume_session(self):
        self.start_button.setEnabled(False)
        threading.Thread(target=self.timer.start).start()
        self.resume_button.hide()
        self.pause_button.show()

    def stop_session(self):
        self.resume_button.hide()
        self.pause_button.show()
        self.runWindow.close()
        self.start_button.setEnabled(True)
        self.timer.stop()
