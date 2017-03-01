# -*-coding:utf8 -*-
# author: yushan
# date: 2017-02-28


# 自己的解法
def solution(number):
    a = sum([i for i in xrange(0,number,3)])
    b = sum([i for i in xrange(0,number,5) if i % 3 !=0])
    return a + b

def solution(number):
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)


# test.describe("Multiples of 3 and 5")
#
# test.it("should handle basic cases")
# test.assert_equals(solution(10), 23)
