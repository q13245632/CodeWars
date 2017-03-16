# -*- coding:utf-8 -*-
# author: yushan
# date: 2017-03-14

import math
def same_col_seq(val, k, col):
    n = int(math.floor(math.sqrt(2*val)))
    print n
    color = {1:"red",2:"yellow",0:"blue"}
    lst = []
    if col == "yellow":return []
    while k > 0:
        num = n*(n+1)/2
        if num > val and color[num%3] == col:
            lst.append(num)
            k -= 1
        n += 1
    return lst

print same_col_seq(917024,16,"red")
# [917335, 921403, 925480, 929566, 933661, 937765, 941878, 946000, 950131, 954271, 958420, 962578, 966745, 970921, 975106, 979300]

D, R = {}, [[], [], []]
for i in range(10000):
    D[i] = D.get(i - 1, 0) + i
    R[D[i] % 3].append(D[i])


def same_col_seq(val, k, col):
    r = ['blue', 'red', 'yellow'].index(col)
    return [e for e in R[r] if e > val][:k]
