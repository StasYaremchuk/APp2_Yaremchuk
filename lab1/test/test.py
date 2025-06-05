import unittest
import sys
import os

sys.path.append(os.path.abspath('../src'))

from lab1 import bubble_sort, find_largest

class TestSorting(unittest.TestCase):
    def test_bubble_sort(self):
        data = [5, 2, 9, 1, 5, 6]
        bubble_sort(data)
        self.assertEqual(data, [1, 2, 5, 5, 6, 9])

        data = [3, 1, 2]
        bubble_sort(data)
        self.assertEqual(data, [1, 2, 3])

        data = [10]
        bubble_sort(data)
        self.assertEqual(data, [10])

        data = [4, 3, 2, 1]
        bubble_sort(data)
        self.assertEqual(data, [1, 2, 3, 4])

    def test_find_largest(self):
        data = [15, 7, 22, 9, 36, 2, 42, 18]

        value, index = find_largest(data, 1)
        self.assertEqual(value, 42)
        self.assertEqual(index, 6)

        value, index = find_largest(data, 2)
        self.assertEqual(value, 36)
        self.assertEqual(index, 4)

        value, index = find_largest(data, 3)
        self.assertEqual(value, 22)
        self.assertEqual(index, 2)

        value, index = find_largest(data, 9)
        self.assertEqual(index, -1)

        value, index = find_largest(data, 0)
        self.assertEqual(index, -1)