# -*-coding:utf8-*-
# 自己的解法
def func_or(a,b):
    if a:
        return True
    else:
        if b:
            return True
    return False

def func_xor(a,b):
    if a:
        if not b:
            return True
    else:
        if b:
            return True
    return False

# Test.describe("Basic tests")
# Test.assert_equals(func_or(True, True), True)
# Test.assert_equals(func_or(True, False), True)
# Test.assert_equals(func_or(False, False), False)
# Test.assert_equals(func_or(0, 11), True)
# Test.assert_equals(func_or(None, []), False)
# Test.assert_equals(func_xor(True, True), False)
# Test.assert_equals(func_xor(True, False), True)
# Test.assert_equals(func_xor(False, False), False)
# Test.assert_equals(func_xor(0, 11), True)
# Test.assert_equals(func_xor(None, []), False)

# 思路不同
def func_or(a,b):
    return not (not a and not b)

def func_xor(a,b):
    return (not a) != (not b)