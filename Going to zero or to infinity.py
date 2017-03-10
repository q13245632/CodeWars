# -*- coding:utf-8 -*-
# author: yushan
# date: 2017-03-10


import math
import decimal
def going(n):
    m = sum([math.factorial(x) for x in xrange(1,n)])
    n_fac = math.factorial(n)
    f =  1 + decimal.Decimal(m) / n_fac
    return f if len(str(f)) <=8 else float(str(f)[:8])


def going(n):
    factor = 1.0
    acc = 1.0
    for i in range(n, 1, -1):
        factor *= 1.0 / i
        acc += factor
    return int(acc * 1e6) / 1e6