# -*-coding:utf8-*-
# 自己的解法
# return the sum of the two polynomials p1 and p2.
def poly_add(p1, p2):
    if p1 and not p2: return p1
    if not p1 and p2: return p2
    if not p1 and not p2: return p1
    if len(p1)<len(p2):
        for i in xrange(len(p2) - len(p1)):
            p1.append(0)
    else:
        for i in xrange(len(p1) - len(p2)):
            p2.append(0)
    return [p1[i] + p2[i] for i in xrange(len(p1))]

# Test.describe("Add two polynomials")
#
# Test.it("Should return the sum of polynomials")
# Test.assert_equals(poly_add([1], [1]),  [2], "Two polynomial of order zero fail.")
# Test.assert_equals(poly_add([1,2], [1]),  [2,2], "Mixed length polynomials fail.")
# Test.assert_equals(poly_add([1,2,3,4], [4,3,2,1]), [5,5,5,5])
#
# Test.it("Should handle empty list")
# Test.assert_equals(poly_add([],[]), [])
# Test.assert_equals(poly_add([1,2,3,4,5,6], []), [1,2,3,4,5,6])
# Test.assert_equals(poly_add([], [1,2,3,4,5,6]), [1,2,3,4,5,6])

# 思路不同
from itertools import izip_longest
def poly_add(p1, p2):
    return [a+b for a, b in izip_longest(p1, p2, fillvalue=0)]

# 简化程序
def poly_add(p1, p2):
    # store the result here
    res = []
    longest_p = max(len(p1), len(p2))
    for i in range(longest_p):
        # add the two numbers together unless there is no number there, then just add 0 (don't change)
        res.append((p1[i] if i < len(p1) else 0) + (p2[i] if i < len(p2) else 0))
    return res