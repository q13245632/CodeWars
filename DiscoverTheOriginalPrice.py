# -*-coding:utf8-*-
# 自己的解法
def discover_original_price(discounted_price, sale_percentage):
    n = discounted_price / (1 - float(sale_percentage) / 100)
    if n - int(n) < 0.01:
        return int(n)
    else:
        return "{:.2f}".format(n)

# 使用round函数
def discover_original_price(price, discount):
    return 0 if discount == 100 else round(price / (1.0 - discount / 100.0), 2)