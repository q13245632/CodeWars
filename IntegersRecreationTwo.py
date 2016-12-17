# -*-coding:utf8-*-
# 自己解法
def prod2sum(a, b, c, d):
    a = abs(a)
    b = abs(b)
    c = abs(c)
    d = abs(d)
    lst = []
    item = []
    x = a * c
    y = a * d
    m = b * c
    n = b * d
    i = abs(y - m)
    item.append(i)
    j = x + n
    item.append(j)
    item.sort()
    lst.append(item)
    k = abs(x - n)
    if item[0] != k and item[1] != k:
        item = []
        item.append(k)
        l = y + m
        item.append(l)
        item.sort()
        lst.append(item)
        lst = sorted(lst, cmp=lambda x, y: cmp(x[0], y[0]))
    return lst

# 简化程序
def prod2sum(a, b, c, d):
    l1 = sorted([abs(a*c+b*d),abs(a*d-b*c)])
    l2 = sorted([abs(a*c-b*d),abs(a*d+b*c)])
    if l1==l2:
        return [l1]
    else:
        return sorted([l1,l2])

# 一行代码
prod2sum = lambda a, b, c, d: sorted(map(list, {tuple(sorted(map(abs, s))) for s in ((a*c - b*d, a*d + b*c), (a*d - b*c, a*c + b*d))}))


