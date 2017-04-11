# -*- coding:utf-8 -*-
# author: yushan
# date: 2017-04-08


def reduce(money,coins,num):
    if money == 0: return num + 1
    if money < 0 or len(coins) <= 0: return num
    return reduce(money - coins[0],coins,num) + reduce(money, coins[1::], num)


def count_change(money, coins):
    if money <= 0 or len(coins) <= 0:return 0
    return reduce(money,coins,0)


# test.assert_equals(3, count_change(4, [1,2]))
# test.assert_equals(4, count_change(10, [5,2,3]))
# test.assert_equals(0, count_change(11, [5,7]))



def count_change(money, coins):
    if money<0:
        return 0
    if money == 0:
        return 1
    if money>0 and not coins:
        return 0
    return count_change(money-coins[-1],coins) + count_change(money,coins[:-1])


def count_change(money, coins):
    dp = [1]+[0]*money
    for coin in coins:
        for x in xrange(coin,money+1):
            dp[x] += dp[x-coin]
    return dp[money]