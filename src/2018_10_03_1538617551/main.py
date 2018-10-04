#!/usr/bin/env python3
import unittest


def solve(value: str) -> []:
    seen = dict()
    valid = []
    for i, x in enumerate(value):
        if x.isdigit():
            x = int(x)
            diff = 10 - x
            if diff in seen:
                n = value.count('?', seen[diff], i)
                if n == 3:
                    valid.append(((seen[diff], diff), (i, x)))
                else:
                    return False
            else:
                seen[x] = i

    return valid


class TestSolution(unittest.TestCase):
    def test_case_1_success(self):
        result = solve('arrb6???4xxbl5???eee5')
        self.assertTrue(result)

    def test_case_2_success(self):
        result = solve('acc?7??sss?3rr1??????5')
        self.assertTrue(result)

    def test_case_3_fail(self):
        result = solve('5??aaaaaaaaaaaaaaaaaaa?5?5')
        self.assertFalse(result)

    def test_case_4_success(self):
        result = solve('9???1???9???1???9')
        self.assertTrue(result)

    def test_case_5_success(self):
        result = solve('aa6?9')
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
