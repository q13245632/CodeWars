# -*-coding:utf8-*-
# 自己的解法
def check_bit(string):
    isEven = False
    num = 0
    for x in xrange(len(string) - 1):
        if string[i] is '1':
            num += 1
    if num % 2 == 0: isEven = True
    return isEven

def parity_bit(binary):
    lst = binary.split(" ")
    for i in xrange(len(lst)):
        if check_bit(lst[i]):
            if lst[i][7] == '0':
                lst[i] = lst[i][:7]
            else:
                lst[i] = "error"
        else:
            if lst[i][7] == '1':
                lst[i] = lst[i][:7]
            else:
                lst[i] = "error"
    return ' '.join(lst)

# 简化程序
def parity_bit(binary):
    res = ''
    for b in binary.split(' '):
        if b[:-1].count('1') % 2 == int(b[-1]):
            res += b[:-1] + ' '
        else:
            res += 'error '
    return res[:-1]

# 使用函数
def parity_bit(binary):
    # your code here!
    def change(b):
        if b.count('1') % 2 == 0:
            return b[:-1]
        return 'error'

    res = map(change, binary.split())
    return " ".join(res)

# 一行代码
def parity_bit(binary):
    return ' '.join([w[:-1] if w[:-1].count('1') % 2 == int(w[-1]) else 'error' for w in binary.split()])