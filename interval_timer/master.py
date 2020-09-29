import time


class TimerController:
    def __init__(self):
        self.timer = time.perf_counter()
        print(self.timer)
