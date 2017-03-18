# -*- coding:utf-8 -*-
# author: yushan
# date: 2017-03-17


def zeros(n):
    five_k = 0
    temp = 5
    while n > temp:
        five_k += n // temp
        temp *= 5
    return five_k

print zeros(1000)
# test.assert_equals(zeros(12), 2)


def zeros(n):
  x = n/5
  return x+zeros(x) if x else 0