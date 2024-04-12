import time


class Timer:

    def __init__(self):
        self.running = False
        self.started = False

        self.passed = 0

    def start(self, time_label):
        self.running = True
        self.count(time_label)

    def stop(self):
        self.running = False

    def count(self, time_label):
        start = time.time()
        if self.started:
            until_now = self.passed
        else:
            until_now = 0
        while self.running:
            self.passed = time.time() - start + until_now
            time_label.setText(self.format_time_string(self.passed))

    def format_time_string(self, time_passed):
        secs = time_passed % 60
        mins = time_passed // 60
        hours = mins // 60
        return f"{int(hours):02d}:{int(mins):02d}:{int(secs):02d}:{int((self.passed % 1) * 100):02d}"
