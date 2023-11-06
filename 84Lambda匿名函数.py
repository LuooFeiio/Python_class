# 无名称的匿名函数，只可临时使用一次
# lambda 传入参数: 函数体(一行代码)
# lambda是关键字
# 传入参数表示匿名函数的形式参数，如：x, y 表示接收2个形式参数
# 函数体，只能写一行，无法写多行代码
def test_func(compute, a, b):
    result = compute(a, b) # compute是函数
    print(f"compute参数的类型是：{type(compute)}")
    print(f"计算结果：{result}")

test_func(lambda x, y: x + y, 3, 4)