# -*-coding:utf8-*-
# 自己的解法
# 限制条件：不能使用这些关键字
# def
# if
# eval or exec
# return
# import
is_leap = lambda x : x % 400 == 0 or x % 100 != 0 and x % 4 == 0


# 思路不同
y100 = set([x for x in range(1600, 10000, 100)])
y400 = [x for x in range(1600, 10000, 400)]
y4 = set([y for y in range(1584, 10000, 4)])

leapy = list(y4 - y100) + y400

is_leap = lambda n : n in leapy