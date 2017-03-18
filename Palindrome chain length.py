# -*- coding:utf-8 -*-
# author: yushan
# date: 2017-03-17
def palindrome_chain_length(n):
    k = n
    num = 0
    while k != int("".join(list(str(k))[::-1])):
        k += int("".join(list(str(k))[::-1]))
        num += 1
    return num

def palindrome_chain_length(n, count=0):
    if str(n) == str(n)[::-1]: return count
    else: return palindrome_chain_length(n + int(str(n)[::-1]), count+1)
# test.assert_equals(palindrome_chain_length(87), 4)
