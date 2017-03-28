# -*- coding:utf-8 -*-
# author: yushan
# date: 2017-03-27

from collections import Counter
def first_non_repeating_letter(string):
    string_copy = string.lower()
    counter = Counter(string_copy)
    index = len(string)
    ch = ""
    for k,v in counter.items():
        if v == 1 and string_copy.index(k) < index:
            index = string_copy.index(k)
            ch = k
    return ch if ch in string else ch.upper()


def first_non_repeating_letter(string):
    string_lower = string.lower()
    for i, letter in enumerate(string_lower):
        if string_lower.count(letter) == 1:
            return string[i]
    return ""
# Test.describe('Basic Tests')
# Test.it('should handle simple tests')
# Test.assert_equals(first_non_repeating_letter('a'), 'a')
# Test.assert_equals(first_non_repeating_letter('stress'), 't')
# Test.assert_equals(first_non_repeating_letter('moonmen'), 'e')
#
# Test.it('should handle empty strings')
# Test.assert_equals(first_non_repeating_letter(''), '')
#
# Test.it('should handle all repeating strings')
# Test.assert_equals(first_non_repeating_letter('abba'), '')
# Test.assert_equals(first_non_repeating_letter('aa'), '')
#
# Test.it('should handle odd characters')
# Test.assert_equals(first_non_repeating_letter('~><#~><'), '#')
# Test.assert_equals(first_non_repeating_letter('hello world, eh?'), 'w')
#
# Test.it('should handle letter cases')
# Test.assert_equals(first_non_repeating_letter('sTreSS'), 'T')
# Test.assert_equals(first_non_repeating_letter('Go hang a salami, I\'m a lasagna hog!'), ',')