import os
import sys
import time
from datetime import datetime, timezone
from os.path import dirname as up_dir

import serial.tools.list_ports

# Standard baudrate
BAUDRATE = 9600


class MicroController:
    """
    It is used as an abstraction of the hardware and represent the MicroController. It is used to connect to the
    MicroController, which is directly connected with the TGAM Module of the EEG Toy and read the data from it.
    The real hardware provides the data in CSV format and the MicroController class reads that data from the serial
    connection.
    """

    def __init__(self, port, baudrate=BAUDRATE, timeout=10.0):
        """
        Initializes a MicroController instance and creates a serial connection using the serial library.

        :param port: str, The serial port to connect to.
        :param baudrate: int, The baudrate for the serial connection (default: BAUDRATE(=9600)).
        :param timeout: float, The number of seconds after which a timeout sets in (default: 10 seconds).
        """
        self.__port = port
        self.__baudrate = baudrate
        self.__ser = serial.Serial(port, baudrate, timeout=timeout)
        self.__timeout = timeout

    def is_open(self):
        """
        Checks if serial connection is open
        :return: bool, True if the serial connection is open, False otherwise.
        """
        return self.__ser.is_open

    def open(self):
        """
        Opens the serial connection and flushes the input buffer.
        :return: None
        """
        self.__ser.open()
        self.__ser.flushInput()

    def last_package(self):
        """
        Reads the data from the serial connection and returns a string in CSV format, which represents the last package
        recorded by the hardware.
        :return: string, the last package in CSV format OR None if no package was found
        """
        # Read line by line from the serial connection
        while self.is_open():
            line = None
            try:
                # Read line from serial connection
                line = str(self.__ser.readline())
            except Exception as e:
                # Close the connection if an error occurs
                self.close()
                print("Can't read from serial port because of ", e)
                break

            if line == "b''" or line == '':  # This means readLine went to timeout
                self.close()
                break

            if line is None:  # If for some other reason line is still None break
                self.close()
                break

            # Check if read line contains the CSV data
            if "CSV" in line:
                s = line[7:-3]  # Cut the CSV data out of the line and remove the newline character

                # Add timestamp to the front of the package and return it
                full_package = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S.%f') + ";" + s
                return full_package
        return None

    def close(self):
        """
        Closes the serial connection.
        :return: None
        """
        self.__ser.close()

    def switch_connection(self, port, baudrate=BAUDRATE):
        """
        Switches the connection to another port.

        :param port: str, The new serial port to connect to.
        :param baudrate: int, The new baudrate for the serial connection (default: 9600).
        :return: None
        """
        self.__port = port
        self.__baudrate = baudrate
        self.__ser = serial.Serial(port, baudrate)

    @staticmethod
    def get_available_ports():
        """
        Returns a list of available ports.
        Inspired by answer of tfeldmann to https://stackoverflow.com/questions/12090503/listing-available-com-ports-with-python

        :raises EnvironmentError: If the platform is unsupported or unknown.
        :return: list, A list of available ports.
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
    MCConnector represents an interface for the GUI to work with the hardware, without handling the hardware directly.
    This class is used to start, stop, pause and resume sessions. The recorded sessions are then saved in the data folder
    with the format session_yy-mm-dd_hh-mm-ss-ffffff.csv and further added to the sessions.csv file. The sessions.csv file
    is used to keep track of all the sessions taken and stores an index, the date and file name of each session.
    It creates a MicroController object and uses it to connect to the hardware. Through the MicroController object it
    reads the data from the hardware.

    The creations of files and folders is not protected by locks, even though race conditions are possible (see stop_session).
    The reason is that MCConnector only creates files and folders, if they don't exist, and the only other program that
    modifies the same files is the GUI, which is not running at the same time as MCConnector.
    """

    def __init__(self, port, baudrate=BAUDRATE):
        """
        Creates the MicroController Connector. It requires a serial port, and the baudrate can be set, if not set it's
        set to BAUDRATE (=9600).
        :param port: serial port
        :param baudrate: baudrate (default: BAUDRATE)
        """
        self.__arduino = MicroController(port, baudrate)
        self.__packages = []
        self.__pause = False
        self.__timer_start = None
        self.__paused_time = 0.0
        self.__session_date = None

        self.receive = self.__arduino.is_open()

    def start_session(self):
        """
        Starts a session and logs the data in a list. It opens the serial connection if it's not already open and
        continuously reads data from the hardware until the session is stopped or paused.
        The data is in the form of packages, which are strings with following format:
        "TIMERTIME;TIMESTAMP;SIGNAL_QUALITY;ATTENTION;MEDITATION;DELTA;THETA;LOW ALPHA;HIGH ALPHA;"
        The data gets stored in the list self.__packages.
        :return: None
        """
        # Get the date when the session started
        self.__session_date = datetime.now().strftime("%y-%m-%d_%H-%M-%S-%f")

        # Get the time when the session started
        self.__timer_start = time.monotonic()

        # Open serial connection explicitly
        if not self.__arduino.is_open():
            self.open()

        # Check if data can be received
        if not self.receive:
            print("Connection not open! Session can't be started")

        while self.receive:
            # Get package from the hardware through MicroController
            package = self.__arduino.last_package()

            # Ignore packages if the session is paused
            if self.__pause:
                print("Pausing")
                continue

            # If package is None,
            if package is None:
                print("No package found! Check connection")
                continue

            # Add the time passed since the session started to the start of the package
            # and add the package to the list
            package = str(self.__paused_time + time.monotonic() - self.__timer_start) + ";" + package
            print("package received: ", package)
            self.__packages.append(package)

        print("Session stopped")

    def stop_session(self):
        """
        Stops the current session, writes the logged data to a CSV file, and closes the serial connection.
        The CSV file is saved in the data folder with a timestamp in its name. The session is also added to
        the sessions.csv file, which keeps track of all sessions.
        :return None
        """
        if self.__arduino.is_open():
            self.close()  # Close the connection and stops the session logging done by start_session

        # Paths to data folder and session csv
        path = os.path.join(up_dir(up_dir(up_dir(os.path.realpath(__file__)))), "data")
        file_name = rf"session_{self.__session_date}"
        file_path = os.path.join(path, file_name + ".csv")

        # Write the session csv file
        header_session_line = "TIMERTIME;TIMESTAMP;SIGNAL_QUALITY;ATTENTION;MEDITATION;DELTA;THETA;LOW ALPHA;HIGH ALPHA;LOW BETA;HIGH BETA;LOW GAMMA; MID GAMMA;RAW WAVE DATA\n"

        # Create the data folder if it doesn't exist
        if not os.path.isdir(path):
            os.makedirs(path)

        # Write the session data to the session csv file
        with open(file_path, "w+") as f:
            f.write(header_session_line)
            for pack in self.__packages:
                f.write(pack + "\n")

        session_csv_path = os.path.join(path, "sessions.csv")

        # Add to sessions.csv or create session.csv
        header_line = "INDEX;DATE;FILE_NAME\n"

        # Check if sessions.csv exists, if not create it
        # Note: Race conditions possible, but should not be relevant (or possible) for this program (see class docstring)
        if not os.path.exists(session_csv_path):
            with open(session_csv_path, "a+") as f:
                f.write(header_line)

        # Get the index for the new session
        with open(session_csv_path, "r+") as f:
            lines = f.readlines()
            if not lines:  # if session.csv is empty, which shouldn't happen, write header
                f.seek(0)
                f.write(header_line)
                index = 0
            else:
                index = lines[-1].split(";")[0]
                if index == "INDEX":
                    index = 0
                else:
                    index = int(index) + 1

        # Add session to sessions.csv
        with open(session_csv_path, "a+") as f:
            date = file_name[8:-4]  # cutting session_ and .csv out
            f.write(f"{index};{date};{file_name}\n")

        self.__packages = []
        self.__session_date = None
        self.__timer_start = None

    def pause_session(self):
        """
        Pauses the current session. While a session is paused, no data is read from the hardware.
        :return:
        """
        if self.__pause:  # Can't really happen, but better safe than sorry
            print("Session is already paused!")
            return
        print("PAUSED")
        self.__pause = True
        self.__paused_time += time.monotonic() - self.__timer_start

    def resume_session(self):
        """
        Resumes a paused session. After a session is resumed, data is again read from the hardware and logged.
        :return: None
        """
        if not self.__pause:  # Can't really happen, but better safe than sorry
            print("Session is not paused!")
            return
        print("RESUMED")
        self.__pause = False
        self.__timer_start = time.monotonic()

    @staticmethod
    def last_session_name():
        """
        Returns the name of the last session that was recorded. The name is extracted from the sessions.csv file
        :return: str, The name of the last session.
        """
        path = os.path.join(up_dir(up_dir(up_dir(os.path.realpath(__file__)))), "data")

        session_csv_path = os.path.join(path, "sessions.csv")

        with open(session_csv_path, "r") as f:
            lines = f.readlines()
            last_session_file_name = lines[-1].split(";")[2][:-1]  # cutting \n out

        return last_session_file_name

    def open(self):
        """
        Opens the serial connection to the hardware. This method needs to be called before starting a session.
        :return: None
        """
        self.receive = True
        self.__arduino.open()

    def close(self):
        """
        Closes the serial connection to the hardware. This method should be called after a session is stopped.
        :return: None
        """
        self.receive = False
        self.__arduino.close()
