# -*-coding:utf8 -*-
# author: yushan
# date: 2017-02-27


# 自己的解法
def comp(array1, array2):
    print array1
    print array2
    if array1 == None or array2 == None:
        return False
    arr1 = set(array1)
    arr2 = set(array2)
    if len(arr1) != len(arr2):
        return False
    for i in arr1:
        if arr2.__contains__(i * i):
            arr2.remove(i * i)
    if len(arr2) > 0:
        return False
    return True

# 题意为相同长度的两个数组，i 与 i*i 一一对应时返回True
def comp(array1, array2):
    try:
        return sorted([i ** 2 for i in array1]) == sorted(array2)
    except:
        return False
