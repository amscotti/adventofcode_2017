#!/usr/bin/env python

import unittest


def row_evenly_divisible(row):
    number_row = sorted([int(i) for i in row.split(" ")], reverse=True)
    for idx, item in enumerate(number_row):
        for x in range(len(number_row)-1, idx+1, -1):
            if item % number_row[x] is 0:
                return int(item / number_row[x])


def row_delta(row):
    number_row = [int(i) for i in row.split(" ")]
    return max(number_row) - min(number_row)


def corruption_checksum(spreadsheet, row_func):
    return sum([row_func(row) for row in spreadsheet.split("\n")])


class TestFindRowDelta(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(row_delta("5 1 9 5"), 8)

    def test_case_2(self):
        self.assertEqual(row_delta("7 5 3"), 4)

    def test_case_3(self):
        self.assertEqual(row_delta("2 4 6 8"), 6)


class TestFindRowEvenlyDivisible(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(row_evenly_divisible("5 9 2 8"), 4)

    def test_case_2(self):
        self.assertEqual(row_evenly_divisible("9 4 7 3"), 3)

    def test_case_3(self):
        self.assertEqual(row_evenly_divisible("3 8 6 5"), 2)


class TestFindCorruptionChecksum(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(corruption_checksum("5 1 9 5\n7 5 3\n2 4 6 8", row_delta), 18)

    def test_case_2(self):
        self.assertEqual(corruption_checksum("5 9 2 8\n9 4 7 3\n3 8 6 5", row_evenly_divisible), 9)


if __name__ == '__main__':
    unittest.main()
