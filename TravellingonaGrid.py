# -*-coding:utf8 -*-
# 自己的解法
# (1 1)(3 3)
def factorial(x):
	fac = 1
	for i in xrange(1,x+1):
		fac = fac * i
	return fac
def travel_chessboard(s):
	arr = list(s)
	x1 = int(arr[1])
	y1 = int(arr[3])
	x2 = int(arr[6])
	y1 = int(arr[8])
	m = x2 - x1
	n = y2 - y1
	w = 1
	if n == 0 or m == 0:
		w = 1
	else:
		k = m + n
		w = factorial(k)/(factorial(m)*factorial(n))
	return w

# 简化思路
import re
from math import factorial as fac

def travel_chessboard(s):
    x1, y1, x2, y2 = map(int, re.findall(r'\d+', s))
    dx, dy = (x2 - x1), (y2 - y1)
    return fac(dx + dy) / (fac(dx) * fac(dy))