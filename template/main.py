#!/usr/bin/env python3
import unittest


def solve():
    raise NotImplementedError()


class TestSolution(unittest.TestCase):
    def test_success(self):
        result = solve()
        self.assertIsNotNone(result)


if __name__ == '__main__':
    unittest.main()
