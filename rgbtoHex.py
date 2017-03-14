# -*- coding:utf-8 -*-
# author: yushan
# date: 2017-03-14

def rgb(r, g, b):
    r = 255 if r > 255 else r
    g = 255 if g > 255 else g
    b = 255 if b > 255 else b
    r = 0 if r < 0 else r
    g = 0 if g < 0 else g
    b = 0 if b < 0 else b
    r_hex = str(hex(r)).split("x")[-1].upper()
    g_hex = str(hex(g)).split("x")[-1].upper()
    b_hex = str(hex(b)).split("x")[-1].upper()
    return "{:0>2}{:0>2}{:0>2}".format(r_hex,g_hex,b_hex)


def rgb(r, g, b):
    round = lambda x: min(255, max(x, 0))
    return ("{:02X}" * 3).format(round(r), round(g), round(b))
# test.assert_equals(rgb(0,0,0),"000000", "testing zero values")
# test.assert_equals(rgb(1,2,3),"010203", "testing near zero values")
# test.assert_equals(rgb(255,255,255), "FFFFFF", "testing max values")
# test.assert_equals(rgb(254,253,252), "FEFDFC", "testing near max values")
# test.assert_equals(rgb(-20,275,125), "00FF7D", "testing out of range values")
