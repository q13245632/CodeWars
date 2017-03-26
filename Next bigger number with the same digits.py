# -*- coding:utf-8 -*-
# author: yushan
# date: 2017-03-23

def next_bigger(num):
    digits = [int(i) for i in str(num)]
    idx = len(digits) - 1
    while idx >= 1 and digits[idx-1] >= digits[idx]:
        idx -= 1
    if idx == 0:
        return -1
    pivot = digits[idx-1]
    swap_idx = len(digits) - 1
    while pivot >= digits[swap_idx]:
        swap_idx -= 1
    digits[swap_idx], digits[idx-1] = digits[idx-1], digits[swap_idx]
    digits[idx:] = digits[:idx-1:-1]
    return int(''.join(str(x) for x in digits))

def next_bigger(n):
    n = str(n)[::-1]
    try:
        i = min(i + 1 for i in range(len(n[:-1])) if n[i] > n[i + 1])
        j = n[:i].index(min([a for a in n[:i] if a > n[i]]))
        return int(n[i + 1::][::-1] + n[j] + ''.join(sorted(n[j + 1:i + 1] + n[:j])))
    except:
        return -1
# Test.assert_equals(next_bigger(12),21)
# Test.assert_equals(next_bigger(513),531)
# Test.assert_equals(next_bigger(2017),2071)
# Test.assert_equals(next_bigger(414),441)
# Test.assert_equals(next_bigger(144),414)