# -*- coding:utf-8 -*-
# author: yushan
# date: 2017-03-14


def valid_parentheses(string):
    lst = []
    for i in string:
        if i == "(":
            lst.append(i)
        if i == ")":
            if len(lst) > 0:
                lst = lst[:-1]
            else:
                return False
    return True if len(lst) == 0 else False

def valid_parentheses(string):
    cnt = 0
    for char in string:
        if char == '(': cnt += 1
        if char == ')': cnt -= 1
        if cnt < 0: return False
        return True if cnt == 0 else False

import re

_regex = "[^\(|\)]"

def valid_parentheses(string):
    string = re.sub(_regex, '', string)
    while len(string.split('()')) > 1:
        string = ''.join(string.split('()'))
    return string == ''

# Test.assert_equals(valid_parentheses("  ("),False)
# Test.assert_equals(valid_parentheses(")test"),False)
# Test.assert_equals(valid_parentheses(""),True)
# Test.assert_equals(valid_parentheses("hi())("),False)
# Test.assert_equals(valid_parentheses("hi(hi)()"),True)