from interval_timer.master import TimerObject, State
import time
import threading


class TabataTimer(TimerObject):
    def __init__(self, rounds=8):
        self.rounds = rounds
        self.start()

    def start(self):
        self.counter = 0
        self.state = State.ACTIVE
        self.tabata()

    def end(self):
        self.start_time = None

    def tabata(self):
        threading.Timer(1.0, self.tabata).start()
        print(self.counter, self.state)
        if self.state == State.ACTIVE:
            if self.counter == 20:
                self.state = State.REST
                self.counter = 0
            else:
                self.counter += 1
        else:
            if self.counter == 10:
                self.state = State.ACTIVE
                self.counter = 0
            else:
                self.counter += 1
