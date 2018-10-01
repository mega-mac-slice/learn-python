#!/usr/bin/env python3
import unittest
from collections import Counter
from typing import List, Tuple


def word_frequency(text: str) -> List[Tuple[str, int]]:
    tokens = text.split()
    counter = Counter(tokens)
    return [i for i in sorted(counter.items(), key=lambda x: x[1], reverse=True)]


class TestSolution(unittest.TestCase):
    def test_short_success(self):
        text = 'big is big'
        result = word_frequency(text)
        self.assertEqual(('big', 2), result[0])

    def test_medium_success(self):
        text = 'a pig goes to market but only pig is allowed to eat at market because it is pig'
        result = word_frequency(text)
        self.assertEqual(('pig', 3), result[0])


if __name__ == '__main__':
    unittest.main()
