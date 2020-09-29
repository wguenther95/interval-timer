from interval_timer.master import TimerObject
import time


class TabataTimer(TimerObject):
    def __init__(self, rounds=8):
        self.rounds = rounds
        self.start()

    def start(self):
        self.start_time = time.perf_counter()
        cur_time = time.perf_counter() - self.start_time
        print(cur_time)

    def end(self):
        self.start_time = None
