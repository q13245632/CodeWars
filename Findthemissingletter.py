# -*-coding:utf8-*-
# 自己的解法
def find_missing_letter(chars):
    char = ''
    for x in xrange(len(chars) - 1):
        if ord(chars[x+1]) - ord(chars[x]) != 1:
            char = chr(ord(chars[x])+1)
    return char

# 思路不同
def find_missing_letter(chars):
    chk = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    start = chk.find(chars[0])
    return (set(chk[start:start + len(chars)]) - set(chars)).pop()