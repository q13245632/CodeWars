# -*-coding:utf8 -*-
# author: yushan
# date: 2017-02-26


# 自己的解法
def sqInRect(lng, wdth):
    if lng == wdth:
        return None
    else:
        lst = []
        max_lng = max(lng,wdth)
        max_wdth = min(lng,wdth)
        while max_lng != max_wdth:
            lst.append(max_wdth)
            temp = max_lng - max_wdth
            max_lng = max(max_wdth,temp)
            max_wdth = min(max_wdth,temp)  
        lst.append(max_lng)
        return lst


def sqInRect(lng, wdth, recur = 0):
    if lng == wdth:
        return (None, [lng])[recur]            # If this is original function call, return None for equal sides (per kata requirement);
                                               # if this is recursion call, we reached the smallest square, so get out of recursion.
    lesser = min(lng, wdth)
    return [lesser] + sqInRect(lesser, abs(lng - wdth), recur = 1)

sqInRect=s=lambda a,b,r=0:(None,[a])[r]if a==b else [min
                           (a,b)]+s(min(a,b),abs(a-b),1)


def sqInRect(lng, wdth):
    if lng != wdth:
        sqrs = []
        while lng and wdth:
            if wdth > lng: lng, wdth = wdth, lng
            sqrs.append(wdth)
            lng -= wdth
        return sqrs
sqInRect(5, 3)
sqInRect(3, 5)
# test.assert_equals(sqInRect(5, 5), None)
# test.assert_equals(sqInRect(5, 3), [3, 2, 1, 1])