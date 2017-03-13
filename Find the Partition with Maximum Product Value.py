# -*- coding:utf-8 -*-
# author: yushan
# date: 2017-03-13

def find_part_max_prod(n):
    # your code here
    if n <= 4:return n
    k = n % 3
    m = n // 3
    lst = []
    if k == 0:
        return [[3] * m,3 ** m]
    elif k==1:
        return [[4] + [3] * (m-1),[3]*(m-1)+[2,2],3**(m-1) * 4]
    elif k == 2:
        return [[3] * m+[2],3**m * 2]




from itertools import groupby

def partition(n, k):
    result = [n / k for _ in xrange(k)]
    for i in xrange(n % k):
        result[i] += 1
    return result

def prod(arr):
    return reduce(lambda x, y: x * y, arr)


def find_part_max_prod(n):
    partitions = sorted((partition(n, i) for i in xrange(1, n + 1)), key=prod)
    data = [(k, list(group)) for k, group in groupby(partitions, key=prod)][-1]

    return data[1] + [data[0]]




def find_part_max_prod(n):
  if n == 1: return [[1], 1]
  q, r = divmod(n, 3)
  if r == 0: return [[3]*q, 3**q]
  if r == 1: return [[4] + [3]*(q - 1), [3]*(q - 1) + [2, 2], 3**(q - 1) * 2**2]
  return [[3]*q + [2], 3**q * 2]