"""
pootanda2tarea7v1 test by Fran Ogallas
"""

from pootanda2tarea7v1 import Fraction
import unittest
from unittest import TestCase


class MyTestCase(TestCase):

    def setUp(self):
        self.fraction_1 = Fraction(1, 2)
        self.fraction_2 = Fraction(12, 3)

    def test_result_fraction(self):
        self.assertEqual(self.fraction_1.result_fraction(), 0.5)
        self.assertEqual(self.fraction_2.result_fraction(), 4.0)

    def test_calculation_operands(self):
        self.assertEqual(str(self.fraction_1 * self.fraction_2), "2/1")
        self.assertEqual(str(self.fraction_2 * self.fraction_1), "2/1")
        self.assertEqual(str(self.fraction_1 / self.fraction_2), "1/8")
        self.assertEqual(str(self.fraction_2 / self.fraction_1), "8/1")
        self.assertEqual(str(self.fraction_1 + self.fraction_2), "9/2")
        self.assertEqual(str(self.fraction_1 - self.fraction_2), "-7/2")
        self.assertEqual(str(self.fraction_2 - self.fraction_1), "7/2")

    def test_comparisons(self):
        assert not self.fraction_1 == self.fraction_2
        assert self.fraction_1 != self.fraction_2
        assert self.fraction_1 < self.fraction_2
        assert self.fraction_1 <= self.fraction_2
        assert not self.fraction_1 > self.fraction_2
        assert not self.fraction_1 >= self.fraction_2
        try:
            exception_inducer = self.fraction_1 == "fraction_2"
            raise AssertionError("Fractions only should be allowed to be compared with fractions")
        except TypeError:
            pass


    def mytest(self):
        self.test_result_fraction()
        self.test_calculation_operands()
        self.test_comparisons()


    def tearDown(self):
        del self.fraction_1
        del self.fraction_2


if __name__ == '__main__':
    unittest.main()