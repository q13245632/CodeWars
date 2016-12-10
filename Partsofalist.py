# 自己的解法
def partlist(arr):
    lst = []
    for i in xrange(len(arr) - 1):
        a = " ".join(arr[0:i+1])
        b = " ".join(arr[i+1:])
        tup = (a,b)
        lst.append(tup)
    return lst

# 看到其他的一行解法
def partlist(ar):
    return [(" ".join(ar[:i]), " ".join(ar[i:])) for i in xrange(1, len(ar))]