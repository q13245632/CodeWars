# -*- coding:utf-8 -*-
# author: yushan
# date: 2017-03-29


bin='01'
oct='01234567'
dec='0123456789'
hex='0123456789abcdef'
allow='abcdefghijklmnopqrstuvwxyz'
allup='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alpha='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphanum='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def convert(input, source, target):
    k = 0
    l = len(input)
    for i in xrange(len(input)):
        k += source.index(input[i]) * len(source) ** (len(input) - i - 1)
    n,k = divmod(k,len(target))
    string = str(target[k])
    while n != 0:
        n,k = divmod(n,len(target))
        string += str(target[k])
    return string[::-1]


# test.describe('example tests')
# bin = Alphabet.BINARY; oct = Alphabet.OCTAL; dec = Alphabet.DECIMAL; hex = Alphabet.HEXA_DECIMAL;
# allow = Alphabet.ALPHA_LOWER; alup = Alphabet.ALPHA_UPPER; alpha = Alphabet.ALPHA; alnum = Alphabet.ALPHA_NUMERIC;
#
# test.it('should convert between numeral systems')
# test.assert_equals(convert("15", dec, bin), '1111', '"15" dec -> bin');
# test.assert_equals(convert("15", dec, oct), '17', '"15" dec -> oct');
# test.assert_equals(convert("1010", bin, dec), '10', '"1010" bin -> dec');
# test.assert_equals(convert("1010", bin, hex), 'a', '"1010" bin -> hex');
#
# test.it('should convert between other bases')
# test.assert_equals(convert("0", dec, alpha), 'a', '"0" dec -> alpha');
# test.assert_equals(convert("27", dec, allow), 'bb', '"27" dec -> alpha_lower');
# test.assert_equals(convert("hello", allow, hex), '320048', '"hello" alpha_lower -> hex')
# test.assert_equals(convert("SAME", alup, alup), 'SAME', '"SAME" alpha_upper -> alpha_upper');

def convert(input, source, target):
    base_in = len(source)
    base_out = len(target)
    acc = 0
    out = ''
    for d in input:
        acc *= base_in
        acc += source.index(d)
    while acc != 0:
        d = target[acc%base_out]
        acc = acc/base_out
        out = d+out
    return out if out else target[0]


from math import log

def convert(value, source, target):
    value = sum(source.find(c) * (len(source) ** i) for i, c in enumerate(reversed(value)))
    return ''.join(target[(value / (len(target) ** i)) % len(target)] for i in xrange(0 if not value else int(log(value, len(target))),-1,-1))