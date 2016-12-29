# -*-coding:utf8 -*-
# 自己的解法
import re
def bracket_buster(string):
    if not isinstance(string,str):
        return "Take a seat on the bench."
    result = []
    lst = re.findall('\[.*?\]',str(string))
    for i in xrange(len(lst)):
        result.append(lst[i][1:(len(lst[i])-1)])
    return result
print bracket_buster("Don't [pass to Ramone]")
# 测试集
# test.assert_equals(bracket_buster("Don't [pass to Ramone]"), ["pass to Ramone"])
# test.assert_equals(bracket_buster(1337), "Take a seat on the bench.")
# test.assert_equals(bracket_buster("[I'm] glad y'all [set it]] off"), ["I'm", 'set it'])

# 其他解法
import re

REGEX = re.compile(r'\[(.*?)\]')


def bracket_buster(strng):
    try:
        return REGEX.findall(strng)
    except TypeError:
        return 'Take a seat on the bench.'