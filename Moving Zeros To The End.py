# -*- coding:utf-8 -*-
# author: yushan
# date: 2017-03-09


def move_zeros(array):
    zeros = []
    lst = []
    for i in array:
        if (type(i) == int or type(i) == float) and int(i) == 0:
            zeros.append(0)
        else:
            lst.append(i)
    lst.extend(zeros)
    return lst

def move_zeros(array):
    return sorted(array, key= lambda x: x == 0 and type(x) != bool)