#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Crossword Solver Program"""

__author__ = "Patrick Buzzo"


import re


def find_words(word_part):
    re_word = r''
    for i in word_part:
        if i == '?':
            re_word += '\w'
        else:
            re_word += i
    with open('dictionary.txt', 'r') as dt:
        read = dt.read()
        matches = re.findall(re_word, read)
        for line in matches:
            print(line)


# find_words('f???st')
def main():
    with open('dictionary.txt') as f:
        words = f.read().split()

    test_word = raw_input(
        'Please enter a word to solve.\nUse spaces to signify unknown letters (ex--> f??st): ').lower()
    find_words(test_word)


if __name__ == '__main__':
    main()
