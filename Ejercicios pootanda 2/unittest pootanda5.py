"""
pootanda2tarea5v1 test by Fran Ogallas
"""


from unittest import TestCase
import unittest
from pootanda2tarea5v1 import Stack
from pootanda2tarea5v1 import Queue


class TestStackAndQueue(TestCase):

    def setUp(self):
        self.test_stack = Stack((1, 2, 3, 4))
        self.test_queue = Queue((5, 6, 7, 8))

    def test_len(self):
        self.assertEqual(len(self.test_queue), 4)
        self.assertEqual(len(self.test_stack), 4)

    def test_see_top_element(self):
        self.assertEqual(self.test_stack.see_top_element(), 1)
        self.assertEqual(self.test_queue.see_top_element(), 5)

    def test_push_and_pop(self):
        self.test_stack.push(9)
        self.assertEqual(str(self.test_stack), "[9, 1, 2, 3, 4]")
        self.assertEqual(self.test_stack.pop(), 9)

    def test_enqueue_and_dequeue(self):
        self.test_queue.enqueue(9)
        self.assertEqual(str(self.test_queue), "[5, 6, 7, 8, 9]")
        self.assertEqual(self.test_queue.dequeue(), 5)

    def test_empty_and_is_empty(self):
        self.test_stack.empty()
        self.assertEqual(len(self.test_stack), 0)
        assert self.test_stack.is_empty()
        self.test_queue.empty()
        self.assertEqual(len(self.test_queue), 0)
        assert self.test_queue.is_empty()

    def mytest(self):
        self.test_len()
        self.test_see_top_element()
        self.test_push_and_pop()
        self.test_enqueue_and_dequeue()
        self.test_empty_and_is_empty()

    def tearDown(self):
        del self.test_stack
        del self.test_queue


if __name__ == '__main__':
    unittest.main()
