# -*-coding:utf8 -*-
# 自己的解法
def morse_converter(string):
    n = len(string) / 5
    num = 0
    for i in xrange(n):
        if string[i*5:(i+1)*5] == ".----":
            num += 1 * (10 ** (n-1-i))
        if string[i*5:(i+1)*5] == "..---":
            num += 2 * (10 ** (n - 1 - i))
        if string[i*5:(i+1)*5] == "...--":
            num += 3 * (10 ** (n-1-i))
        if string[i*5:(i+1)*5] == "....-":
            num += 4 * (10 ** (n - 1 - i))
        if string[i*5:(i+1)*5] == ".....":
            num += 5 * (10 ** (n-1-i))
        if string[i*5:(i+1)*5] == "-....":
            num += 6 * (10 ** (n - 1 - i))
        if string[i*5:(i+1)*5] == "--...":
            num += 7 * (10 ** (n-1-i))
        if string[i*5:(i+1)*5] == "---..":
            num += 8 * (10 ** (n - 1 - i))
        if string[i*5:(i+1)*5] == "----.":
            num += 9 * (10 ** (n-1-i))
        if string[i*5:(i+1)*5] == "-----":
            num += 0 * (10 ** (n - 1 - i))
    return num
# 测试集
# 1 .---- 2 ..--- 3 ...-- 4 ....- 5 ..... 6 -.... 7 --... 8 ---.. 9 ----. 0 -----
# Test.describe("Basic tests")
# Test.assert_equals(morse_converter(".----"), 1)
# Test.assert_equals(morse_converter("..----------..."), 207)
# Test.assert_equals(morse_converter("----.--.....---...--"), 9723)

# 其他解法
MORSE_TO_NUM = {
    ".----" : "1",
    "..---" : "2",
    "...--" : "3",
    "....-" : "4",
    "....." : "5",
    "-...." : "6",
    "--..." : "7",
    "---.." : "8",
    "----." : "9",
    "-----" : "0",
}

def morse_converter(s):
    return int("".join(MORSE_TO_NUM[s[i:i+5]] for i in xrange(0, len(s), 5)))