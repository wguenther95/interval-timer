import os
import sys
import unittest

from PyQt5.QtWidgets import QApplication

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from interval_timer.tabata import TabataTimer
from interval_timer.interval import IntervalTimer
from interval_timer.master import TimerObject


class TabataTest(unittest.TestCase):
    def test(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TimerObject()
    sys.exit(app.exec_())
