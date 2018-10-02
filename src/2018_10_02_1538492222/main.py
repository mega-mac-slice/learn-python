#!/usr/bin/env python3
import unittest
from typing import List
from functools import reduce


def product(value: List[int]) -> int:
    return reduce(lambda x, acc: acc * x, value, 1)


class TestSolution(unittest.TestCase):
    def test_success(self):
        result = product([1, 2, 3])
        self.assertEqual(6, result)


if __name__ == '__main__':
    unittest.main()
