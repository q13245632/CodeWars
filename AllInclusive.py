# -*-coding:utf8-*-
# 自己的解法
def contain_all_rots(string, arr):
    if len(string) <= 0:
        return True
    lst = [string[i:] + string[0:i] for i in xrange(len(string))]
    return all(x in arr for x in lst)

# Test.describe("contain_all_rots")
# Test.it("Basic tests")
# testing(contain_all_rots("", []), True)
# testing(contain_all_rots("", ["bsjq", "qbsj"]), True)
# testing(contain_all_rots("bsjq", ["bsjq", "qbsj", "sjqb", "twZNsslC", "jqbs"]), True)
# testing(contain_all_rots("XjYABhR", ["TzYxlgfnhf", "yqVAuoLjMLy", "BhRXjYA", "YABhRXj", "hRXjYAB", "jYABhRX", "XjYABhR", "ABhRXjY"]), False)

# 思路
def contain_all_rots(strng, arr):
    length = len(strng)
    s2 = strng * 2
    return set(s2[a:a + length] for a in xrange(length)).issubset(arr)