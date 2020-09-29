import os
import sys
import unittest

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from interval_timer.tabata import TabataTimer
from interval_timer.interval import IntervalTimer


class TabataTest(unittest.TestCase):
    def test(self):
        pass


if __name__ == '__main__':
    TabataTimer()
