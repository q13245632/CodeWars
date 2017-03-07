# -*- coding:utf-8 -*-
# author: yushan
# date: 2017-03-03


# 自己的解法
from collections import Counter
def group(arr):
    s = set(arr)
    c = Counter(arr)
    lst = []
    for i in arr:
        item = [i]
        if s.__contains__(i) and c[i] > 1:
            for _ in xrange(c[i]-1):
                item.append(i)
        elif s.__contains__(i) and c[i] == 1:
            item = item
        else:
            continue
        lst.append(item)
        s.remove(i)
    return lst


from collections import Counter

def group(a):
    return sorted([[k]*v for k, v in Counter(a).items()], key=lambda k: a.index(k[0]))

# Test.describe("Basic tests")
# Test.assert_equals(group([3, 2, 6, 2, 1, 3]), [[3, 3], [2, 2], [6], [1]])
# Test.assert_equals(group([3, 2, 6, 2]), [[3], [2, 2], [6]])
# Test.assert_equals(group([]), [])
# Test.assert_equals(group([1, 100, 4, 2, 4]), [[1], [100], [4, 4], [2]])
# Test.assert_equals(group([-1, 1, -1]), [[-1, -1], [1]])