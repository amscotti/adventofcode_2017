#!/usr/bin/env python

import unittest


def passphrase_validation(input_passphrase):
    word_list = input_passphrase.split(' ')
    return not [i for i in word_list if word_list.count(i) > 1]


def anagram(word_a, word_b):
    return word_a != word_b and sorted(word_a) == sorted(word_b)


def anagrams_passphrase_validation(input_passphrase):
    if not passphrase_validation(input_passphrase):
        return False
    else:
        word_list = input_passphrase.split(' ')
        for word in word_list:
            if len([i for i in word_list if anagram(word, i)]) > 0:
                return False
        return True


class TestPassphraseValidation(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(passphrase_validation("aa bb cc dd ee"), True)

    def test_case_2(self):
        self.assertEqual(passphrase_validation("aa bb cc dd aa"), False)

    def test_case_3(self):
        self.assertEqual(passphrase_validation("aa bb cc dd aaa"), True)

    def test_input_file(self):
        with open("day_4_input.txt", 'r') as input_file:
            self.assertEqual(sum([1 for line in input_file if passphrase_validation(line.strip())]), 466)


class TestAnagramsPassphraseValidation(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(anagrams_passphrase_validation("abcde fghij"), True)

    def test_case_2(self):
        self.assertEqual(anagrams_passphrase_validation("abcde xyz ecdab"), False)

    def test_case_3(self):
        self.assertEqual(anagrams_passphrase_validation("a ab abc abd abf abj"), True)

    def test_case_4(self):
        self.assertEqual(anagrams_passphrase_validation("iiii oiii ooii oooi oooo"), True)

    def test_case_5(self):
        self.assertEqual(anagrams_passphrase_validation("oiii ioii iioi iiio"), False)

    def test_input_file(self):
        with open("day_4_input.txt", 'r') as input_file:
            self.assertEqual(sum([1 for line in input_file if anagrams_passphrase_validation(line.strip())]), 251)


if __name__ == '__main__':
    unittest.main()
