def reverseAndMirror(s1, s2):
    str1 = s1.swapcase()
    str2 = s2.swapcase()
    str2[::-1]
    return str2[::-1] + "@@@" + str1[::-1] + str1