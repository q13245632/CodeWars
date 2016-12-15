# -*-coding:utf8-*-
# 自己的解法
def averages(arr):
    if not arr or len(arr) <= 1:
        return []
    lst = []
    for i in xrange(len(arr) - 1):
        lst.append(float(arr[i] + arr[i+1])/2)
    return lst

# test.describe("Example Tests")
# tests = (
#     ([2, 2, 2, 2], [2, 2, 2, 2, 2]),
#     ([0, 0, 0, 0], [2, -2, 2, -2, 2]),
#     ([2, 4, 3, -4.5], [1, 3, 5, 1, -10]),
#     ([], [])
# )
#
# for exp, inp in tests:
#     test.assert_equals(averages(inp), exp)

# 简化程序
def averages(arr):
    if arr is None or len(arr) < 2:
        return []

    return [(arr[i] + arr[i + 1]) / 2 for i in range(len(arr) - 1)]