# -*-coding:utf8-*-
# 自己的解法
def calc(x):
    lst = [str(ord(a)) for a in x]
    str_old = "".join(lst)
    str_replace = str_old.replace("7","1")
    old = sum(map(int,str_old))
    new = sum(map(int,str_replace))
    return old - new

# test.describe("Example Tests")
# test.assert_equals(calc('abcdef'), 6)
# test.assert_equals(calc('ifkhchlhfd'), 6)
# test.assert_equals(calc('aaaaaddddr'), 30)
# test.assert_equals(calc('jfmgklf8hglbe'), 6)
# test.assert_equals(calc('jaam'), 12)

# 简化
def calc(x):
    total1 = ''.join(str(ord(y)) for y in x)
    total2 = total1.replace('7','1')
    return sum(int(y) for y in total1) - sum(int(z) for z in total2)
