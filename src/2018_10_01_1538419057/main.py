#!/usr/bin/env python3
import unittest
from typing import List


def sum_exists(a: List[int], b: List[int]) -> bool:
    seen = set()

    for x in a:
        for y in b:
            diff = y - x

            if diff in seen:
                return True

        seen.add(x)

    return False


class TestSolution(unittest.TestCase):
    def test_simple_success(self):
        result = sum_exists([1, 2], [3])
        self.assertTrue(result)

    def test_simple_fail(self):
        result = sum_exists([1, 2], [4])
        self.assertFalse(result)

    def test_simple_negative_success(self):
        result = sum_exists([-1, 4], [3])
        self.assertTrue(result)

    def test_simple_negative_fail(self):
        result = sum_exists([-1, 4], [4])
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
