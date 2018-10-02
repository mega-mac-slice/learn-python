#!/usr/bin/env python3
import unittest


def solve(n: int) -> int:
    path = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        path[i][0] = 1
        path[0][i] = 1

    for y in range(1, n + 1):
        for x in range(1, n + 1):
            top = path[y - 1][x]
            left = path[y][x - 1]
            path[y][x] = top + left

    return path[-1][-1]


class TestSolution(unittest.TestCase):
    def test_1_success(self):
        result = solve(1)
        self.assertEqual(2, result)

    def test_2_success(self):
        result = solve(2)
        self.assertEqual(6, result)

    def test_3_success(self):
        result = solve(3)
        self.assertEqual(6, result)

    def test_10_success(self):
        result = solve(10)
        self.assertEqual(221542, result)

    def test_20_success(self):
        result = solve(20)
        self.assertIsNotNone(result)


if __name__ == '__main__':
    unittest.main()
