#!/usr/bin/env python

import unittest


def memory_reallocation_generator(memory_input):
    yield memory_input
    while True:
        max_index = memory_input.index(max(memory_input))
        distribution = memory_input[max_index]
        memory_input[max_index] = 0
        for i in range(max_index + 1, distribution + max_index + 1):
            memory_input[i % len(memory_input)] += 1
        yield memory_input


def memory_reallocation(memory_input):
    state = []
    for memory in memory_reallocation_generator(memory_input):
        if state.count(memory):
            return len(state)
        else:
            state.append(list(memory))


def memory_reallocation_recycled(memory_input):
    state = []
    for memory in memory_reallocation_generator(memory_input):
        if state.count(memory) is 2:
            index = [i for i, x in enumerate(state) if x == memory]
            return index[1] - index[0]
        else:
            state.append(list(memory))


class TestMemoryReallocation(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(memory_reallocation([0, 2, 7, 0]), 5)

    def test_case_2(self):
        self.assertEqual(memory_reallocation([10, 3, 15, 10, 5, 15, 5, 15, 9, 2, 5, 8, 5, 2, 3, 6]), 14029)


class TestMemoryReallocationRecycled(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(memory_reallocation_recycled([0, 2, 7, 0]), 4)

    def test_case_2(self):
        self.assertEqual(memory_reallocation_recycled([10, 3, 15, 10, 5, 15, 5, 15, 9, 2, 5, 8, 5, 2, 3, 6]), 2765)


if __name__ == '__main__':
    unittest.main()
