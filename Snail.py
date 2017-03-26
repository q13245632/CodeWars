# -*- coding:utf-8 -*-
# author: yushan
# date: 2017-03-23

def snail(array):
    results = []
    while len(array) > 0:
        # go right
        results += array[0]
        del array[0]

        if len(array) > 0:
            # go down
            for i in array:
                results += [i[-1]]
                del i[-1]

            # go left
            if array[-1]:
                results += array[-1][::-1]
                del array[-1]

            # go top
            for i in reversed(array):
                results += [i[0]]
                del i[0]

    return results


def snail(array):
    a = []
    while array:
        a.extend(list(array.pop(0)))
        array = zip(*array)
        array.reverse()
    return a

def snail(array):
    ret = []
    if array and array[0]:
        size = len(array)
        for n in xrange((size + 1) // 2):
            for x in xrange(n, size - n):
                ret.append(array[n][x])
            for y in xrange(1 + n, size - n):
                ret.append(array[y][-1 - n])
            for x in xrange(2 + n, size - n + 1):
                ret.append(array[-1 - n][-x])
            for y in xrange(2 + n, size - n):
                ret.append(array[-y][n])
    return ret

# array = [[1,2,3],
#          [4,5,6],
#          [7,8,9]]
# expected = [1,2,3,6,9,8,7,4,5]
# test.assert_equals(snail(array), expected)
#
#
# array = [[1,2,3],
#          [8,9,4],
#          [7,6,5]]
# expected = [1,2,3,4,5,6,7,8,9]
# test.assert_equals(snail(array), expected)