# -*- coding:utf-8 -*-
# author: yushan
# date: 2017-04-08



def smaller(arr):
    lst = []
    n = len(arr)
    for i in xrange(n):
        k = 0
        for j in xrange(i,n):
            if arr[j] < arr[i]:
                k += 1
        lst.append(k)
    return lst


# Test.describe("Basic Tests")
# Test.assert_equals(smaller([5, 4, 3, 2, 1]), [4, 3, 2, 1, 0])
# Test.assert_equals(smaller([1, 2, 3]), [0, 0, 0])
# Test.assert_equals(smaller([1, 2, 0]), [1, 1, 0])
# Test.assert_equals(smaller([1, 2, 1]), [0, 1, 0])
# Test.assert_equals(smaller([1, 1, -1, 0, 0]), [3, 3, 0, 0, 0])
# Test.assert_equals(smaller([5, 4, 7, 9, 2, 4, 4, 5, 6]), [4, 1, 5, 5, 0, 0, 0, 0, 0])


def smaller(arr):
    # Good Luck!
    return [len([a for a in arr[i:] if a < arr[i]]) for i in range(0, len(arr))]

def smaller(arr):
    return [sum(b < a for b in arr[i + 1:]) for i, a in enumerate(arr)]