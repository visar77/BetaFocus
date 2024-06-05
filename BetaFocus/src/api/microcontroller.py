import glob
import os
import sys
import time
from os.path import dirname as up_dir
from datetime import datetime, timezone

import serial.tools.list_ports


class MicroController:
    """
    Represents the MicroController.
    """

    def __init__(self, port, baudrate=9600, timeout=10.0):
        """
        Creates serial connection with serial library.
        :param port: serial port
        :param baudrate: serial baudrate (default: 9600)
        :param timeout: seconds after a timeout sets in (timeout: 10 seconds)
        """
        self.__port = port
        self.__baudrate = baudrate
        self.__ser = serial.Serial(port, baudrate, timeout=timeout)
        self.__timeout = timeout

    def is_open(self):
        """
        Checks if serial connection is open
        :return: boolean, true or false
        """
        return self.__ser.is_open

    def open(self):
        """
        Opens serial connection and flushes input
        :return:
        """
        self.__ser.open()
        self.__ser.flushInput()

    def last_package(self):
        """
        Reads the last package from the serial connection.
        :return: string, the last package in CSV format OR None if no package was found
        """
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
        """
        Closes the serial connection
        :return:
        """
        self.__ser.close()

    def check_connection(self):
        """
        Checks if the connection is still available
        :return:
        """
        ports = self.get_available_ports()
        for p in ports:
            if self.__port in p:
                return True
        return False

    def switch_connection(self, port, baudrate=9600):
        """
        Switches the connection to another port
        :param port: serial port
        :param baudrate: new baudrate (default: 9600)
        :return:
        """
        self.__port = port
        self.__baudrate = baudrate
        self.__ser = serial.Serial(port, baudrate)

    @staticmethod
    def get_available_ports():
        """
        Returns a list of available ports
        :raises EnvironmentError: Unsupported or unknown platform
        :return: list of available ports
        """
        ports = [str(x) for x in sorted(serial.tools.list_ports.comports())]

        cut_ports = []
        for p in ports:
            if sys.platform.startswith('win'):
                p = p.split(" - ")[0]
            elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
                p = p.split(" ")[0]
            elif sys.platform.startswith("darwin"):
                p = p.split(" ")[0]
            else:
                raise EnvironmentError('Unsupported platform')
            cut_ports.append(p)

        return cut_ports


class MCConnector:
    """
    Represents the MicroController Connector. This class is used to start and stop a session. It also handles the
    pausing and resuming of a session. Sessions are saved in the data folder with the format
    session_yy-mm-dd_hh-mm-ss-fff.csv.
    """

    def __init__(self, port, baudrate=9600):
        """
        Creates a MicroController Connector.
        :param port: serial port
        :param baudrate: baudrate (default: 9600)
        """
        self.__arduino = MicroController(port, baudrate)
        self.open = self.__arduino.is_open()
        self.__packages = []
        self.__pause = False
        self.timer_start = None
        self.paused_time = 0
        self.session_date = None

    def start_session(self):
        """
        Starts a session and logs the data in a list.
        :return:
        """
        self.session_date = datetime.now().strftime("%y-%m-%d_%H-%M-%S-%f")

        self.timer_start = time.monotonic()
        self.open = self.__arduino.is_open()

        if not self.open:
            print("Connection not open! Session can't be started")

        while self.open:
            package = self.__arduino.last_package()

            if self.__pause:
                print("Pausing")
                continue

            if package is None:
                print("No package found")
                package = ";;;;;;;;;;;;"

            package = str(self.paused_time + time.monotonic() - self.timer_start) + ";" + package
            print("package received: ", package)
            self.__packages.append(package)

        print("Session stopped")

    def stop_session(self):
        """
        Stops the session and writes the data to a csv file.
        :return: path to csv file as string
        """
        self.close()  # Close the connection and stops the session logging done by start_session

        path = os.path.join(up_dir(up_dir(up_dir(os.path.realpath(__file__)))), "data")
        file_name = rf"session_{self.session_date}.csv"
        path = os.path.join(path, file_name)

        # Write a session csv
        header_session_line = "TIMERTIME;TIMESTAMP;POOR_SIGNAL_QUALITY;ATTENTION;MEDITATION;DELTA;THETA;LOW ALPHA;HIGH ALPHA;LOW BETA;HIGH BETA;LOW GAMMA; MID GAMMA;RAW WAVE DATA\n"
        with open(path, "w+") as f:
            f.write(header_session_line)
            for pack in self.__packages:
                f.write(pack + "\n")

        session_csv_path = os.path.join(os.path.dirname(path), "sessions.csv")

        # Add to sessions.csv or create session.csv
        header_line = "INDEX;DATE;FILE_NAME;TIMESTAMP_OF_FIRST_VALID_PACKAGE;TIMESTAMP_OF_LAST_VALID_PACKAGE\n"
        if not os.path.exists(session_csv_path):
            with open("../../data/sessions.csv", "a+") as f:
                f.write(header_line)

        with open(session_csv_path, "w+") as f:
            lines = f.readlines()
            if not lines:  # lines is empty
                f.write(header_line)
                index = 0
            else:
                index = lines[-1].split(";")[0]
                if index == "INDEX":
                    index = 0
                else:
                    index = int(index) + 1

        with open(session_csv_path, "a+") as f:
            date = file_name[8:-4]  # cutting session_ and .csv out
            i = 0
            while self.__packages[i].split(";")[1] != "" and i < len(self.__packages) - 1:
                i += 1
            date_of_first_package = self.__packages[i].split(";")[1]
            i = -1
            while self.__packages[i].split(";")[1] != "" and i > 0:
                i -= 1
            date_of_last_package = self.__packages[i].split(";")[1]
            f.write(f"{index};{date};{file_name};{date_of_first_package};{date_of_last_package}\n")

        self.__packages = []
        self.session_date = None
        self.timer_start = None

    def pause_session(self):
        """
        Pauses the session.
        :return:
        """
        print("PAUSED")
        self.__pause = True
        self.paused_time += time.monotonic() - self.timer_start

    def resume_session(self):
        """
        Resumes the session.
        :return:
        """
        print("RESUMED")
        self.__pause = False
        self.timer_start = time.monotonic()

    @staticmethod
    def last_session_path():
        """
        Returns path to last session taken
        :return: str
        """
        path = os.path.join(up_dir(up_dir(up_dir(os.path.realpath(__file__)))), "data")

        session_csv_path = os.path.join(os.path.dirname(path), "sessions.csv")

        with open(session_csv_path, "w+") as f:
            lines = f.readlines()
            last_session_file_name = lines[-1].split(";")[2]

        path_to_last_session = os.path.join(path, last_session_file_name)
        return path_to_last_session

    def close(self):
        """
        Closes the connection.
        :return:
        """
        self.__arduino.close()
        self.open = False
