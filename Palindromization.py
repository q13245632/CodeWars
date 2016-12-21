# -*-coding:utf8 -*-
# 自己的解法
def palindromization(elements, n):
    if not elements or n < 2:
        return "Error!"
    else:
        string = elements * 10
        k = n // 2
        q = n % 2
        string_half = string[:k]
        string_return = ""
        if q != 0:
            string_a = string[k:k+q]
            string_return = string_half + string_a + string_half[::-1]
        else:
            string_return = string_half + string_half[::-1]
        return string_return
print palindromization("123",2)
print palindromization("123",3)
print palindromization("123",8)
print palindromization("123",7)
# Test.describe("Examples")
#
# # Use "it" to identify the conditions you are testing for
# Test.it("Description examples")
# # using assert_equals will report the invalid values to the user
# Test.assert_equals(palindromization("123",2), "11");
# Test.assert_equals(palindromization("123",3), "121");
# Test.assert_equals(palindromization("123",4), "1221");
# Test.assert_equals(palindromization("123",5), "12321");
# Test.assert_equals(palindromization("123",6), "123321");
# Test.assert_equals(palindromization("123",7), "1231321");
# Test.assert_equals(palindromization("123",8), "12311321");
# Test.assert_equals(palindromization("123",9), "123121321");
# Test.assert_equals(palindromization("123",10), "1231221321");
#
# Test.it("Description error")
#
# Test.assert_equals(palindromization("", 2), "Error!");
# Test.assert_equals(palindromization("123", 1), "Error!");
# 简化程序
def palindromization(el, n):
  if el == "" or n < 2: return "Error!"
  res = "".join([el[i % len(el)] for i in range(n // 2)])
  return res + ["", el[(len(res)) % len(el)]][n % 2] + res[::-1]
