# -*- coding:utf-8 -*-
# author: yushan
# date: 2017-03-21

from collections import Counter
def scramble(s1,s2):
    count1 = Counter(s1)
    count2 = Counter(s2)
    for i,k in count2.items():
        if i not in count1.iterkeys():
            return False
        elif count1[i] < k:
            return False
    return True

from collections import Counter
def scramble(s1,s2):
    # Counter basically creates a dictionary of counts and letters
    # Using set subtraction, we know that if anything is left over,
    # something exists in s2 that doesn't exist in s1
    return len(Counter(s2)- Counter(s1)) == 0

def scramble(s1, s2):
    return not any(s1.count(char) < s2.count(char) for char in set(s2))