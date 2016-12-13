# -*-coding:utf8-*-
# 自己的解法
def calculate_time(battery,charger):
    fast_hour = float(battery * 0.85) / charger
    decrease_hour = float(battery * 0.10) / (charger * 0.50)
    trickle_hour = float(battery * 0.05) / (charger * 0.20)
    return round(fast_hour + decrease_hour + trickle_hour,2)
    #your code here

# Test.describe("Basic Tests")
# Test.assert_equals(calculate_time(1000,500),2.6)
# Test.assert_equals(calculate_time(1500,500),3.9)
# Test.assert_equals(calculate_time(2000,1000),2.6)
# Test.assert_equals(calculate_time(5000,1000),6.5)
# Test.assert_equals(calculate_time(1000,5000),0.26)

# 简化解法
def calculate_time(battery,charger):
    return round(1.30*battery/charger, 2)
