# -*-coding:utf8 -*-
# 自己的解法
from itertools import combinations
def isCoPrime(a,b):
    c = 0
    max_n = max(a,b)
    min_n = min(a,b)
    if max_n % min_n == 0:
        c = min_n
    else:
        while True:
            temp = max_n % min_n
            if temp == 0:
                break
            else:
                max_n = min_n
                min_n = temp
    c = min_n
    if c == 1:
        return True
    else:
        return False

def fromNb2Str(n, modsys):
    mul = 1
    for a in modsys:
        mul = mul * a
    if mul <= n:
        return "Not applicable"
    if len(modsys) >= 2:
        lst = list(combinations(modsys,2))
        if not all([isCoPrime(b[0],b[1]) for b in lst]):
            return "Not applicable"
        else:
            string = "-"
            list_ = [str(n % x) for x in modsys]
            string += "--".join(list_) + "-"
            return string
    return "Not applicable"

# 简化程序
from fractions import gcd
from operator import mul
from itertools import combinations
def fromNb2Str(n, modsys):
    return '-' + '--'.join(str(n%i) for i in modsys) + '-' if reduce(mul, modsys) > n and all(x==1 for x in map(lambda x: gcd(*x), combinations(modsys,2))) else "Not applicable"

# 使用lambda表达式
from itertools import combinations
from fractions import gcd

def fromNb2Str(n, modsys):
    if reduce(lambda x, y: x * y, modsys) < n or any(gcd(i, j) != 1 for i, j in combinations(modsys, 2)):
        return "Not applicable"
    else:
        return "-" + "--".join(str(n % i) for i in modsys) + "-"

# 其他解法
from itertools import combinations
from functools import reduce
from operator import mul
from fractions import gcd

def lcm(a, b):
    return (a * b) // gcd(a, b)

def is_coprime_set(arr):
    return all(lcm(a, b) == a * b for a, b in combinations(arr, 2))

def fromNb2Str(n, modsys):
    if not is_coprime_set(modsys) or reduce(mul, modsys, 1) < n:
        return 'Not applicable'
    return '-' + '--'.join(str(n % m) for m in modsys) + '-'