# -*- coding:utf-8 -*-
# author: yushan
# date: 2017-03-20


def whoIsNext(names, r):
    n = len(names)
    if r < n:
        return names[r - 1]
    i = 0
    f = n * (2 ** i)
    r -= f
    while r > 0:
        i += 1
        f = n * (2 ** i)
        r -= f
    r += (n * (2 ** i))
    return names[(r / (2 ** i))]


def whoIsNext(names, r):
    while r > 5:
        r = (r - 4) / 2
    return names[r-1]