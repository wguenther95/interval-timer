from interval_timer.master import TimerObject, State
import time
import threading


class TabataTimer(TimerObject):
    def __init__(self, rounds=8):
        self.rounds = rounds

        self.start()

    def start(self):
        self.timer = 0
        self.round_counter = 0
        self.state = State.ACTIVE

        t = threading.Timer(1.0, self.tabata)
        t.start()
