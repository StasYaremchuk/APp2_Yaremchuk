import unittest
import sys
import os

sys.path.append(os.path.abspath('../src'))
from lab2 import minEatingSpeed


class TestMinEatingSpeed(unittest.TestCase):

    def test_case_1(self):
        piles = [3, 6, 7, 11]
        H = 8
        self.assertEqual(minEatingSpeed(piles, H), 4)

    def test_case_2(self):
        piles = [30, 11, 23, 4, 20]
        H = 5
        self.assertEqual(minEatingSpeed(piles, H), 30)

    def test_case_3(self):
        piles = [30, 11, 23, 4, 20]
        H = 6
        self.assertEqual(minEatingSpeed(piles, H), 23)