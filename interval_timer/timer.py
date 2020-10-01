from enum import Enum
from PyQt5.QtCore import QTimer, QTime
from PyQt5.QtWidgets import QLCDNumber


class TimerObject(QLCDNumber):
    def __init__(self):
        super().__init__()
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.increment)

        self.update(QTime(0, 0, 0, 0))

    def increment(self):
        self.time = self.time.addSecs(1)
        self.update(self.time)

    def restart(self):
        self.update(QTime(0, 0, 0, 0))
        self.timer.start()

    def pause(self):
        self.timer.stop()

    def start(self):
        self.timer.start()

    def update(self, time=QTime):
        self.time = time
        self.time_string = self.time.toString('mm:ss')
        self.display(self.time_string)


class State(Enum):
    ACTIVE = 0
    REST = 1
