import time

from PyQt5.QtWidgets import QLabel


class Timer:

    def __init__(self):
        self.running: bool = False
        self.started: bool = False
        self.passed: float = 0

    def start(self, time_label: QLabel):
        self.running = True
        self.count(time_label)

    def stop(self):
        self.running = False

    def count(self, time_label: QLabel):
        start = time.time()
        if self.started:
            until_now: float = self.passed
        else:
            until_now: float = 0
        while self.running:
            self.passed = time.time() - start + until_now
            time_label.setText(self.format_time_string(self.passed))

    def format_time_string(self, time_passed: float) -> str:
        secs: float = time_passed % 60
        mins: float = time_passed // 60
        hours: float = mins // 60
        return f"{int(hours):02d}:{int(mins):02d}:{int(secs):02d}:{int((self.passed % 1) * 100):02d}"
