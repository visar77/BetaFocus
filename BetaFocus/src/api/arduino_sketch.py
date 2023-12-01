import serial.tools.list_ports
import re
from datetime import datetime, timezone


def get_available_ports():
    return sorted(serial.tools.list_ports.comports())[0]


class Arduino:

    def __init__(self, port, baudrate=9600, timeout=3):
        self.port = port
        self.baudrate = baudrate
        self.ser = serial.Serial(port, baudrate, timeout=3)
        self.timeout = timeout

    def is_open(self):
        return self.ser.is_open

    def open(self):
        self.ser.open()
        self.ser.flushInput()

    def last_package(self):
        try:
            while True:
                line = str(self.ser.readline())
                if line == "b''":  # This means readLine went to timeout
                    break
                if "CSV" in line:
                    s = re.sub("[A-Z]|[a-z]|'|\\s", "", line)
                    full_package = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S.%f') + s
                    return full_package[:-1]  # The last character is a backslash, which we don't need
        except Exception:
            print("Something went wrong!")
        return "NO PACKAGE FOUND!"

    def close(self):
        self.ser.close()

    def check_connection(self):
        ports = get_available_ports()
        for p in ports:
            if self.port in p:
                return True
        return False

    def switch_connection(self, port, baudrate=9600):
        self.port = port
        self.baudrate = baudrate
        self.ser = serial.Serial(port, baudrate)


class ArduinoConnector:

    def __init__(self, port, baudrate=9600):
        self.arduino = Arduino(port, baudrate)
        self.open = True
        self.packages = []

    def start_session(self, time_set=6):
        t1 = datetime.now().timestamp()  # timestamp when called
        self.open = self.arduino.is_open()
        if not self.open:
            print("Connection not open! Session can't be started")
        while self.open:
            package = self.arduino.last_package()
            if "NO PACKAGE FOUND!" in package:
                print("No package found, closing without saving...")
                self.open = False
                self.close()
                return
            # print(package)
            self.packages.append(package)

            if datetime.now().timestamp() - t1 >= time_set:
                self.open = False
                print("Done with session!")
                self.stop_session()

    def stop_session(self):
        with open("../../data/example.csv", "w") as f:
            for pack in self.packages:
                f.write(pack + "\n")
        self.packages = []
        self.close()

    def last_attention(self):
        pass

    def close(self):
        self.arduino.close()