import time

from PyQt5.QtWidgets import QLabel


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
                self.time_label.setText(self.format_time_string())
        self.passed = 0

    def format_time_string(self) -> str:
        secs: float = self.passed % 60
        mins: float = self.passed // 60
        hours: float = mins // 60
        return f"{int(hours):02d}:{int(mins):02d}:{int(secs):02d}:{int((self.passed % 1) * 100):02d}"
