from threading import Thread
from PyQt5.QtWidgets import QMainWindow

from .timer import Timer
from api.microcontroller import MCConnector
from .data import Archive, Session


class Controller:

    def __init__(self, main_window: QMainWindow):
        # MicroController-Controller

        # Lass erstmal so stehen, kümmern uns später dann zusammen, wie man das richtig umsetzt
        # Habe ein try und catch hinzugefügt, damit Programm nicht abstürzt, wenn wir später den Port über
        # die GUI definieren, wird das alles klappen und die try und catches werden mit was anderem ersetzt
        port = 'COM5'
        try:
            self.mc_connector = MCConnector(port, 9600)
        except Exception as e:
            pass

        # windows
        self.main_window = main_window
        self.run_window = self.main_window.run_window
        self.eval_window = self.main_window.eval_window
        self.connect_dialog = self.main_window.connect_dialog
        self.stats_window = self.main_window.stats_window
        # timer
        self.timer = Timer(self.run_window.time_label)
        self.timer_thread = Thread(target=self.timer.count)
        # data
        self.archive = Archive()
        self.session = Session()
        # add functionalities to all buttons
        self.connect()

    def connect(self):
        self.main_window.start_button.clicked.connect(self.start_session)
        self.run_window.pause_button.clicked.connect(self.pause_session)
        self.run_window.resume_button.clicked.connect(self.resume_session)
        self.run_window.close_signal.connect(self.stop_session)

    def start_session(self):
        """
        handles the view changes upon session start;
        launches the stopwatch in a dedicated thread
        """
        self.run_window.show()
        self.main_window.start_button.setEnabled(False)
        self.timer.start()
        if not self.timer_thread.is_alive():
            self.timer_thread = Thread(target=self.timer.count)
        print(self.timer_thread.name)
        self.timer_thread.start()
        # Später können wir die try und catches entfernen, wenn mc_connector den richtigen Port bekommt
        try:
            self.mc_connector.start_session()
        except Exception as e:
            pass

    def pause_session(self):
        self.timer.pause()
        self.run_window.pause_button.hide()
        self.run_window.resume_button.show()
        try:
            self.mc_connector.pause_session()
        except Exception as e:
            pass

    def resume_session(self):
        self.timer.resume()
        self.run_window.resume_button.hide()
        self.run_window.pause_button.show()
        try:
            self.mc_connector.resume_session()
        except Exception as e:
            pass

    def stop_session(self):
        # Reset state of run buttons
        self.run_window.resume_button.hide()
        self.run_window.pause_button.show()

        self.eval_window.show()
        self.main_window.start_button.setEnabled(True)
        self.timer.stop()
        try:
            self.session.set_path(self.mc_connector.stop_session())
        except Exception as e:
            pass
