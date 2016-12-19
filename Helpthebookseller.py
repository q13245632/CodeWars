# -*-coding:utf8 -*-
# 自己的解法
def stock_list(listOfArt, listOfCat):
    lst = []
    set_sum = set()
    for a in listOfCat:
        sum_a = 0
        for b in listOfArt:
            if b[0] == a:
                m,n = b.split(" ")
                sum_a += int(n)
        if sum_a == 0:
            set_sum.add(a)
        string = "(" + a + " : " + str(sum_a) + ")"
        lst.append(string)
    if len(set_sum) == len(listOfCat):
        return ""
    return " - ".join(lst)


# b = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"]
# c = ["A", "B"]
# res = "(A : 200) - (B : 1140)"
# test.assert_equals(stock_list(b, c), res)

# 其他解法
from collections import Counter

def stock_list(listOfArt, listOfCat):
    if not listOfArt:
        return ''
    codePos = listOfArt[0].index(' ') + 1
    cnt = Counter()
    for s in listOfArt:
        cnt[s[0]] += int(s[codePos:])
    return ' - '.join('({} : {})'.format(cat, cnt[cat]) for cat in listOfCat)

from collections import Counter

def stock_list(listOfArt, listOfCat):
    return '' if not (listOfArt and listOfCat) else ' - '.join('({} : {})'.format(c, sum(int(book.split()[1]) for book in listOfArt if book[0] == c)) for c in listOfCat)