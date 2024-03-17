"""
pootanda2tarea8manageabledatev1 test by Fran Ogallas
"""

from pootanda2tarea8manageabledatev1 import ManageableDate
import unittest
from unittest import TestCase
from datetime import date


class MyTestCase(TestCase):

    def setUp(self):
        self.manageabledate_1 = ManageableDate(date(2023, 2, 1))
        self.manageabledate_2 = ManageableDate(date(2024, 3, 2))

    def test_validate_date(self):
        assert ManageableDate.validate_date(2024, 2, 24)
        assert not ManageableDate.validate_date(0, 2, 24)
        assert ManageableDate.validate_date(1, 2, 24)
        assert not ManageableDate.validate_date(10000, 2, 24)
        assert ManageableDate.validate_date(1, 1, 1)
        assert not ManageableDate.validate_date(2022, 2, 29)
        assert ManageableDate.validate_date(9999, 12, 31)
        assert not ManageableDate.validate_date(2022, 4, 0)
        assert ManageableDate.validate_date(2024, 2, 29)

    def test_change_year(self):
        try:
            self.manageabledate_1.change_year(8000, [2023, 2, 1])
        except ValueError:
            pass
        try:
            self.manageabledate_1.change_year(-3000, [2023, 2, 1])
        except ValueError:
            pass
        self.assertEqual(str(self.manageabledate_1.change_year(1, [2023, 2, 1])),
                         "[2024, 2, 1]")
        self.assertEqual(str(self.manageabledate_1.change_year(-1, [2023, 2, 1])),
                         "[2022, 2, 1]")
        self.assertEqual(str(self.manageabledate_1.change_year(0, [2023, 2, 1])),
                         "[2023, 2, 1]")

    def test_change_month(self):
        try:
            self.manageabledate_1.change_month(1000000, [2023, 2, 1])
        except ValueError:
            pass
        try:
            self.manageabledate_1.change_month(-10000000, [2023, 2, 1])
        except ValueError:
            pass
        self.assertEqual(str(self.manageabledate_1.change_month(2, [2024, 2, 1])),
                         "[2024, 4, 1]")
        self.assertEqual(str(self.manageabledate_1.change_month(-2, [2023, 2, 1])),
                         "[2022, 12, 1]")
        self.assertEqual(str(self.manageabledate_1.change_month(0, [2023, 2, 1])),
                         "[2023, 2, 1]")

    def test_change_days(self):
        try:
            self.manageabledate_1.change_n_days(1000000, [2023, 2, 1])
        except ValueError:
            pass
        try:
            self.manageabledate_1.change_n_days(-10000000, [2023, 2, 1])
        except ValueError:
            pass
        self.assertEqual(str(self.manageabledate_1.change_n_days(4, [2024, 2, 27])),
                         "[2024, 3, 2]")
        self.assertEqual(str(self.manageabledate_1.change_n_days(-4, [2023, 1, 2])),
                         "[2022, 12, 29]")
        self.assertEqual(str(self.manageabledate_1.change_n_days(0, [2023, 2, 1])),
                         "[2023, 2, 1]")

    def test_comparison_macrotool(self):
        self.assertEqual(self.manageabledate_1.comparison_macrotool([2024, 2, 1]), (f"La fecha introducida es más "
                                                                                    f"RECIENTE que la fecha almacenada."
                                                                                    f"\ncon una diferencia de "
                                                                                    f"365 días."))
        self.assertEqual(self.manageabledate_1.comparison_macrotool([2022, 2, 1]), (f"La fecha introducida es más "
                                                                                    f"ANTIGUA que la fecha almacenada."
                                                                                    f"\ncon una diferencia de "
                                                                                    f"365 días."))
        self.assertEqual(self.manageabledate_1.comparison_macrotool([2023, 2, 1]), (f"Ambas son la misma fecha."))

    def mytest(self):
        self.test_validate_date()
        self.test_change_year()
        self.test_change_month()
        self.test_change_days()
        self.test_comparison_macrotool()

    def tearDown(self):
        del self.manageabledate_1
        del self.manageabledate_2


if __name__ == '__main__':
    unittest.main()
