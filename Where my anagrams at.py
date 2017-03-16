# -*- coding:utf-8 -*-
# author: yushan
# date: 2017-03-16


def anagrams(word, words):
    return [i for i in words if sorted(i) == sorted(word)]


def anagrams(word, words):
    lst = []
    word = sorted(word)
    for i in words:
        if word == sorted(i):
            lst.append(i)
    return lst

# anagrams('laser', ['lazing', 'lazy', 'lacer']) = > []
# Test.assert_equals(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']), ['aabb', 'bbaa'])
# Test.assert_equals(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']), ['carer', 'racer'])