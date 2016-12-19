# -*-coding:utf8 -*-
# 自己的解法
def bracket_pairs(string):
    dict_a = dict()
    lst = []
    for i in xrange(len(string)):
        if string[i] == "(":
            lst.append(i)
        elif string[i] == ")":
            if len(lst) > 0:
                dict_a[lst.pop()] = i
            else:
                return False
    if len(lst) > 0:
        return False
    else:
        return dict_a

# return a dictionary with open/close position pairs
# Test
# Test.assert_equals(bracket_pairs("len(list)"),{3:8},"Single pair of brackets")
# Test.assert_equals(bracket_pairs("def f(x"),False,"unmatched bracket")
# Test.assert_equals(bracket_pairs("(a(b)c()d)"),{0:9,2:4,6:7},"nested brackets")

# 其他解法
def bracket_pairs(string):
    print string
    dictionary = {}
    index = 0
    op = 0
    cl = 0
    for i, letter in enumerate(string):
        if letter == '(':
            dictionary[i] = ''
            op += 1
        elif letter == ')':
            cl += 1
            if dictionary:
                index += 1
                list_dict = dictionary.items()
                list_dict.reverse()
                if index <= len(list_dict):
                    for key, value in list_dict:
                        if value == '':
                            dictionary[key] = i
                            break

    for key, value in dictionary.items():
        if value == '':
            return False
    if op != cl:
        return False
    return dictionary