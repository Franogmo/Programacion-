"""
pootanda2tarea6v3 test by Fran Ogallas
"""

from pootanda2tarea6v3 import Duration
import unittest
from unittest import TestCase


class MyTestCase(TestCase):

    def setUp(self):
        self.duration1 = Duration(5, -70, -70)

    def test_negative_hours(self):
        try:
            self.duration5 = Duration(-2, 8, 8)
            assert False
        except ValueError:
            pass

    def test_addition_methods(self):
        self.duration1.add_hours(3)
        self.assertEqual(self.duration1.hours, 6)
        self.duration1.add_hours(-3)
        self.assertEqual(self.duration1.hours, 3)
        try:
            self.duration1.add_hours(-10)
            assert False
        except ValueError:
            pass
        self.duration1.add_minutes(3)
        self.assertEqual(self.duration1.minutes, 51)
        self.duration1.add_minutes(-3)
        self.assertEqual(self.duration1.minutes, 48)
        try:
            self.duration1.add_minutes(-1000000)
            assert False
        except ValueError:
            pass
        self.duration1.add_seconds(3)
        self.assertEqual(self.duration1.seconds, 53)
        self.duration1.add_seconds(-3)
        self.assertEqual(self.duration1.seconds, 50)
        try:
            self.duration1.add_seconds(-1000000)
            print(f"{self.duration1.hours}h {self.duration1.minutes}min {self.duration1.seconds}s")
            input()
            assert False
        except ValueError:
            pass

    def test_subtraction_methods(self):
        self.duration1.subtract_hours(3)
        self.assertEqual(self.duration1.hours, 0)
        self.duration1.subtract_hours(-3)
        self.assertEqual(self.duration1.hours, 3)
        try:
            self.duration1.subtract_hours(10)
            assert False
        except ValueError:
            pass
        self.duration1.subtract_minutes(3)
        self.assertEqual(self.duration1.minutes, 45)
        self.duration1.subtract_minutes(-3)
        self.assertEqual(self.duration1.minutes, 48)
        try:
            self.duration1.subtract_minutes(1000000)
            assert False
        except ValueError:
            pass
        self.duration1.subtract_seconds(3)
        self.assertEqual(self.duration1.seconds, 47)
        self.duration1.subtract_seconds(-3)
        self.assertEqual(self.duration1.seconds, 50)
        try:
            self.duration1.subtract_seconds(1000000)
            assert False
        except ValueError:
            pass


    def test_operands(self):
        self.duration2 = Duration(1, 30, 30)
        self.duration3 = self.duration1 + self.duration2
        self.assertEqual(self.duration3.hours, 5)
        self.assertEqual(self.duration3.minutes, 19)
        self.assertEqual(self.duration3.seconds, 20)
        self.duration4 = self.duration1 - self.duration2
        self.assertEqual(self.duration4.hours, 2)
        self.assertEqual(self.duration4.minutes, 18)
        self.assertEqual(self.duration4.seconds, 20)

    def mytest(self):
        self.test_negative_hours()
        self.test_addition_methods()
        self.test_subtraction_methods()
        self.test_operands()

    def tearDown(self):
        del self.duration1


if __name__ == '__main__':
    unittest.main()
