# -*-coding:utf8-*-
# 自己的解法
def get_mixed_num(fraction):
    a , b = map(int,fraction.split('/'))
    n = a / b
    m = a % b
    return str(n) + " " + str(m) + "/" + str(b)

print get_mixed_num('13/5')

# test.describe("Basic Tests")
# test.it("Basic Tests")
# test.assert_equals(get_mixed_num('18/11'), '1 7/11')
# test.assert_equals(get_mixed_num('13/5'), '2 3/5')
# test.assert_equals(get_mixed_num('75/10'), '7, 5/10')

# 简化解法
def get_mixed_num(f):
    f = [int(x) for x in f.split('/')]
    w, r = divmod(f[0], f[1])
    return '{} {}/{}'.format(w, r, f[1])
