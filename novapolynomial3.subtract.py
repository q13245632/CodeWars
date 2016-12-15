# -*-coding:utf8-*-
# 自己的解法
# return the subtraction of the two polynomials p1 and p2.
def poly_subtract(p1, p2):
    res = []
    longest_p = max(len(p1), len(p2))
    for i in range(longest_p):
        res.append((p1[i] if i < len(p1) else 0) - (p2[i] if i < len(p2) else 0))
    return res


