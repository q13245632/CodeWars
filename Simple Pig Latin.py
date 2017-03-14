# -*- coding:utf-8 -*-
# author: yushan
# date: 2017-03-14

def pig_it(text):
    lst = text.split(" ")
    res = []
    for i in lst:
        first = i[:1]
        later = i[1:]
        if i.isalpha():
            res.append(later + first + "ay")
        else:
            res.append(i)
    return " ".join(res)


def pig_it(text):

    return " ".join(x[1:] + x[0] + "ay" if x.isalnum() else x for x in text.split())
# Test.assert_equals(pig_it('Pig latin is cool'),'igPay atinlay siay oolcay')
# Test.assert_equals(pig_it('This is my string'),'hisTay siay ymay tringsay')