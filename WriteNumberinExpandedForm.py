# -*-coding:utf8 -*-
# 自己的解法
def expanded_form(num):
    n = len(str(num))
    string = str(num)
    lst = []
    for i in xrange(n): # python3.4.3版本需将xrange改为range
        if string[i] != "0":
            lst.append(str(int(string[i])* (10**(n-1-i))))
    return " + ".join(lst)
# 测试集
# test.assert_equals(expanded_form(12), '10 + 2');
# test.assert_equals(expanded_form(42), '40 + 2');
# test.assert_equals(expanded_form(70304), '70000 + 300 + 4');

# 一句话编程
def expanded_form(num):
    return " + ".join([str(int(d) * 10**p) for p, d in enumerate(str(num)[::-1]) if d != "0"][::-1])