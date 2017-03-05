# -*- coding:utf-8 -*-
# author: yushan
# date: 2017-03-05


# 自己的解法
from collections import Counter
def cut_the_ropes(arr):
    l = len(arr)
    cur = 0
    c = Counter(arr)
    s = sorted(set(arr))
    lst = []
    for k in s:
        lst.append(l)
        cur = c[k]
        l -= cur
    return lst


def cut_the_ropes(arr):
    results = [len(arr)]
    while arr:
        m = min(arr)
        arr = [elem - m for elem in arr if elem != m]
        results.append(len(arr))
    return results[:-1]


cut_the_ropes([1, 2, 3, 4, 3, 3, 2, 1])
# Test.describe("Basic Tests")
# Test.assert_equals(cut_the_ropes([3, 3, 2, 9, 7]),[5, 4, 2, 1])
# Test.assert_equals(cut_the_ropes([1, 2, 3, 4, 3, 3, 2, 1]),[8, 6, 4, 1])
# Test.assert_equals(cut_the_ropes([13035, 6618, 13056, 20912, 1119, 13035, 6618, 6618, 8482, 13056]),[10, 9, 6, 5, 3, 1])
# Test.assert_equals(cut_the_ropes([9, 9, 9, 9, 7]),[5, 4])
# Test.assert_equals(cut_the_ropes([3, 3, 2, 9, 7]),[5, 4, 2, 1])