# -*- coding:utf-8 -*-
# author: yushan
# date: 2017-03-11


def triple_double(num1, num2):
    return any([i * 3 in str(num1) and i * 2 in str(num2) for i in '0123456789'])

def triple_double(num1, num2):
    str1 = str(num1)
    str2 = str(num2)
    has = False
    for i in xrange(len(str2) - 1):
        temp2 = None
        if str2[i:i+1] == str2[i+1:i+2]:
            temp2 = str2[i:i+1] * 3
        temp = str2[i:i+2]
        if temp2:
            if temp in str1 and temp2 in str1:
                has = True
    return 1 if has else 0