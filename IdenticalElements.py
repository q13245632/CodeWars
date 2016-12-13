# -*-coding:utf8-*-
# 自己的解法
def duplicate_elements(m, n):
    result = False
    if m and n:
        for i in m:
            if n.count(i) > 0:
                result = True
                break
        return result
    else:
        return False

print duplicate_elements([0,7,8,4], [4,6,7,8,9])

# Test.describe("Basic tests")
# Test.it("should handle positive duplicates")
# Test.assert_equals(duplicate_elements([1, 2, 3, 4, 5], [1, 6, 7, 8, 9]), True)
# Test.assert_equals(duplicate_elements([9, 8, 7], [8, 1, 3]), True)

def duplicate_elements(m, n):
    return bool(set(m).intersection(n))
