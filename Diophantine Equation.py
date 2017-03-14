# -*- coding:utf-8 -*-
# author: yushan
# date: 2017-03-14


import math
def sol_equa(n):
    lst = []
    for i in xrange(1,int(math.sqrt(n)) + 1):
        if n % i == 0:
            k = n // i
            x = (i+k) // 2
            k = (x-i) // 2
            if x >=0 and k >= 0 and (x-2*k)*(x+2*k) == n:
                lst.append([x,k])
    return sorted(lst,key=lambda x:x[0],reverse=True)


def sol_equa(n):
    return [[(i + n / i) / 2, (n / i - i) / 4] for i in range(1, int(n ** 0.5) + 1, 1) if
                n % i == 0 and (n / i - i) % 4 == 0]
    
# test.assert_equals(sol_equa(12), [[4, 1]])
# test.assert_equals(sol_equa(13), [[7, 3]])
# test.assert_equals(sol_equa(16), [[4, 0]])
# test.assert_equals(sol_equa(17), [[9, 4]])