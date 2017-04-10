# -*- coding:utf-8 -*-
# author: yushan
# date: 2017-04-08


def middle_permutation(string):
    s = "".join(sorted(string))
    mid = int(len(s) / 2) - 1
    if len(s) % 2 == 0:
        return s[mid] + (s[:mid] + s[mid + 1:])[::-1]
    else:
        return s[mid:mid + 2][::-1] + (s[:mid] + s[mid + 2:])[::-1]

# Test.describe("Basic tests")
# Test.assert_equals(middle_permutation("abc"),"bac")
# Test.assert_equals(middle_permutation("abcd"),"bdca")
# Test.assert_equals(middle_permutation("abcdx"),"cbxda")
# Test.assert_equals(middle_permutation("abcdxg"),"cxgdba")
# Test.assert_equals(middle_permutation("abcdxgz"),"dczxgba")