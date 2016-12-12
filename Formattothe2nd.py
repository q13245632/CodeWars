# -*-coding:utf8-*-
# 自己的解法
def print_nums(*args):
    max_len = 0
    if len(args) <= 0:
        return ''
    else:
        for i in args:
            if max_len < len(str(i)):
                max_len = len(str(i))
        string = '{:0>' + str(max_len) + '}'
        return "\n".join([string.format(str(i)) for i in args])

# test.describe('Basic Tests')
# test.assert_equals(print_nums(), '')
# test.assert_equals(print_nums(2), '2')
# test.assert_equals(print_nums(1, 12, 34), '01\n12\n34')
# test.assert_equals(print_nums(1009, 2), '1009\n0002')

# 其他解法
def print_nums(*args):
  width = max((len(str(num)) for num in args), default=0)
  return '\n'.join('{:0{}d}'.format(num, width) for num in args)