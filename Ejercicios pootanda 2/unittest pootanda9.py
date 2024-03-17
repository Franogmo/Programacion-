"""
pootanda2tarea9v2 test by Fran Ogallas
"""

from pootanda2tarea9v2 import NewDate
import unittest
from unittest import TestCase


class MyTestCase(TestCase):

    def setUp(self):
        self.newdate1 = NewDate(5, 1, 2024)
        self.newdate2 = NewDate(26, 2, 2024)
        self.newdate3 = NewDate(self.newdate1)


    def test_change_newdate(self):
        try:
            self.newdate1.change_newdate(1000000)
        except ValueError:
            pass
        try:
            self.newdate1.change_newdate(-1000000)
        except ValueError:
            pass
        self.newdate2.change_newdate(5)
        self.assertEqual(str(self.newdate2),"2 de Marzo de 2024")
        self.newdate1.change_newdate(-9)
        self.assertEqual(str(self.newdate1),"27 de Diciembre de 2023")
        self.newdate2.change_newdate(0)
        self.assertEqual(str(self.newdate2),"2 de Marzo de 2024")

    def test_compare_newdates(self):
        self.assertEqual(self.newdate1.compare_newdates(self.newdate2), f"{self.newdate1} es una fecha más "
                                                                        f"antigua que {self.newdate2}")
        self.assertEqual(self.newdate2.compare_newdates(self.newdate1), f"{self.newdate2} es una fecha más "
                                                                        f"reciente que {self.newdate1}")
        self.assertEqual(self.newdate1.compare_newdates(self.newdate3), "Ambas son la misma fecha")

    def test_other_magic_methods(self):
        try:
            x = self.newdate1 - 8
            raise SyntaxError
        except TypeError:
            pass
        self.assertEqual(len(self.newdate1), 739255)


    def mytest(self):
        self.test_change_newdate()
        self.test_compare_newdates()
        self.test_other_magic_methods()



    def tearDown(self):
        del self.newdate1
        del self.newdate2


if __name__ == '__main__':
    unittest.main()
