# -*- coding:utf-8 -*-
# author: yushan
# date: 2017-03-17


import string
from codecs import encode as _dont_use_this_

def rot13(message):
    lst = []
    for i in message:
        if ord('a') <= ord(i) <=ord('z'):
            k = ord(i) + 13 if ord(i) + 13 <= ord('z') else ord(i) - 13
            lst.append(chr(k))
        elif ord('A') <= ord(i) <= ord('Z'):
            k = ord(i) + 13 if ord(i) + 13 <= ord('Z') else ord(i) - 13
            lst.append(chr(k))
        else:
            lst.append(i)
    return "".join(lst)



import string
from codecs import encode as _dont_use_this_
from string import maketrans, lowercase, uppercase

def rot13(message):
    lower = maketrans(lowercase, lowercase[13:] + lowercase[:13])
    upper = maketrans(uppercase, uppercase[13:] + uppercase[:13])
    return message.translate(lower).translate(upper)
