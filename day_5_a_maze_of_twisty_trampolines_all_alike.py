#!/usr/bin/env python

import unittest


def maze_of_jump(input_maze, offset):
    maze = [int(i) for i in input_maze.strip().split('\n')]
    length_of_maze = len(maze)
    position = 0
    steps = 0
    while length_of_maze > position:
        steps += 1
        jump = maze[position]
        maze[position] = offset(maze[position])
        position = position + jump
    return steps


class TestMazeOfJump(unittest.TestCase):
    def setUp(self):
        self.offset = lambda p: p + 1

    def test_case_1(self):
        self.assertEqual(maze_of_jump("0\n3\n0\n1\n-3", self.offset), 5)

    def test_case_2(self):
        self.assertEqual(maze_of_jump("0\n0\n0\n0\n0", self.offset), 10)

    def test_case_3(self):
        self.assertEqual(maze_of_jump("1\n2\n3\n-1\n0\n0", self.offset), 6)

    def test_input_file(self):
        with open("day_5_input.txt", 'r') as input_file:
            self.assertEqual(maze_of_jump(input_file.read(), self.offset), 354121)


class TestMazeOfJumpOffsetUpdate(unittest.TestCase):
    def setUp(self):
        self.offset = lambda p: p - 1 if p >= 3 else p + 1

    def test_case_1(self):
        self.assertEqual(maze_of_jump("0\n3\n0\n1\n-3", self.offset), 10)

    def test_case_2(self):
        self.assertEqual(maze_of_jump("0\n0\n0\n0\n0", self.offset), 10)

    def test_case_3(self):
        self.assertEqual(maze_of_jump("1\n2\n3\n-1\n0\n0", self.offset), 6)

    def test_input_file(self):
        with open("day_5_input.txt", 'r') as input_file:
            self.assertEqual(maze_of_jump(input_file.read(), self.offset), 27283023)


if __name__ == '__main__':
    unittest.main()
