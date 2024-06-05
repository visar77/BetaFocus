import os
import pandas as pd

from os.path import dirname as up_dir


class Archive:
    """
    TODO:
    - get: eine Liste mit den Pfaden zu allen Dateien
    - Funktion die zu einem Dateipfad den Dateinamen zurückgibt wie er im Archiv angezeigt werden soll
    """

    def __init__(self):
        self.path = os.path.join(up_dir(up_dir(up_dir(os.path.realpath(__file__)))), "data")


class Session:
    """
    Session-Objekt wird am Ende einer Timer-Session erzeugt
    Nimmt den Pfad zu seinen Daten entgegen
    """

    def __init__(self):
        self.path = ""
        self.data = pd.DataFrame()
        self.x_vals = []
        self.y_vals = []

    def set_path(self, path):
        self.path = path
        self.init_data()

    def init_data(self):
        self.data = pd.read_csv(self.path)
        if self.data:
            print("yes")

    def get_x_vals(self):
        pass

    def get_y_vals(self):
        pass
