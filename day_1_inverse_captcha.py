#!/usr/bin/env python

import unittest


def inverse_captcha_part_one(input_captcha):
    input_len = len(input_captcha)
    return sum([int(v) for idx, v in enumerate(input_captcha) if v is input_captcha[(idx + 1) % input_len]])


def inverse_captcha_part_two(input_captcha):
    input_len = len(input_captcha)
    return sum([int(v) for idx, v in enumerate(input_captcha)
                if v is input_captcha[(idx + int(input_len/2)) % input_len]])


class TestFindInverseCaptchaPartOne(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(inverse_captcha_part_one("1122"), 3)

    def test_case_2(self):
        self.assertEqual(inverse_captcha_part_one("1111"), 4)

    def test_case_3(self):
        self.assertEqual(inverse_captcha_part_one("1234"), 0)

    def test_case_4(self):
        self.assertEqual(inverse_captcha_part_one("91212129"), 9)


class TestFindInverseCaptchaPartTwo(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(inverse_captcha_part_two("1212"), 6)

    def test_case_2(self):
        self.assertEqual(inverse_captcha_part_two("1221"), 0)

    def test_case_3(self):
        self.assertEqual(inverse_captcha_part_two("123425"), 4)

    def test_case_4(self):
        self.assertEqual(inverse_captcha_part_two("123123"), 12)

    def test_case_5(self):
        self.assertEqual(inverse_captcha_part_two("12131415"), 4)


if __name__ == '__main__':
    unittest.main()
