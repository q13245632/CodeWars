# -*- coding:utf-8 -*-
# author: yushan
# date: 2017-03-23


import itertools
def permutations(string):
    lst = itertools.permutations(string)
    lst = list(set(["".join(i) for i in lst]))
    return lst



import itertools

def permutations(string):
    return list("".join(p) for p in set(itertools.permutations(string)))