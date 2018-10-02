#!/usr/bin/env python3
import unittest


def merge(*arrays):
    result = []
    total = sum((len(i) for i in arrays))

    while len(result) < total:
        fronts = [(value[0], value) for value in arrays if value]
        _, array = min(fronts, key=lambda x: x[0])
        result.append(array.pop(0))

    return result


class TestSolution(unittest.TestCase):
    def test_merge_two_success(self):
        result = merge([1, 3, 5], [2, 4])
        self.assertEqual([1, 2, 3, 4, 5], result)

    def test_merge_three_success(self):
        result = merge([1, 3, 5], [2, 2, 2], [2, 4])
        self.assertEqual([1, 2, 2, 2, 2, 3, 4, 5], result)


if __name__ == '__main__':
    unittest.main()
