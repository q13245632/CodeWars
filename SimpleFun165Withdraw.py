# -*-coding:utf8 -*-
# author: yushan
# date: 2017-02-25


# 自己的解法
def withdraw(n):
    lst = []
    h = 0
    f = 0
    t = 0
    h = n / 100
    m = n % 100
    if m == 10 or m == 30:
        h = h - 1
        m = 100 + m
        f = 1
        t = (m - 50) / 20
    elif m == 50:
        f = 1
        t = 0
    elif m < 70:
        f = 0
        t = m / 20
    elif m == 80:
        f = 0
        t = m / 20
    else:
        f = 1
        t = (m - 50) / 20
    lst.append(h)
    lst.append(f)
    lst.append(t)
    return lst


# 思路很棒
def withdraw2(n):
    n50 = 0
    n20, r = divmod(n, 20)
    if r == 10:
        n20 -= 2
        n50 += 1
    n100, n20 = divmod(n20, 5)
    return [n100, n50, n20]

# 遍历
def withdraw(n):
    return sorted([[b100, b50, b20] for b100 in range(n // 100 + 1) for b50 in range(2) for b20 in range(5) if b100 * 100 + b50 * 50 + b20 * 20 == n], key=sum)[0]


def withdraw(n):
    n, k = (n - 60, 3) if n % 100 in [10, 30, 60, 80] else (n, 0)
    return [n // 100, n % 100 // 50, n % 100 % 50 // 20 + k]


print withdraw(40)
print withdraw(250)
print withdraw(260)
print withdraw(230)
print withdraw(60)
print withdraw(280)