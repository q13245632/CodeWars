# -*-coding:utf8 -*-
# author: yushan
# date: 2017-02-26


# 自己的解法
def the_biggest_search_keys(*args):
    if len(args) == 0:
        return "''"
    lst = []
    maxlen = 0
    for i in args:
        if len(i) == maxlen:
            lst.append("'"+i+"'")
        elif len(i) > maxlen:
            maxlen = len(i)
            lst = []
            lst.append("'"+i+"'")
    lst.sort()
    return ", ".join(lst)


def the_biggest_search_keys(*args):
    by_len = {}
    fmt = "'{}'".format
    for a in args:
        by_len.setdefault(len(a), []).append(a)
    try:
        return ', '.join(fmt(b) for b in sorted(by_len[max(by_len)]))
    except ValueError:
        return "''"


def the_biggest_search_keys(*args):
    maxLen = max(map(len, args), default=None)
    return "''" if not args else ", ".join(sorted(filter(lambda s: len(s)-2 == maxLen, map(lambda s: "'{}'".format(s), args))))

def the_biggest_search_keys(*keys):
    m = max(map(len, keys)) if keys else "''"
    return str( sorted( filter(lambda x: len(x) == m, keys) ) )[1:-1] if keys else m

def the_biggest_search_keys(*keys):
    return ', '.join(sorted("'" + key + "'" for key in keys if len(key) == max(map(len, keys)))) if len(keys) else "''"


print the_biggest_search_keys("key1", "key222222", "key333")
print the_biggest_search_keys("coding", "tryruby", "sorting")
print the_biggest_search_keys()
# Test.describe("Basic tests")
# Test.assert_equals(the_biggest_search_keys("key1", "key22", "key333"), "'key333'")
# Test.assert_equals(the_biggest_search_keys("coding", "sorting", "tryruby"), "'sorting', 'tryruby'")
# Test.assert_equals(the_biggest_search_keys("small keyword", "how to coding?", "very nice kata", "a lot of keys", "I like Ruby!!!"), "'I like Ruby!!!', 'how to coding?', 'very nice kata'")
# Test.assert_equals(the_biggest_search_keys("pippi"), "'pippi'")
# Test.assert_equals(the_biggest_search_keys(), "''")