# -*-coding:utf8 -*-
# author: yushan
# date: 2017-03-02

# 自己的解法
def remove_url_anchor(url):
    lst = url.split("#")
    return lst[0]
