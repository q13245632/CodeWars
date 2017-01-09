# -*-coding:utf8 -*-
# 自己的解法
def longest_repetition(chars):
    if chars is None or len(chars) == 0:
        return ("",0)
    pattern = chars[0]
    char = ""
    c_max = 0
    count = 1
    for s in xrange(1,len(chars)):
        print chars[s]
        if chars[s] == pattern:
            count += 1
        else:
            if c_max < count:
                c_max = count
                char = chars[s-1]
            pattern = chars[s]
            count = 1
    if c_max < count:
        c_max = count
        char = chars[len(chars) - 1]
    return (char,c_max)


# 其他解法
def longest_repetition(chars):
    from itertools import groupby
    return max(((char, len(list(group))) for char, group in groupby(chars)),
               key=lambda char_group: char_group[1], default=("", 0))


import re


def longest_repetition(chars):
    if not chars: return ("", 0)

    longest = max(re.findall(r"((.)\2*)", chars), key=lambda x: len(x[0]))
    return (longest[1], len(longest[0]))

