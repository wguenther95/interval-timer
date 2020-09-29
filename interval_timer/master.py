from enum import Enum
from PyQt5.QtCore import QTimer, QTime


class TimerObject:
    def __init__(self):
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.increment)

        self.restart()

    def increment(self):
        self.time = self.time.addSecs(1)
        self.time_string = self.time.toString('mm:ss')
        print(self.time_string)

    def restart(self):
        self.time = QTime(0, 0, 0, 0)
        self.time_string = self.time.toString('mm:ss')
        self.timer.start()


class State(Enum):
    ACTIVE = 0
    REST = 1
