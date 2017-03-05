# -*- coding:utf-8 -*-
# author: yushan
# date: 2017-03-05


# 自己的解法
def checkchoose(m, n):
    if m == n:
        return 1
    njie = reduce(lambda a,b:a*b,xrange(1,n+1))
    num = -1
    for i in xrange(1,n):
        ijie = reduce(lambda a,b:a*b,xrange(1,i+1))
        n_i = reduce(lambda a,b:a*b,xrange(1,n-i+1))
        if njie / (ijie * n_i) == m:
            num = i
            break
    return num


from math import factorial as fac
def checkchoose(m, n):
    for x in range(0, n+1):
        if fac(n)/(fac(x)*fac(n-x))== m:
            return x
    return -1

print checkchoose(6,4)
print checkchoose(4, 4)
print checkchoose(4, 2)
# Test.describe("Basic tests")
# Test.it("Smaller numbers")
# Test.assert_equals(checkchoose(6, 4), 2)
# Test.assert_equals(checkchoose(4, 4), 1)
# Test.assert_equals(checkchoose(4, 2), -1)
# Test.assert_equals(checkchoose(35, 7), 3)
# Test.assert_equals(checkchoose(36, 7), -1)