# -*-coding:utf8-*-
# 自己解法
def permutation_position(perm):
    lst = list(perm)
    lst.reverse()
    num = 0
    for i in xrange(len(lst)):
        num += (ord(lst[i]) - ord("a")) * (26 ** i)
    return num + 1

# 简化程序
permutation_position = lambda x : 1 + sum([ (ord(c) - (ord('a'))) * (26 ** i) for i,c in enumerate(x[::-1])])
