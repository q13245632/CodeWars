# -*- coding:utf-8 -*-
# author: yushan
# date: 2017-03-11


def perimeter(n):
    a,b = 1,1
    num = 2
    for _ in xrange(n - 1):
        a,b = b,a+b
        num += b
    return 4 * num


def fib(n):
    a, b = 0, 1

    for i in range(n + 1):
        if i == 0:
            yield b
        else:
            a, b = b, a + b
            yield b
def perimeter(n):
    return sum(fib(n)) * 4



def perimeter(n):
    a, b = 1, 2
    while n:
        a, b, n = b, a + b, n - 1
    return 4 * (b - 1)

test.assert_equals(perimeter(5), 80)
test.assert_equals(perimeter(7), 216)
test.assert_equals(perimeter(20), 114624)
test.assert_equals(perimeter(30), 14098308)
test.assert_equals(perimeter(100), 6002082144827584333104)