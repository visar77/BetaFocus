from gui.view import App
from gui.controller import Controller


def main():
    app = App()
    controller = Controller(app.mainWindow)
    app.mainWindow.show()
    app.exec()


if __name__ == "__main__":
    main()
