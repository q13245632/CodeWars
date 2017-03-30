# -*- coding:utf-8 -*-
# author: yushan
# date: 2017-03-29


def same_structure_as(original, other):
    struct1 = check(original, "")
    struct2 = check(other, "")
    return struct1 == struct2


def check(arr, current):
    if type(arr) is list:
        current += '['
        for a in arr:
            if type(a) is list:
                current += check(a, current)
            else:
                current += 'x'

        current += ']'
    return current


# Test.assert_equals(same_structure_as([1,[1,1]],[2,[2,2]]),
#                    True, "[1,[1,1]] same as [2,[2,2]]")
# Test.assert_equals(same_structure_as([1,[1,1]],[[2,2],2]),
#                    False, "[1,[1,1]] not same as [[2,2],2]")

def same_structure_as(original,other):
    if isinstance(original, list) and isinstance(other, list) and len(original) == len(other):
        for o1, o2 in zip(original, other):
            if not same_structure_as(o1, o2): return False
        else: return True
    else: return not isinstance(original, list) and not isinstance(other, list)