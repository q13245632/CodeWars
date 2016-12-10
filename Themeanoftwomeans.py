# -*-coding:utf8-*-
# 自己的解法
def get_mean(arr,x,y):
    if x <= 1 or y <= 1:
        return -1
    if x > len(arr) or y > len(arr):
        return -1
    x_mean = float(sum(arr[:x]))/x
    y_mean = float(sum(arr[-y:]))/y
    print x_mean," ",y_mean
    return (x_mean + y_mean) / 2

print get_mean([1,3,2],2,2)
# 测试集
# Test.describe("Basic tests")
# Test.assert_equals(get_mean([1,3,2,4],2,3),2.5)
# Test.assert_equals(get_mean([1,3,2],2,2),2.25)
# Test.assert_equals(get_mean([1,3,2,4],1,2),-1)
# Test.assert_equals(get_mean([1,3,2,4],2,8),-1)
# Test.assert_equals(get_mean([1,-1,2,-1],2,3),0)

# 简化程序
def get_mean(arr,x,y):
  if x not in range(2,len(arr)+1) or y not in range(2, len(arr)+1): return -1
  return (sum(arr[:x])/x + sum(arr[-y:])/y) /2