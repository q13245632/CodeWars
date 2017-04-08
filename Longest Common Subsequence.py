# -*- coding:utf-8 -*-
# author: yushan
# date: 2017-04-08

def lcs(s1, s2):
    n1 = len(s1)
    n2 = len(s2)
    if n1 == 0 or n2 == 0:
        return ''
    dp = [[0 for j in xrange(n2 + 1)] for i in xrange(n1 + 1)]
    for i in xrange(n1):
        for j in xrange(n2):
            if s1[i] == s2[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
    m = dp[n1][n2]
    mj = n1
    mk = n2
    res = []
    for i in xrange(m, 0, -1):
        found = False
        j = i
        while j <= mj:
            k = i
            while k <= mk:
                if s1[j - 1] == s2[k - 1] and dp[j][k] == i:
                    found = True
                    mj = j - 1
                    mk = k - 1
                    res.append(s1[j - 1])
                    break
                else:
                    k += 1
            if found:
                break
            j += 1
    return ''.join(res[::-1])


test.assert_equals(lcs("a", "b"), "")
test.assert_equals(lcs("abcdef", "abc"), "abc")


def lcs(x, y):
    if len(x) == 0 or len(y) == 0:
        return ''
    if x[-1] == y[-1]:
        return lcs(x[:-1], y[:-1]) + x[-1]
    else:
        lcs1 = lcs(x,y[:-1])
        lcs2 = lcs(x[:-1],y)
        if len(lcs1) > len(lcs2):
            return lcs1
        else:
            return lcs2



from itertools import combinations

def subsequences(s):
    """Returns set of all subsequences in s."""
    return set(''.join(c) for i in range(len(s) + 1) for c in combinations(s, i))

def lcs(x, y):
    """Returns longest matching subsequence of two strings."""
    return max(subsequences(x).intersection(subsequences(y)), key=len)



def lcs(x, y):
  res=[]
  i=0
  for item in y:
     if item in x[i:]:
        res+=[item]
        i=x.index(item)+1
  return "".join(res)