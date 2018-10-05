#!/usr/bin/env python3
import unittest


def solve(arr: [], value: str) -> str:
    arr = set(arr)
    n = len(value)
    valid = []

    for i in range(n):
        for j in range(n):
            lhs = i
            rhs = j + 1

            token = value[lhs:rhs]
            print(token)
            if len(arr - set(token)) == 0:
                valid.append(token)

    if valid:
        return min(valid, key=lambda x: len(x))
    else:
        return ''


class TestSolution(unittest.TestCase):
    def test_success(self):
        result = solve(['x', 'y', 'z'], 'xyyzyzyx')
        self.assertEqual('zyx', result)

    def test_middle_success(self):
        result = solve(['x', 'y', 'z'], 'xxxxyzxxx')
        self.assertEqual('xyz', result)


if __name__ == '__main__':
    unittest.main()
