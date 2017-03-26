# -*- coding:utf-8 -*-
# author: yushan
# date: 2017-03-23


def calc(expr):
    if not expr:return 0
    lst = expr.split(" ")
    stack = []
    for i in lst:
        if i.isdigit():
            stack.append(int(i))
        if "." in i:
            stack.append(float(i))
        if i == "+":
            a = stack[-1]
            b = stack[-2]
            c = a + b
            stack = stack[:-2] + [c]
        if i == "-":
            a = stack[-1]
            b = stack[-2]
            c = b - a
            stack = stack[:-2] + [c]
        if i == "*":
            a = stack[-1]
            b = stack[-2]
            c = b * a
            stack = stack[:-2] + [c]
        if i == "/":
            a = stack[-1]
            b = stack[-2]
            c = b / a
            stack = stack[:-2] + [c]
    return stack[-1] if stack[-1] else 0


import operator

def calc(expr):
    OPERATORS = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    stack = [0]
    for token in expr.split(" "):
        if token in OPERATORS:
            op2, op1 = stack.pop(), stack.pop()
            stack.append(OPERATORS[token](op1, op2))
        elif token:
            stack.append(float(token))
    return stack.pop()

# Test.assert_equals(calc(""), 0, "Should work with empty string")
# Test.assert_equals(calc("1 2 3"), 3, "Should parse numbers")
# Test.assert_equals(calc("1 2 3.5"), 3.5, "Should parse float numbers")
# Test.assert_equals(calc("1 3 +"), 4, "Should support addition")
# Test.assert_equals(calc("1 3 *"), 3, "Should support multiplication")
# Test.assert_equals(calc("1 3 -"), -2, "Should support subtraction")
# Test.assert_equals(calc("4 2 /"), 2, "Should support division")