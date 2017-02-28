# -*-coding:utf8 -*-
# author: yushan
# date: 2017-02-28

from collections import Counter
# 自己的解法
def permute_a_palindrome (string):
    if string == None:
        return True
    c = Counter(string)
    odd = 0
    for k in c.itervalues():
        if k % 2 == 1:
            odd += 1
    return odd == 1 or odd == 0


def permute_a_palindrome(input):
    return sum(input.count(c) % 2 for c in set(input)) < 2


permute_a_palindrome = lambda s: bool(len(list(filter(lambda x: x % 2 != 0, [s.count(char) for char in set(s)]))) < 2)


# test.assert_equals(permute_a_palindrome("a"), True)
# test.assert_equals(permute_a_palindrome("aa"), True)
# test.assert_equals(permute_a_palindrome("baa"), True)
# test.assert_equals(permute_a_palindrome("aab"), True)
# test.assert_equals(permute_a_palindrome("baabcd"), False)
# test.assert_equals(permute_a_palindrome("racecars"), False)
# test.assert_equals(permute_a_palindrome("abcdefghba"), False)
# test.assert_equals(permute_a_palindrome(""), True)