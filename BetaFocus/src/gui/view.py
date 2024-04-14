from PyQt5.QtWidgets import QMainWindow, QGridLayout, QWidget, QPushButton, QLabel, QDesktopWidget, QVBoxLayout
from PyQt5.QtGui import QFont, QPainter, QColor, QPainterPath, QBrush, QIcon, QPixmap
from PyQt5.QtCore import Qt, QRectF, QPoint, QSize


class RunWindow(QWidget):

    def __init__(self):
        super(RunWindow, self).__init__()
        self.resize(900, 600)
        self.center()
        self.setStyleSheet("background-color: black;")
        layout = QGridLayout()
        layout.setAlignment(Qt.AlignHCenter)
        layout.setContentsMargins(20, 20, 20, 20)
        # label at the top of the window
        self.label = QLabel("You BetaFocus right now!", self)
        self.label.setFont(QFont("Times New Roman", 60, QFont.Bold))
        self.label.setStyleSheet("color: white;")
        self.label.setAlignment(Qt.AlignHCenter)
        layout.addWidget(self.label, 0, 1, 1, 1)
        # label that displays the time passed
        self.time_label = QLabel("00:00:00:00", self)
        layout.addWidget(self.time_label, 1, 1, 1, 3)
        self.time_label.setAlignment(Qt.AlignHCenter)
        self.time_label.setFont(QFont("Times New Roman", 125, QFont.Bold))
        # set layout to window widget
        self.setLayout(layout)

    def center(self):
        """
        centers the main window according to the desktop size of the device used
        """
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        # top left of rectangle becomes top left of window centering it
        self.move(qr.topLeft())


class MiniButton(QPushButton):

    def __init__(self, character: str):
        super(MiniButton, self).__init__()
        self.setFixedSize(20, 20)
        self.setText(character)
        self.setStyleSheet("border-style: outset;"
                           "border-width: 2px;"
                           "border-radius: 10px;"
                           "border-color: white;"
                           "padding: 2px;")


class StatsButton(QPushButton):

    def __init__(self):
        super(StatsButton, self).__init__()
        self.setText("Statistiken")
        self.setStyleSheet("border-style: outset;"
                           "border-width: 2px;"
                           "border-radius: 10px;"
                           "border-color: white;"
                           "min-width: 15em;"
                           "padding: 6px;")
        pic = QPixmap("stats.png")
        self.setIcon(QIcon(pic))
        self.setIconSize(QSize(5, 5))


class StartButton(QPushButton):

    def __init__(self):
        super(StartButton, self).__init__()
        self.setFixedSize(250, 250)

    def paintEvent(self, event):
        """
        overriding the pushbutton class' paint event to create triangular shape
        """
        p = QPainter(self)
        path = QPainterPath()
        rect = QRectF(0, 0, self.size().width(), self.size().height())
        button_font = QFont("Times New Roman", 30)
        # drawing triangular shape
        path.moveTo(rect.topLeft())                     # starting top left corner
        path.lineTo(rect.bottomLeft())                  # line to bottom left corner
        path.lineTo(rect.width(), rect.height() / 2)    # line to outer right corner
        # filling with color and positioning text
        p.fillPath(path, QBrush(QColor("green")))
        p.setFont(button_font)
        p.setPen(QColor("white"))
        p.drawText(QPoint(int(rect.width() / 3.5), int(rect.height() / 2)), "Start")


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.resize(900, 600)
        self.center()
        self.setWindowTitle("BetaFocus")
        self.setStyleSheet("background-color: black;")
        layout = QGridLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        big_font = QFont("Times New Roman", 60, QFont.Bold)
        normal_font = QFont("Times New Roman", 30)
        # Main window's "BetaFocus" label
        self.label = QLabel("BetaFocus", self)
        self.label.setFont(big_font)
        self.label.setStyleSheet("color: white;")
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label, 0, 1, 1, 1)
        # triangular start button
        self.start_button = StartButton()
        self.start_button.setParent(self)
        layout.addWidget(self.center_widget(self.start_button), 1, 1, 1, 1)
        # statistics button at the bottom
        self.stats_button = StatsButton()
        self.stats_button.setParent(self)
        self.stats_button.setFont(normal_font)
        layout.addWidget(self.center_widget(self.stats_button), 2, 1, 1, 1)
        # information button in the top left corner
        self.info_button = MiniButton("i")
        self.info_button.setParent(self)
        layout.addWidget(self.info_button, 0, 0, 1, 1)
        # help button in the top right corner
        self.help_button = MiniButton("?")
        self.help_button.setParent(self)
        layout.addWidget(self.help_button, 0, 2, 1, 1)
        # other windows are widgets and children of the main window
        self.run_window = RunWindow()
        # set layout to main window
        self.widget = QWidget()
        self.widget.setLayout(layout)
        self.setCentralWidget(self.widget)

    def center(self):
        """
        centers the main window according to the desktop size of the device used
        """
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        # top left of rectangle becomes top left of window centering it
        self.move(qr.topLeft())

    @staticmethod
    def center_widget(button: QPushButton) -> QWidget:
        """
        takes the passed button and adds it the box layout of a widget which is then returned;
        enables the button to be centered within a grid layout
        """
        widget = QWidget()
        box = QVBoxLayout()
        box.setAlignment(Qt.AlignCenter)
        box.addWidget(button, stretch=1, alignment=Qt.AlignCenter)
        box.setContentsMargins(0, 60, 0, 20)
        widget.setLayout(box)
        return widget
