# -*- coding:utf-8 -*-
# author: yushan
# date: 2017-03-21


def is_valid_IP(strng):
    if strng == "" or strng == None:return False
    lst = strng.split(".")
    if not len(lst) == 4:return False
    for i in lst:
        if i.isalpha():
            return False
        if int(i) > 255 or int(i) < 0:
            return False
        if not len(i) == len(str(int(i))):
            return False
    return True


# Test.assert_equals(is_valid_IP('12.255.56.1'),     True)
# Test.assert_equals(is_valid_IP(''),                False)
# Test.assert_equals(is_valid_IP('abc.def.ghi.jkl'), False)
# Test.assert_equals(is_valid_IP('123.456.789.0'),   False)
# Test.assert_equals(is_valid_IP('12.34.56'),        False)
# Test.assert_equals(is_valid_IP('12.34.56 .1'),     False)
# Test.assert_equals(is_valid_IP('12.34.56.-1'),     False)
# Test.assert_equals(is_valid_IP('123.045.067.089'), False)


def is_valid_IP(strng):
  lst = strng.split('.')
  passed = 0
  for sect in lst:
    if sect.isdigit():
      if sect[0] != '0':
        if 0 < int(sect) <= 255:
          passed += 1
  return passed == 4




import re
def is_valid_IP(strng):
    return bool(re.match(r'^((\d{1,2}|1\d{2}|2[0-4]\d|25[0-5])(\.(?!$)|$)){4}(?=$)',strng))