import os
import time
from datetime import datetime, timezone

import serial.tools.list_ports


class Arduino:

    def __init__(self, port, baudrate=9600, timeout=3.0):
        self.__port = port
        self.__baudrate = baudrate
        self.__ser = serial.Serial(port, baudrate, timeout=3.0)
        self.__timeout = timeout

    def is_open(self):
        return self.__ser.is_open

    def open(self):
        self.__ser.open()
        self.__ser.flushInput()

    def last_package(self):
        while True:
            line = str(self.__ser.readline())
            if line == "b''" or line == '':  # This means readLine went to timeout
                break
            if "CSV" in line:
                s = line[7:-3]
                full_package = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S.%f') + ";" + s
                return full_package

        return None

    def close(self):
        self.__ser.close()

    def check_connection(self):
        ports = self.get_available_ports()
        for p in ports:
            if self.__port in p:
                return True
        return False

    def switch_connection(self, port, baudrate=9600):
        self.__port = port
        self.__baudrate = baudrate
        self.__ser = serial.Serial(port, baudrate)

    @staticmethod
    def get_available_ports():
        return sorted(serial.tools.list_ports.comports())[0]


class ArduinoConnector:

    def __init__(self, port, baudrate=9600):
        self.__arduino = Arduino(port, baudrate)
        self.open = True
        self.__packages = []

    def start_session(self, time_set=6.0, path=None):
        date = datetime.now().strftime("%y-%m-%d_%H-%M-%S-%f")
        file_name = rf"session_{date}.csv"
        if path is None:
            path = "../../data"
        path = os.path.join(path, file_name)
        t0 = time.monotonic()
        self.open = self.__arduino.is_open()
        if not self.open:
            print("Connection not open! Session can't be started")

        while self.open:
            package = self.__arduino.last_package()
            if package is None:
                print("No package found, closing without saving...")
                self.open = False
                self.close()
                return
            # print(package)
            self.__packages.append(package)

            if time.monotonic() - t0 >= time_set:
                self.open = False
                print("Done with session!")
                self.stop_session(path, file_name)

    def stop_session(self, path: str, file_name: str = None):
        # Write a session csv
        with open(path, "w+") as f:
            f.write("DATE;POOR_SIGNAL_QUALITY;ATTENTION;MEDITATION;DELTA;THETA;LOW ALPHA;HIGH ALPHA;LOW BETA;HIGH BETA;LOW GAMMA; HIGH GAMMA;RAW WAVE DATA\n")
            for pack in self.__packages:
                f.write(pack + "\n")

        # Add to sessions.csv or create session.csv

        if not os.path.isfile("../../data/sessions.csv"):
            with open("../../data/sessions.csv", "w+") as f:
                f.write("INDEX;DATE;FILE_NAME;DATE_OF_FIRST_PACKAGE;DATE_OF_LAST_PACKAGE\n")

        with open("../../data/sessions.csv", "r+") as f:
            index = f.readlines()[-1].split(";")[0]
            if index == "INDEX":
                index = 0
            else:
                index = int(index) + 1

        with open("../../data/sessions.csv", "a+") as f:
            date = file_name[8:-4]   # cutting session_ and .csv out
            date_of_first_package = self.__packages[0].split(";")[0]
            date_of_last_package = self.__packages[-1].split(";")[0]
            f.write(f"{index};{date};{file_name};{date_of_first_package};{date_of_last_package}\n")

        self.__packages = []
        self.close()

    def close(self):
        self.__arduino.close()
