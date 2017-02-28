# -*-coding:utf8 -*-
# author: yushan
# date: 2017-02-28


# 自己的解法
import string
import random
def password_gen():
    n = random.randint(6,20)
    if n > 20:
        print n,"++++"
    upper = list(string.uppercase)
    lower = list(string.lowercase)
    digit = list(string.digits)
    lst = []
    lst.extend(upper)
    lst.extend(lower)
    lst.extend(digit)
    pwd = []
    upper_char = upper[random.randint(0,25)]
    lower_char = lower[random.randint(0,25)]
    digit_char = digit[random.randint(0,9)]
    upper_pos = random.randint(0,n - 1)
    lower_pos = random.randint(0,n - 1)
    digit_pos = random.randint(0,n - 1)
    while upper_pos == lower_pos or upper_pos == digit_pos or digit_pos == lower_pos:
        upper_pos = random.randint(0,n - 1)
        lower_pos = random.randint(0,n - 1)
        digit_pos = random.randint(0,n - 1)
    for i in xrange(n):
        if i == upper_pos:
            pwd.append(upper_char)
            continue
        if i == lower_pos:
            pwd.append(lower_char)
            continue
        if i == digit_pos:
            pwd.append(digit_char)
            continue
        pwd.append(lst[random.randint(0,61)])
    return "".join(pwd)


from math import ceil
from random import randint, sample, shuffle
from string import ascii_lowercase as l, ascii_uppercase as u, digits as d

def password_gen(min_length=6, max_length=20, alphabet=(l, u, d)):
    _min, _max = ceil(min_length / len(alphabet)), ceil(max_length / len(alphabet))
    cards = [randint(_min, _max) for i in range(len(alphabet))]
    password = sum(map(sample, alphabet, cards), [])
    shuffle(password)
    return ''.join(password)[randint(0, _min * len(alphabet) - min_length): max_length]


import random

letters = list("abcdefghijklmnopqrstuvwxyz")
numbers = list("1234567890")

def password_gen():
    pwd_len = random.randint(6,20)
    pwd = [random.choice(letters).upper() for _ in range(random.randint(1, pwd_len - 2))]
    pwd += [random.choice(letters) for _ in range(random.randint(1, pwd_len - len(pwd) - 1))]
    pwd += [random.choice(numbers) for _ in range(pwd_len - len(pwd))]
    random.shuffle(pwd)
    return "".join(pwd)


for _ in xrange(1000):
    a = password_gen()
    if len(a) > 20:
        print a
# test.describe("This is not a real test, just a sample output of your code")
#
# print("Generated password   | Valid?")
# print("---------------------|-------")
# for _ in range(40):
#     pwd = password_gen()
#     lower = any(c.islower() for c in pwd)
#     upper = any(c.isupper() for c in pwd)
#     number = any(c.isdigit() for c in pwd)
#
#     print("%-20s | %s!" %
#         ( pwd, ["INVALID", "OK"][ 6 <= len(pwd) <= 20 and lower and upper and number]) )
#
# test.expect(True)
