import os
import pandas as pd

from datetime import datetime
from os.path import dirname as up_dir


class Archive:
    """
    TODO:
    - get: eine Liste mit den Pfaden zu allen Dateien
    - Funktion die zu einem Dateipfad den Dateinamen zurückgibt wie er im Archiv angezeigt werden soll
    """

    def __init__(self):
        self.path = os.path.join(up_dir(up_dir(up_dir(os.path.realpath(__file__)))), "data")
        self.dir = os.fsencode(self.path)
        self.x_data = []
        self.y_data = []
        self.mean_vals = []
        self.init_data()

    def init_data(self):
        self.x_data = []
        self.y_data = []
        self.mean_vals = []
        for file in os.listdir(self.dir):
            filename = os.fsdecode(file)
            if filename != "sessions.csv":
                data = pd.read_csv(os.path.join(self.path, filename), delimiter=';', skip_blank_lines=True,
                                   parse_dates=[1], on_bad_lines='skip')
                if not data.empty and len(data['TIMESTAMP'].values.tolist()) < 1:
                    i = 0
                    while data['TIMESTAMP'].values.tolist()[i] is None:
                        i += 1
                    timestamp = data['TIMESTAMP'].values.tolist()[i]
                    i = -1
                    while data['TIMESTAMP'].values.tolist()[i] is None:
                        i -= 1
                    abs_time = data['TIMESTAMP'].values.tolist()[i] - timestamp
                    self.x_data.append(timestamp/1000/1000/1000)
                    self.x_data.sort()
                    self.y_data.append(abs_time/1000/1000/1000/60)
                    self.y_data.sort()
                    self.mean_vals.append(data['ATTENTION'].mean(skipna=True))

    def get_x_data(self):
        return self.x_data

    def get_y_data(self):
        return self.y_data

    def get_mean_vals(self):
        return self.mean_vals

    def get_five(self):
        sessions = pd.read_csv(os.path.join(self.path, "sessions.csv"), delimiter=';', skip_blank_lines=True,
                               on_bad_lines='skip')
        if len(sessions['FILE_NAME'].values.tolist()) > 5:
            return sessions['FILE_NAME'].values.tolist()[-5:-1]
        else:
            return sessions['FILE_NAME'].values.tolist()


class Session:
    """
    Session-Objekt wird am Ende einer Timer-Session erzeugt
    Nimmt den Pfad zu seinen Daten entgegen
    """

    def __init__(self):
        self.path = ""
        self.data = pd.DataFrame()
        # data
        self.start = 0
        self.x_vals = []
        self.y_vals = []
        # stats
        self.mean = 0
        self.max = 0
        # thresholds
        self.upper = 60
        self.lower = 40

    def set_path(self, path):
        self.path = path
        self.init_data()

    def init_data(self):
        self.data = pd.read_csv(self.path, delimiter=';', skip_blank_lines=True, parse_dates=[1], on_bad_lines='skip')
        i = 0
        while self.data['TIMESTAMP'].values.tolist()[i] is None:
            i += 1
        self.start = self.data['TIMESTAMP'].values.tolist()[i]
        for j in range(len(self.data['TIMESTAMP'].values.tolist())):
            if self.data['TIMESTAMP'].values.tolist()[j] is not None:
                self.x_vals.append((self.data['TIMESTAMP'].values.tolist()[j] - self.start)/1000/1000/1000)
                self.y_vals.append(self.data['ATTENTION'].values.tolist()[j])

    def get_x_vals(self):
        return self.x_vals

    def get_y_vals(self):
        return self.y_vals

    def get_mean(self):
        return self.data['ATTENTION'].mean(skipna=True)

    def get_max(self):
        return self.data['ATTENTION'].max()

    def get_upper(self):
        return self.upper

    def get_lower(self):
        return self.lower

    def set_session_name(self, name: str):
        os.rename(self.path, os.path.join(up_dir(up_dir(up_dir(os.path.realpath(__file__)))), "data", f"{name}.csv"))
        self.path = os.path.join(up_dir(up_dir(up_dir(os.path.realpath(__file__)))), "data", f"{name}.csv")

        sessions = pd.read_csv(os.path.join(up_dir(up_dir(up_dir(os.path.realpath(__file__)))), "data", "sessions.csv"),
                               delimiter=';', skip_blank_lines=True, on_bad_lines='skip')
        sessions['FILE_NAME'].replace(self.path.split('/')[-1], f"{name}.csv")
        sessions.to_csv(os.path.join(up_dir(up_dir(up_dir(os.path.realpath(__file__)))), "data", "sessions.csv"))
