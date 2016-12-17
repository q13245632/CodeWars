# -*-coding:utf8 -*-
# 自己的解法
def est_subsets(arr):
    lst = set(arr)
    return (2**(len(lst)) - 1)  

# 简化思路
est_subsets = lambda arr: 2 ** (len(set(arr))) - 1