# -*- coding:utf-8 -*-
# author: yushan
# date: 2017-03-11


def productFib(prod):
    a = 0
    b = 1
    while a * b < prod:
        temp = a
        a = b
        b = temp + a
    return [a,b,True] if a * b == prod else [a,b,False]


def productFib(prod):
    a, b = 0, 1
    while prod > a * b:
        a, b = b, a + b
    return [a, b, prod == a * b]
# test.assert_equals(productFib(4895), [55, 89, True])
# test.assert_equals(productFib(5895), [89, 144, False])