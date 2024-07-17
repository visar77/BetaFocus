import os

from PyQt5.QtCore import QDir

from gui.view import App
from gui.controller import Controller


def main():
    app = App()
    controller = Controller(app.main_window)
    app.exec()


if __name__ == "__main__":
    root = os.path.dirname(os.path.abspath(__file__))
    QDir.addSearchPath('images', os.path.join(root, 'gui/images'))
    main()
