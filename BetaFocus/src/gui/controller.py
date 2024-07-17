import re
from threading import Thread
import time

import numpy as np
import pyqtgraph
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtWidgets import QMessageBox, QLabel

from api.microcontroller import MCConnector
from .data import Archive
from .view import MainWindow, EvalWindow


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

        # data
        self.archive = Archive()
        self.archive_page = 1
        # add functionalities to all buttons
        self.connect_elements()

    def connect_elements(self):
        """
        Connects all buttons and dialogs to their respective functions.
        :return:
        """
        self.connect_dialog.accepted.connect(self.set_microcontroller)
        self.connect_dialog_button.clicked.connect(self.insert_ports_to_combobox)
        self.main_window.start_button.clicked.connect(self.start_session)
        self.run_window.pause_button.clicked.connect(self.pause_session)
        self.run_window.resume_button.clicked.connect(self.resume_session)
        self.run_window.close_signal.connect(self.stop_session)
        self.eval_window.archiv_button.clicked.connect(lambda state, x=True, y=True: self.prepare_archive_window(x, y))
        self.main_window.stats_button.clicked.connect(lambda state, x=True, y=True: self.prepare_archive_window(x, y))
        self.stats_window.start_button.clicked.connect(self.start_session)
        self.stats_window.next_button.clicked.connect(self.get_next_five_sessions)
        self.stats_window.prev_button.clicked.connect(self.get_prev_five_sessions)
        self.stats_window.double_clicked.connect(self.create_eval_window)

    def start_session(self):
        """
        handles the view changes upon session start launches the stopwatch in a dedicated thread and the
        reading of values of the controller in another thread.
        """
        if self.mc_connector is None:
            if self.port is None:
                self.create_error_message_box("Bitte wähle einen gültigen Port im Verbindungsfenster aus.",
                                              self.main_window)
            else:
                try:
                    self.main_window.setCursor(Qt.WaitCursor)
                    self.mc_connector = MCConnector(self.port)
                    self.main_window.setCursor(Qt.ArrowCursor)
                except Exception as e:
                    self.main_window.setCursor(Qt.ArrowCursor)
                    self.create_error_message_box(
                        "Session kann nicht gestartet werden, da keine serielle Verbindung mit dem Port kreiert werden kann, wähle einen gültigen Port im Verbindungsfenster aus.",
                        self.main_window)
            return

        self.run_window.show()
        self.eval_window.close()
        self.stats_window.close()
        self.main_window.start_button.setEnabled(False)
        self.timer.start()
        if not self.timer_thread.is_alive():
            self.timer_thread = Thread(target=self.timer.count)

        if self.session_thread is None or self.session_thread.isFinished():
            self.session_thread = SessionThread(self)
            self.session_thread.session_stopped.connect(self.handle_start_session_error)

        self.timer_thread.start()
        self.session_thread.start()

    def handle_start_session_error(self, result):
        self.stop_session()

        if result == -3:
            error_text = "Die Verbindung gibt keine gültige Daten zurück, bitte wähle den richtigen Port aus"
        elif result == -2:
            error_text = "Session konnte nicht gestartet werden, da die serielle Verbindung nicht geöffnet werden kann. Bitte versuche es später erneut oder wähle anderne Port aus."
        elif result == -1:
            error_text = "Session wurde beendet, weil es zu einem Fehler beim Lesen der Daten kam."
        elif result == 0:
            error_text = "Session wurde beendet, weil es zu einem Timeout von mehr als 10 s kam. Oder die Verbindung hat keine Pakete gesendet (= Leere Session). Session wurde gespeichert, falls nicht leer."
        else:
            error_text = "No idea how you got here"

        self.create_error_message_box(error_text, self.main_window)

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
        result = self.mc_connector.stop_session()
        if result == -1:
            # Session already closed or not started, ignore call
            self.timer.stop()

            # Reset state of run buttons
            self.run_window.resume_button.hide()
            self.run_window.pause_button.show()
            self.run_window.hide()
            self.main_window.start_button.setEnabled(True)
            self.eval_window.time_label.setText(self.timer.get_format_time_string())
            return

        if result == 0:
            self.create_error_message_box(
                "Session konnte nicht gestoppt werden, da die serielle Verbindung nicht geschlossen werden kann. Bitte versuche es später erneut.",
                self.run_window)
            return

        self.timer.stop()

        # Reset state of run buttons
        self.run_window.resume_button.hide()
        self.run_window.pause_button.show()
        self.run_window.hide()

        self.main_window.start_button.setEnabled(True)
        self.eval_window.time_label.setText(self.timer.get_format_time_string())
        self.prepare_eval_window(self.mc_connector.last_session_name())
        self.prepare_archive_window(reset_plot=True, show=False)

    def set_microcontroller(self):
        self.port = self.connect_dialog.combo_box.currentText()
        try:
            self.connect_dialog.setCursor(Qt.WaitCursor)
            self.mc_connector = MCConnector(self.port)
            self.connect_dialog.setCursor(Qt.ArrowCursor)
        except Exception as e:
            print(e)
            self.connect_dialog.setCursor(Qt.ArrowCursor)
            self.create_error_message_box(
                "Session kann nicht gestartet werden, da keine serielle Verbindung mit dem Port kreiert werden kann, wähle einen gültigen Port im Verbindungsfenster aus.",
                self.main_window)

    def insert_ports_to_combobox(self):
        combo_box = self.connect_dialog.combo_box
        combo_box.clear()
        combo_box.addItems(MCConnector.get_available_ports())

    def create_eval_window(self, index):
        if self.stats_window.labels[index].text() == "-":
            self.create_error_message_box("Diese Session gibt es nicht!", self.stats_window)
            return
        session_name, _ = self.stats_window.labels[index].text().split(" ")
        self.prepare_eval_window(session_name, reload_archive=True, new_window=True)

    def prepare_eval_window(self, session_name, reload_archive=False, new_window=False):
        if reload_archive:
            self.archive.init_data()

        if new_window:
            eval_window = EvalWindow()
            eval_window.setWindowTitle(f"BetaFocus - Auswertung von {session_name}")
            eval_window.archiv_button.hide()
            self.main_window.add_window(eval_window)

        else:
            eval_window = self.eval_window

        eval_window.session_name = session_name
        eval_window.fertig_button.clicked.connect(lambda: self.submit_session_name(eval_window))
        session = self.archive.get_session(session_name)

        total_time = 0
        timestamps = session.data['TIMERTIME'].values.tolist()
        attentions = session.data['ATTENTION'].values.tolist()

        for i in range(1, len(attentions)):
            if attentions[i] > 40:
                total_time += timestamps[i] - timestamps[i - 1]

        hours = total_time // 3600
        total_time %= 3600
        minutes = total_time // 60
        seconds = total_time % 60

        eval_window.time_label.setText(f"{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}")

        red_pen = pyqtgraph.mkPen(color=(255, 0, 0), style=Qt.DashLine)
        green_pen = pyqtgraph.mkPen(color=(0, 128, 0), style=Qt.DashLine)

        eval_window.plotWidget1.plotItem.clear()
        eval_window.plotWidget2.plotItem.clear()

        # Infinite dashed lines
        inf_line1 = pyqtgraph.InfiniteLine(pos=(0, session.get_lower()), angle=0, movable=False, pen=red_pen)
        inf_line2 = pyqtgraph.InfiniteLine(pos=(0, session.get_upper()), angle=0, movable=False, pen=green_pen)

        inf_line3 = pyqtgraph.InfiniteLine(pos=(0, session.get_lower()), angle=0, movable=False, pen=red_pen)
        inf_line4 = pyqtgraph.InfiniteLine(pos=(0, session.get_upper()), angle=0, movable=False, pen=green_pen)

        # top canvas
        x = session.get_x_vals()
        y = session.get_y_vals()
        eval_window.plotWidget1.addLegend(offset=8)

        # Calculate the linear regression line
        if len(x) == 0 or len(y) == 0:
            poly1d_fn = lambda x: np.zeros_like(x)
        else:
            coef = np.polyfit(x, y, 1)
            poly1d_fn = np.poly1d(coef)

        eval_window.plotWidget1.plot(x, y)
        eval_window.plotWidget1.plot(x, poly1d_fn(x), pen=pyqtgraph.mkPen(color=(0, 255, 0), width=2), name="Regressionsgerade")

        eval_window.plotWidget1.addItem(inf_line1, ignoreBounds=False)
        eval_window.plotWidget1.addItem(inf_line2, ignoreBounds=False)
        eval_window.plotWidget1.plotItem.autoRange()
        eval_window.plotWidget1.plotItem.getViewBox().setLimits(yMin=-20, yMax=120)

        # bottom canvas
        eval_window.plotWidget2.plot(self.archive.get_x_data(), self.archive.get_mean_vals(), symbol='x')
        eval_window.plotWidget2.addItem(inf_line3, ignoreBounds=False)
        eval_window.plotWidget2.addItem(inf_line4, ignoreBounds=False)
        eval_window.plotWidget2.plotItem.autoRange()
        eval_window.plotWidget2.plotItem.getViewBox().setLimits(yMin=-20, yMax=120)

        eval_window.max_label.setText(str(session.get_max()))
        eval_window.show()

    def submit_session_name(self, eval_window):
        session_name = eval_window.session_name

        if len(eval_window.line_edit.text()) > 0:
            new_session_name = eval_window.line_edit.text()

            # Check if the name is already taken
            if self.archive.get_session(new_session_name) is not None:
                self.create_error_message_box("Eine Session mit dem Namen gibt es schon!!", eval_window)
                return

            # Check if the name is a valid file name and does not contain spaces
            if re.match(r'^[\w\-.]+$', new_session_name) is not None:
                eval_window.line_edit.setText("")
                self.archive.set_session_name(session_name, new_session_name)
                self.prepare_eval_window(new_session_name, reload_archive=False, new_window=True)
                self.prepare_archive_window(reset_plot=True)
                eval_window.close()
            else:
                # Display an error message if the name is not valid
                self.create_error_message_box("Der Session-Name darf keine Leerzeichen oder illegale Sonderzeichen enthalten.", eval_window)

    def prepare_archive_window(self, reset_plot=True, show=True):
        if not self.archive.sessions_csv_created():
            self.create_error_message_box(
                "Es sind keine Sessions vorhanden, da noch keine Sessions aufgezeichnet wurden. Drücke auf dem grünen Knopf und starte deine erste Session!",
                self.main_window)
            return

        # Enable and disable buttons
        total_pages = (self.archive.get_num_of_sessions() + 4) // 5  # Calculate total pages

        if self.archive_page == 1:  # If this is the first page, hide the prev button
            self.stats_window.prev_button.hide()
        else:
            self.stats_window.prev_button.show()  # Show the prev button as there are previous pages

        if self.archive_page == total_pages:  # If this is the last page, hide the next button
            self.stats_window.next_button.hide()
        else:
            self.stats_window.next_button.show()  # Show the next button as there are next pages

        sessions = self.archive.get_names_of_five_sessions(self.archive_page)

        if len(sessions) < 5:
            for _ in range(5 - len(sessions)):
                sessions.append("-")
        for i in range(5):
            if len(sessions[i]) > 25:
                if len(sessions[i]) > 35:
                    self.stats_window.labels_font[i].setPointSize(8)
                self.stats_window.labels_font[i].setPointSize(12)
            else:
                self.stats_window.labels_font[i].setPointSize(20)
            self.stats_window.labels[i].setFont(self.stats_window.labels_font[i])
            self.stats_window.labels[i].setText(sessions[i])

        if reset_plot:
            self.stats_window.plotWidget.plotItem.clear()
            self.archive.init_data()
            self.stats_window.plotWidget.addLegend()

            x = self.archive.get_x_data()
            y = self.archive.get_y_data()

            self.stats_window.plotWidget.plot(x, y, symbol='x')

            # Calculate the linear regression line
            coef = np.polyfit(x, y, 1)
            poly1d_fn = np.poly1d(coef)
            self.stats_window.plotWidget.plot(x, poly1d_fn(x), pen=pyqtgraph.mkPen(color=(0, 255, 0), width=2), name="Regressionsgerade")

            self.stats_window.update()
            if show:
                self.stats_window.show()

    def get_next_five_sessions(self):
        total_pages = (self.archive.get_num_of_sessions() + 4) // 5  # Calculate total pages
        if self.archive_page < total_pages:  # Check if there are more pages
            self.archive_page += 1
            if self.archive_page == total_pages:  # If this is the last page, hide the next button
                self.stats_window.next_button.hide()
            self.stats_window.prev_button.show()  # Show the previous button as there are previous pages
            self.prepare_archive_window(reset_plot=False)  # Update the window with the new set of sessions
        else:
            self.stats_window.next_button.hide()  # If there are no more pages, hide the next button

    def get_prev_five_sessions(self):
        if self.archive_page > 1:  # Check if there are previous pages
            self.archive_page -= 1
            if self.archive_page == 1:  # If this is the first page, hide the prev button
                self.stats_window.prev_button.hide()
            self.stats_window.next_button.show()  # Show the next button as there are next pages
            self.prepare_archive_window(reset_plot=False)  # Update the window with the new set of sessions
        else:
            self.stats_window.prev_button.hide()  # If there are no more previous pages, hide the prev button

    @staticmethod
    def create_error_message_box(text, parent):
        error_message_box = QMessageBox(parent=parent)
        error_message_box.setWindowTitle("BetaFocus - Fehlermeldung")
        error_message_box.setIcon(QMessageBox.Critical)
        error_message_box.setStyleSheet("color: white")
        error_message_box.setText(text)
        error_message_box.show()


class Timer:

    def __init__(self, time_label: QLabel):
        self.running: bool = False
        self.started: bool = False
        self.stopped: bool = False
        self.passed: float = 0
        self.time_label = time_label

    def start(self):
        self.running = True
        self.started = True
        self.stopped = False

    def pause(self):
        self.running = False

    def resume(self):
        self.running = True

    def stop(self):
        self.pause()
        self.stopped = True
        self.started = False
        self.passed = 0

    def count(self):
        while not self.stopped:
            start = time.monotonic()
            if self.started:
                until_now: float = self.passed
            else:
                until_now: float = 0
            while self.running:
                self.passed = time.monotonic() - start + until_now
                self.time_label.setText(self.get_format_time_string())
        self.passed = 0

    def get_format_time_string(self) -> str:
        secs: float = self.passed % 60
        mins: float = self.passed // 60
        hours: float = mins // 60
        return f"{int(hours):02d}:{int(mins):02d}:{int(secs):02d}"


class SessionThread(QThread):
    session_stopped = pyqtSignal(int)

    def __init__(self, controller):
        QThread.__init__(self)
        self.controller = controller

    def run(self):
        result = self.controller.mc_connector.start_session()
        if result != 1:
            self.session_stopped.emit(result)
