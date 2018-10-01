#!/usr/bin/env python3
import unittest


class MinStack:
    def __init__(self):
        self._values = []
        self._min_values = []

    def is_empty(self):
        return len(self._values) == 0

    def min(self):
        return self._min_values[-1] if self._min_values else None

    def top(self):
        return self._values[-1] if self._values else None

    def add(self, item):
        if self.is_empty() or item <= self.min():
            self._min_values.append(item)

        self._values.append(item)

    def remove(self):
        if self.is_empty():
            return

        item = self._values.pop(-1)
        if item == self.min():
            self._min_values.pop(-1)


class TestSolution(unittest.TestCase):
    def test_usage_add_one_success(self):
        stack = MinStack()
        stack.add(1)
        self.assertEqual(1, stack.top())
        self.assertEqual(1, stack.min())

    def test_usage_increment_values_success(self):
        stack = MinStack()
        stack.add(1)
        stack.add(2)
        stack.add(3)
        self.assertEqual(3, stack.top())
        self.assertEqual(1, stack.min())

    def test_usage_decrement_values_success(self):
        stack = MinStack()
        stack.add(3)
        stack.add(2)
        stack.add(1)
        self.assertEqual(1, stack.top())
        self.assertEqual(1, stack.min())

    def test_usage_remove_success(self):
        stack = MinStack()
        stack.add(3)
        stack.add(2)
        stack.add(1)

        stack.remove()
        self.assertEqual(2, stack.top())
        self.assertEqual(2, stack.min())

    def test_usage_duplicates_success(self):
        stack = MinStack()
        stack.add(2)
        stack.add(3)
        stack.add(2)
        stack.add(4)

        stack.remove()
        self.assertEqual(2, stack.top())
        self.assertEqual(2, stack.min())

        stack.remove()
        self.assertEqual(3, stack.top())
        self.assertEqual(2, stack.min())

        stack.remove()
        self.assertEqual(2, stack.top())
        self.assertEqual(2, stack.min())





if __name__ == '__main__':
    unittest.main()
