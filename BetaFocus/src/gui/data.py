import os
from datetime import datetime
from os.path import dirname as up_dir
from pathlib import Path

import pandas as pd


class Archive:
    """
    Archive object is created at the start of the program and holds all the data of the sessions.
    With init_data() the data is loaded from the data folder and saved in memory (can be costly).
    """

    def __init__(self):
        self.path = os.path.join(up_dir(up_dir(up_dir(os.path.realpath(__file__)))), "data")
        self.x_data = []
        self.y_data = []
        self.mean_vals = []
        self.sessions = []
        if os.path.exists(os.path.join(self.path, "sessions.csv")):
            self.init_data()

    def init_data(self):
        self.x_data = []
        self.y_data = []
        self.mean_vals = []
        self.sessions = []
        # Read the sessions.csv file into a DataFrame
        sessions_path = os.path.join(self.path, "sessions.csv")
        sessions_df = pd.read_csv(sessions_path, delimiter=';', skip_blank_lines=True, on_bad_lines='skip')

        # Convert the 'FILE_NAME' column to string data type
        sessions_df['FILE_NAME'] = sessions_df['FILE_NAME'].astype(str)

        # Iterate over each row in the DataFrame
        for _, row in sessions_df.iterrows():
            # Extract the session name and date
            session_file_name = str(row['FILE_NAME'])
            session_date = row['DATE']

            session = Session(os.path.join(self.path, str(session_file_name) + ".csv"), str(session_file_name),
                              session_date)
            self.sessions.append(session)
            data = session.data
            i = 0
            while data['TIMESTAMP'].values.tolist()[i] is None:
                i += 1
                if i >= len(data['TIMESTAMP'].values.tolist()) - 1:
                    break
            if i >= len(data['TIMESTAMP'].values.tolist()) - 1:
                continue
            timestamp = data['TIMESTAMP'].values.tolist()[i]
            i = -1
            while data['TIMESTAMP'].values.tolist()[i] is None:
                i -= 1
            abs_time = data['TIMESTAMP'].values.tolist()[i] - timestamp
            self.x_data.append(timestamp / 1000 / 1000 / 1000)
            self.x_data.sort()
            self.y_data.append(abs_time / 1000 / 1000 / 1000 / 60)
            self.y_data.sort()
            self.mean_vals.append(session.get_mean())

        print(self.x_data)
        print(self.y_data)

    def get_x_data(self):
        return self.x_data

    def get_y_data(self):
        return self.y_data

    def get_mean_vals(self):
        return self.mean_vals

    def get_names_of_five_sessions(self, page):
        # Sort the sessions based on their timestamps
        self.sessions = sorted(self.sessions, key=lambda session: session.date_timestamp)
        self.sessions.reverse()
        # Calculate the start and end indices for the slice
        start = (page - 1) * 5
        end = start + 5

        # Return a list of tuples, where each tuple contains the file name and date of a session
        return [session.file_name + " (" + datetime.strftime(session.date_timestamp, "%y-%m-%d_%H-%M-%S") + ")" for
                session in self.sessions[start:end]]

    def get_num_of_sessions(self):
        return len(self.sessions)

    def get_session(self, session_name):

        for session in self.sessions:
            if session.file_name.lower() == session_name.lower():
                return session

        # If the session is not found, search in sessions.csv
        sessions_path = os.path.join(self.path, "sessions.csv")
        sessions_df = pd.read_csv(sessions_path, delimiter=';', skip_blank_lines=True, on_bad_lines='skip')
        for i in range(len(sessions_df['FILE_NAME'].values.tolist())):
            if str(sessions_df['FILE_NAME'].values.tolist()[i]) == session_name:
                session_date = sessions_df['DATE'].values.tolist()[i]
                session = Session(os.path.join(self.path, session_name + ".csv"), session_name, session_date)
                self.sessions.append(session)
                return session

        # If cant be found in sessions.csv return None
        return None

    def set_session_name(self, old_name: str, new_name: str):
        # Get session
        session = self.get_session(old_name)
        old_path = session.path

        # Rename the session file and path of Session object
        session.change_name(new_name)
        new_path = session.path
        os.rename(old_path, new_path)

        # Update the session name in the sessions.csv file
        sessions_path = os.path.join(up_dir(up_dir(up_dir(os.path.realpath(__file__)))), "data", "sessions.csv")
        sessions = pd.read_csv(sessions_path, delimiter=';', skip_blank_lines=True, on_bad_lines='skip')

        # Convert the 'FILE_NAME' column to string data type
        sessions['FILE_NAME'] = sessions['FILE_NAME'].astype(str)

        # Find the row with the old file name and replace it with the new file name
        for i in range(len(sessions['FILE_NAME'].values.tolist())):
            if str(sessions['FILE_NAME'].values.tolist()[i]) == str(old_name):
                sessions['FILE_NAME'].values[i] = str(new_name)
                break

        # Write the updated DataFrame back to the sessions.csv file
        sessions.to_csv(sessions_path, index=False, encoding="utf-8", sep=';')

    def sessions_csv_created(self):
        return os.path.exists(os.path.join(self.path, "sessions.csv"))


class Session:
    """
    Session object holds the data of a single session. It is created by an Archive object.
    """

    def __init__(self, path, file_name, date_timestamp):
        self.path = path
        self.file_name = file_name
        self.date_timestamp = datetime.strptime(date_timestamp, "%y-%m-%d_%H-%M-%S-%f")
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
        self.init_data()

    def init_data(self):
        self.data = pd.read_csv(self.path, delimiter=';', skip_blank_lines=True, parse_dates=[1], on_bad_lines='skip')
        i = 0
        while self.data['TIMESTAMP'].values.tolist()[i] is None:
            i += 1
            if i >= len(self.data['TIMESTAMP'].values.tolist()) - 1:
                return
        self.start = self.data['TIMESTAMP'].values.tolist()[i]
        for j in range(len(self.data['TIMESTAMP'].values.tolist())):
            if self.data['TIMESTAMP'].values.tolist()[j] is not None:
                self.x_vals.append((self.data['TIMESTAMP'].values.tolist()[j] - self.start) / 1000 / 1000 / 1000)
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

    def change_name(self, new_name):
        self.path = os.path.join(up_dir(self.path), str(new_name) + ".csv")
        self.file_name = str(new_name)
