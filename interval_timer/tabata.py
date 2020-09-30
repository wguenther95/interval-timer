from interval_timer.master import TimerObject, State
import time
import threading


class TabataTimer(TimerObject):
    state = State.ACTIVE

    def __init__(self, rounds=8):
        super().__init__()
        self.rounds = rounds
        self.round_counter = 0
        self.start()

    def start(self):
        self.restart()
        self.timer.timeout.connect(self.tabata)

    def tabata(self):
        if self.round_counter < self.rounds:
            if self.state == State.ACTIVE:
                if self.time_string == '00:20':
                    self.state = State.REST
                    print("REST")
                    self.restart()
            else:
                if self.time_string == '00:10':
                    self.state = State.ACTIVE
                    print("ACTIVE")
                    self.restart()
                    self.round_counter += 1
        else:
            print("STOP")
