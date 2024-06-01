import threading

from PyQt5.QtWidgets import QMainWindow

from threading import Thread

from .timer import Timer


class Controller:

    def __init__(self, mainWindow: QMainWindow):
        # main window components
        self.mainWindow = mainWindow
        self.start_button = self.mainWindow.start_button
        self.stats_button = self.mainWindow.stats_button
        self.connect_button = self.mainWindow.connect_button
        self.info_button = self.mainWindow.info_button
        self.help_button = self.mainWindow.help_button
        # run window components
        self.runWindow = self.mainWindow.run_window
        self.stop_button = self.runWindow.stop_button
        self.pause_button = self.runWindow.pause_button
        self.resume_button = self.runWindow.resume_button
        self.time_label = self.runWindow.time_label
        # timer
        self.timer = Timer(self.time_label)
        # evaluation window
        self.evalWindow = self.mainWindow.eval_window
        # stats window
        self.statsWindow = self.mainWindow.stats_window
        # connection dialog
        self.connectDialog = self.mainWindow.connect_dialog
        # info window
        self.infoWindow = self.mainWindow.info_window
        # window
        self.helpWindow = self.mainWindow.help_window
        # add functionalities to all buttons
        self.connect()
        self.timer_thread = Thread(target=self.timer.count)

    def connect(self):
        self.start_button.clicked.connect(self.start_session)
        self.stats_button.clicked.connect(self.show_stats)
        self.connect_button.clicked.connect(self.show_dialog)
        self.info_button.clicked.connect(self.show_info)
        self.help_button.clicked.connect(self.show_help)
        self.pause_button.clicked.connect(self.pause_session)
        self.resume_button.clicked.connect(self.resume_session)
        self.stop_button.clicked.connect(self.runWindow.close)
        self.runWindow.close_signal.connect(self.stop_session)

    def start_session(self):
        """
        handles the view changes upon session start;
        launches the stopwatch in a dedicated thread
        """
        self.runWindow.show()
        self.start_button.setEnabled(False)
        self.timer.start()
        self.timer_thread.start()

    def show_stats(self):
        self.statsWindow.show()

    def show_dialog(self):
        self.connectDialog.show()

    def show_info(self):
        self.infoWindow.show()

    def show_help(self):
        self.helpWindow.show()

    def pause_session(self):
        self.timer.pause()
        self.pause_button.hide()
        self.resume_button.show()

    def resume_session(self):
        self.timer.resume()
        self.resume_button.hide()
        self.pause_button.show()

    def stop_session(self):
        # Reset state of run buttons
        self.resume_button.hide()
        self.pause_button.show()

        self.evalWindow.show()
        self.start_button.setEnabled(True)
        self.timer.stop()
