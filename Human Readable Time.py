# -*- coding:utf-8 -*-
# author: yushan
# date: 2017-03-14


def make_readable(seconds):
    mins,secs = divmod(seconds,60)
    hours,mins = divmod(mins,60)
    return "{:0>2}:{:0>2}:{:0>2}".format(hours,mins,secs)

def make_readable(s):
    return '{:02}:{:02}:{:02}'.format(s / 3600, s / 60 % 60, s % 60)
# Test.assert_equals(make_readable(0), "00:00:00")
# Test.assert_equals(make_readable(5), "00:00:05")
# Test.assert_equals(make_readable(60), "00:01:00")
# Test.assert_equals(make_readable(86399), "23:59:59")
# Test.assert_equals(make_readable(359999), "99:59:59")