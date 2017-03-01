# -*-coding:utf8 -*-
# author: yushan
# date: 2017-02-28


# 自己的解法
from itertools import groupby, dropwhile, tee, islice

def sum_groups(arr):
    def it(a):
        while 1:
            yield a
            a = [sum(g) for _, g in groupby(a, key=lambda k: k % 2)]
    it1, it2 = tee(it(arr))
    return len(next(dropwhile(lambda x: x[0] != x[1], zip(it1, islice(it2, 1, None))))[1])


import itertools

def sum_groups(arr):
    prev_len = 1
    while prev_len != len(arr):
        prev_len = len(arr)
        arr = [
            sum(g) for k, g in itertools.groupby(
                arr, key=lambda x: x % 2 == 0
            )
        ]
    return len(arr)