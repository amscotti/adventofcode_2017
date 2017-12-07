#!/usr/bin/env python


import itertools
import unittest


def iter_coords():
    yield (0, 0)
    incr = 0
    x = 1
    y = 0
    while True:
        incr += 2
        top = y + incr - 1
        bot = y - 1
        left = x - incr
        right = x
        yield (x, y)
        while y < top:
            y += 1
            yield (x, y)
        while x > left:
            x -= 1
            yield (x, y)
        while y > bot:
            y -= 1
            yield (x, y)
        while x < right:
            x += 1
            yield (x, y)
        x += 1


def manhattan_distance(item):
    ex, ey = next(itertools.islice(iter_coords(), item-1, item))
    return abs(ex) + abs(ey)


def iter_stress_test():
    data = {}
    iter = iter_coords()

    data[next(iter)] = 1
    yield 1

    for item in iter:
        x, y = item
        val = data.get((x - 1, y - 1), 0)
        val += data.get((x - 1, y), 0)
        val += data.get((x - 1, y + 1), 0)
        val += data.get((x, y - 1), 0)
        val += data.get((x, y + 1), 0)
        val += data.get((x + 1, y - 1), 0)
        val += data.get((x + 1, y), 0)
        val += data.get((x + 1, y + 1), 0)

        data[item] = val
        yield val


def stress_test(item):
    return next(x for x in iter_stress_test() if x > item)


class TestManhattanDistance(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(manhattan_distance(1), 0)

    def test_case_2(self):
        self.assertEqual(manhattan_distance(12), 3)

    def test_case_3(self):
        self.assertEqual(manhattan_distance(23), 2)

    def test_case_4(self):
        self.assertEqual(manhattan_distance(1024), 31)


class TestStressTest(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(stress_test(1), 2)

    def test_case_2(self):
        self.assertEqual(stress_test(2), 4)

    def test_case_3(self):
        self.assertEqual(stress_test(3), 4)

    def test_case_4(self):
        self.assertEqual(stress_test(4), 5)

    def test_case_5(self):
        self.assertEqual(stress_test(5), 10)

    def test_case_more(self):
        self.assertEqual(stress_test(312051), 312453)


if __name__ == '__main__':
    unittest.main()
