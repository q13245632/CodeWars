# -*-coding:utf8-*-
# 自己的解法
from string import maketrans
def sort_twisted37(arr):
    tr = maketrans("37","73")
    sort_arr = sorted([int(str(x).translate(tr)) for x in arr])
    return [int(str(x).translate(tr)) for x in sort_arr]

# 其他思路
def sort_twisted37(arr):
    newarr = []; result = []

    def weird_sorter(elem):
        l = ''
        for i in str(elem):
            if(i == '3'): l = l + '7'
            else:
                if(i == '7'): l = l + '3'
                else: l += i
        return int(l);

    for i in arr: newarr.append(weird_sorter(i))
    newarr.sort()
    for j in newarr: result.append(weird_sorter(j))
    return result

# lambda函数
def sort_twisted37(arr):
  twisted = lambda n: int(''.join('3' if c=='7' else '7' if c == '3' else c for c in str(n)))
  return sorted(arr, key=twisted)

