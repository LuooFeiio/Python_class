def user_info(name, age, gender):
    print(f"您的名字是：{name}，年龄是：{age}，性别是：{gender}")

# 位置传参
user_info("law", 18, "男")

# 关键字传参，可以不按照固定的顺序，"键 = 值"
user_info(gender = "Female", name = "Lee", age = 20)
# 关键字传参，可以和位置传参混用，位置参数必需在前面，且匹配参数顺序，但关键字参数之间不存在先后顺序
user_info("Ming", gender = "Male", age = 20)

# 缺省参数，也叫默认参数
# 定义函数时可以为参数提供默认值
# 所有位置参数必须在默认参数之前，包括函数定义和调用
def user_info_2(name = "Lockdown", age = "45", gender = "男"):
    print(f"您的名字是：{name}，年龄是：{age}，性别是：{gender}")

user_info_2("Jojo", 30)
user_info_2("Rose", 18, "女")
user_info_2(gender = "Female", name = "Lee", age = 20)
user_info_2()

# 不定长参数 - 位置传递
def user_info_3(*args):
    print(args)
    print(type(args))
# 传进的所有参数都会被args变量收集，它会根据传进参数的位置合并为一个元组（tuple），args是元组类型，这就是位置传递
user_info_3()
user_info_3(1, False, "Low")

# 不定长参数 - 关键字传递
def user_info_4(**kwargs):
    print(kwargs)
    print(type(kwargs))
# 参数是”键 = 值“形式的情况下，所有的”键 = 值“都会被kwargs接受，同时会跟据”键 = 值“组成字典
user_info_4(gender = "Female", name = "Lee", age = 20, Log = False)