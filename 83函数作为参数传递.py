def test_func(compute, a, b):
    result = compute(a, b) # compute是函数
    print(f"compute参数的类型是：{type(compute)}")
    print(f"计算结果：{result}")

def compue(x, y):
    return x + y

c = int(input("输入一个参数："))
d = int(input("输入另一个参数："))

test_func(compue, c, d)