import os
import sys
import unittest

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from interval_timer.routine import Routine, Cycle


class DefaultConditionsTest(unittest.TestCase):
    def setUp(self):
        self.routine = Routine()

    def tearDown(self):
        self.routine = None

    def test_default_routine(self):
        self.assertEqual(self.routine.name, None, "Should be None")
        self.assertEqual(self.routine.num_cycles, 1, "Should be 1")
        self.assertEqual(self.routine.warmup, 10, "Should be 10 seconds")
        self.assertEqual(self.routine.cooldown, 30, "Should be 30 seconds")

    def test_default_cycle(self):
        self.assertEqual(self.routine.cycles[0].sets, 10, "Should be 10")
        self.assertEqual(self.routine.cycles[0].low_time, 10, "Should be 10")
        self.assertEqual(self.routine.cycles[0].high_time, 60, "Should be 60")


class RoutineUpdateTest(unittest.TestCase):
    def setUp(self):
        self.routine = Routine()
        self.routine.update("Routine", 5, 15, 15)

    def tearDown(self):
        self.routine = None

    def test_update_routine(self):
        self.assertEqual(self.routine.name, 'Routine', "Should be Routine")
        self.assertEqual(self.routine.num_cycles, 5, "Should be 5")
        self.assertEqual(self.routine.warmup, 15, "Should be 15 seconds")
        self.assertEqual(self.routine.cooldown, 15, "Should be 15 seconds")


class CycleAdditionTest(unittest.TestCase):
    def setUp(self):
        self.routine = Routine()
        cycle = Cycle()
        self.routine.add_cycle(cycle)
        cycle.update(5, 15, 30)

    def tearDown(self):
        self.routine = None

    def test_cycle1(self):
        self.assertEqual(self.routine.cycles[0].sets, 10, "Should be 10")
        self.assertEqual(self.routine.cycles[0].low_time, 10, "Should be 10")
        self.assertEqual(self.routine.cycles[0].high_time, 60, "Should be 60")

    def test_cycle2(self):
        self.assertEqual(self.routine.cycles[1].sets, 5, "Should be 5")
        self.assertEqual(self.routine.cycles[1].low_time, 15, "Should be 15")
        self.assertEqual(self.routine.cycles[1].high_time, 30, "Should be 30")


if __name__ == '__main__':
    unittest.main()
