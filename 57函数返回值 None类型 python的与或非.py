def say_hello():
    """

    :return:
    """
    print("Hello...")
    return None

# 主动使用return None 与不写return语句的效果一样

result = say_hello()
print(result)
print(type(result))

# 用于if判断中，None等同于False
# 函数主动返回None可与if判断联动使用

# python的与或非 and or not
# https://blog.csdn.net/swansonge/article/details/109166865