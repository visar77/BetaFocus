from threading import Thread

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox

from api.microcontroller import *
from .data import Archive, Session
from .timer import Timer
from .view import MainWindow


class Controller:

    def __init__(self, main_window: MainWindow):
        # MicroController-Controller

        self.port = None
        self.mc_connector = None

        # windows
        self.main_window = main_window
        self.run_window = self.main_window.run_window
        self.eval_window = self.main_window.eval_window
        self.connect_dialog = self.main_window.connect_dialog
        self.connect_dialog_button = self.main_window.connect_button
        self.stats_window = self.main_window.stats_window

        # timer
        self.timer = Timer(self.run_window.time_label)
        self.timer_thread = Thread(target=self.timer.count)

        self.session_thread = None

        # error message box
        self.error_message_box = QMessageBox(parent=self.main_window)
        self.error_message_box.setWindowTitle("BetaFocus - Fehlermeldung")
        self.error_message_box.setIcon(QMessageBox.Critical)
        self.error_message_box.setStyleSheet("color: white")

        # data
        self.archive = Archive()
        self.session = Session()
        # add functionalities to all buttons
        self.connect()

    def connect(self):
        self.connect_dialog.accepted.connect(self.set_microcontroller)
        self.connect_dialog_button.clicked.connect(self.insert_ports_to_combobox)
        self.main_window.start_button.clicked.connect(self.start_session)
        self.run_window.pause_button.clicked.connect(self.pause_session)
        self.run_window.resume_button.clicked.connect(self.resume_session)
        self.run_window.close_signal.connect(self.stop_session)

    def start_session(self):
        """
        handles the view changes upon session start launches the stopwatch in a dedicated thread and the
        reading of values of the controller in another thread.
        """
        if self.mc_connector is None:
            if self.port is None:
                self.error_message_box.setText(
                    "Session kann nicht gestartet werden, da kein Port ausgewählt wurde. Wähle bitte einen Port im Verbindungsfenster aus.")
                self.error_message_box.show()
            else:
                try:
                    self.main_window.setCursor(Qt.WaitCursor)
                    self.mc_connector = MCConnector(self.port)
                    self.main_window.setCursor(Qt.ArrowCursor)
                except Exception as e:
                    self.main_window.setCursor(Qt.ArrowCursor)
                    self.error_message_box.setText(
                        "Session kann nicht gestartet werden, da keine serielle Verbindung mit dem Port kreiert werden kann, wähle einen gültigen Port im Verbindungsfenster aus.")
                    self.error_message_box.show()
            return

        self.run_window.show()
        self.main_window.start_button.setEnabled(False)
        self.timer.start()
        if not self.timer_thread.is_alive():
            self.timer_thread = Thread(target=self.timer.count)

        if self.session_thread is None or not self.session_thread.is_alive():
            self.session_thread = Thread(target=self.mc_connector.start_session)

        self.timer_thread.start()
        self.session_thread.start()

    def pause_session(self):
        self.timer.pause()
        self.mc_connector.pause_session()
        self.run_window.pause_button.hide()
        self.run_window.resume_button.show()

    def resume_session(self):
        self.timer.resume()
        self.mc_connector.resume_session()
        self.run_window.resume_button.hide()
        self.run_window.pause_button.show()

    def stop_session(self):
        # Reset state of run buttons
        self.run_window.resume_button.hide()
        self.run_window.pause_button.show()

        self.main_window.start_button.setEnabled(True)
        self.timer.stop()
        self.mc_connector.stop_session()
        self.session.set_path(self.mc_connector.last_session_path())
        self.eval_window.show()

    def set_microcontroller(self):
        self.port = self.connect_dialog.combo_box.currentText()
        try:
            self.connect_dialog.setCursor(Qt.WaitCursor)
            self.mc_connector = MCConnector(self.port)
            self.connect_dialog.setCursor(Qt.ArrowCursor)
        except Exception as e:
            self.connect_dialog.setCursor(Qt.ArrowCursor)
            self.error_message_box.setText(
                "Session kann nicht gestartet werden, da keine serielle Verbindung mit dem Port kreiert werden kann, wähle einen gültigen Port im Verbindungsfenster aus.")
            self.error_message_box.show()

    def insert_ports_to_combobox(self):
        combo_box = self.connect_dialog.combo_box
        combo_box.clear()
        combo_box.addItems(MicroController.get_available_ports())
