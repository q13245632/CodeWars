# -*-coding:utf8 -*-
# 自己的解法
def reduce_by_rules(lst, rules):
    sum_lst = rules[0](lst[0],lst[1])
    print sum_lst
    for i in xrange(2,len(lst)):
        print i
        sum_lst = rules[(i-1) % len(rules)](sum_lst,lst[i])
    return sum_lst

# 测试集
# test.describe("Example Tests")
#
# def assert_equals(expected, input):
#     test.assert_equals(input, expected)
#
# test.it("Rules: [a + b, a - b]")
# rules = [lambda a, b: a + b, lambda a, b: a - b]
#
# assert_equals(5.0, reduce_by_rules([2.0, 2.0, 3.0, 4.0], rules))
#
# test.it("Rules: [a + b]")
# rules = [lambda a, b: a + b]
#
# assert_equals(6.0, reduce_by_rules([2.0, 2.0, 2.0], rules))
# assert_equals(8.0, reduce_by_rules([2.0, 2.0, 2.0, 2.0], rules))
# assert_equals(10.0, reduce_by_rules([2.0, 2.0, 2.0, 2.0, 2.0], rules))
# assert_equals(12.0, reduce_by_rules([2.0, 2.0, 2.0, 2.0, 2.0, 2.0], rules))
#
# test.it("Rules: [a + b, a - b, a * b]")
# rules = [lambda a, b: a + b, lambda a, b: a - b, lambda a, b: a * b]
#
# assert_equals(2.0, reduce_by_rules([2.0, 2.0, 2.0], rules))
# assert_equals(4.0, reduce_by_rules([2.0, 2.0, 2.0, 2.0], rules))
# assert_equals(6.0, reduce_by_rules([2.0, 2.0, 2.0, 2.0, 2.0], rules))
# assert_equals(4.0, reduce_by_rules([2.0, 2.0, 2.0, 2.0, 2.0, 2.0], rules))
#
# test.it("Rules: [min, max]")
# rules = [min, max]
#
# assert_equals(3.3, reduce_by_rules([1.3, 2.0, 3.3], rules))
# assert_equals(2.2, reduce_by_rules([4.1, 2.2, 2.1, 2.5], rules))
# assert_equals(8.0, reduce_by_rules([8.0, 8.1, 4.1, 12.0, 2.0], rules))
# assert_equals(2.4, reduce_by_rules([2.9, 2.8, 2.7, 2.6, 2.5, 2.4], rules))

# 其他解法
from functools import reduce
from itertools import cycle

def reduce_by_rules(lst, rules):
  rs = cycle(rules)
  return reduce(lambda x, y: next(rs)(x, y), lst)

