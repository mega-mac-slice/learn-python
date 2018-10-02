#!/usr/bin/env python3
import unittest
from typing import List
from itertools import permutations


def solve(n: int) -> List[str]:
    options = ['r', 'd']
    items = [''.join(i) for i in permutations(options * n, 2 * n)]
    return [i for i in set(items)]


class TestSolution(unittest.TestCase):
    def test_1_success(self):
        result = solve(1)
        self.assertEqual(2, len(result))

    def test_2_success(self):
        result = solve(2)
        self.assertEqual(6, len(result))

    def test_10_success(self):
        result = solve(10)
        self.assertEqual(6, len(result))

    def test_20_success(self):
        result = solve(10)
        self.assertIsNotNone(result)


if __name__ == '__main__':
    unittest.main()
