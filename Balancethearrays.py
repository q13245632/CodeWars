# -*-coding:utf8 -*-
# 自己的解法
import collections
def balance(arr1, arr2):
    lst_1 = []
    lst_2 = []
    c1 = collections.Counter(arr1)
    c2 = collections.Counter(arr2)
    for x in list(set(arr1)):
        lst_1.append(c1[x])
    for a in list(set(arr2)):
        lst_2.append(c2[a])
    lst_1.sort()
    lst_2.sort()
    return lst_1 == lst_2

# 测试集
# test.describe("Example Tests")
# array1 = ["a","a","a","a","a","b","b","b"]
# array2 = ["c","c","c","c","c","d","d","d"]
# test.assert_equals(balance(array1, array2), True)
#
# array1 = ["a","a"]
# array2 = ["c"]
# test.assert_equals(balance(array1, array2), False)
#
# array1 = ["a","b","c","d","e","f","g","g"]
# array2 = ["h","h","i","j","k","l","m","n"]
# test.assert_equals(balance(array1, array2), True)
#
# array1 = ["a"]
# array2 = ["c"]
# test.assert_equals(balance(array1, array2), True)
#
# array1 = ["a","b","c","d","e","f","g","g"]
# array2 = ["h","h","i","j","k","l","m","m"]
# test.assert_equals(balance(array1, array2), False)

from collections import Counter

def balance(arr1, arr2):
    return sorted(Counter(arr1).values()) == sorted(Counter(arr2).values())

