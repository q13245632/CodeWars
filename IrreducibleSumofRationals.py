# -*-coding:utf8 -*-
# 自己的解法
def ahcf(i,j):
    a = max(i,j)
    b = min(i,j)
    if a == 1 or b == 1:
        return 1
    else:
        while a % b != 0:
            temp = a % b
            a = b
            b = temp
            print a," ",b
        return b

def sum_fracts(lst):
    if not lst:
        return None
    else:
        m = 1
        for x in lst:
            m = m * x[1]
            print m
        n = sum([i[0] * m / i[1] for i in lst])
        print n
        if n % m == 0:
            return n / m
        else:
            print m,"   ",n
            x = ahcf(m,n)
            print x
            m = m / x
            n = n / x
            lst_n = []
            lst_n.append(n)
            lst_n.append(m)
            return lst_n


# test.assert_equals(sum_fracts([[1, 2], [1, 3], [1, 4]]), [13, 12])
# test.assert_equals(sum_fracts([[1, 3], [5, 3]]), 2)

# 简化程序
from fractions import Fraction

def sum_fracts(lst):
    if lst:
        ret = sum(Fraction(a, b) for (a, b) in lst)
        return ret.numerator if ret.denominator == 1 else [ret.numerator, ret.denominator]


from fractions import Fraction
def sum_fracts(lst):
    s = sum(Fraction(*f) for f in lst)
    if s: return s.numerator if s.denominator == 1 else [s.numerator, s.denominator]