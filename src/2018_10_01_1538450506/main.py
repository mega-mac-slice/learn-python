#!/usr/bin/env python3
import unittest
import math


def solve(value: int) -> int:
    freq = [0 for _ in range(10)]

    while value > 0:
        digit = int(math.floor(value % 10))
        freq[digit] += 1
        value = int(value / 10)

    result = 0
    multiplier = 0
    for value in range(1, 10)[::-1]:
        count = freq[value]
        for _ in range(count):
            result += value * 10 ** multiplier
            multiplier += 1

    return result


class TestSolution(unittest.TestCase):

    def test_8970_success(self):
        result = solve(8970)
        self.assertEqual(789, result)

    def test_32445_success(self):
        result = solve(32445)
        self.assertEqual(23445, result)

    def test_10101_success(self):
        result = solve(10101)
        self.assertEqual(111, result)


if __name__ == '__main__':
    unittest.main()
