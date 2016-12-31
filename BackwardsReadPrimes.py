# -*-coding:utf8 -*-
# 自己的解法
import math
def backwardsPrime(start, stop):
    print start, "  ",stop
    lst = []
    for x in xrange(start,stop+1):
        y = int(str(x)[::-1])
        if x != y and isPrime(x) and isPrime(y):
            lst.append(x)
    return lst
def isPrime(num):
    return all(num % i != 0 for i in xrange(2,int(math.sqrt(num))+1))

# 测试集
# a = [9923, 9931, 9941, 9967]
# test.assert_equals(backwardsPrime(9900, 10000), a)

def backwardsPrime(start, nd):
    return [i for i in xrange(start, nd + 1) if i != int(str(i)[::-1]) and isPrime(i) and isPrime(int(str(i)[::-1]))]

def isPrime(n):
    return all([n % i != 0 for i in xrange(2, int(n ** .5) + 1)])
