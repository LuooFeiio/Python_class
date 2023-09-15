age = 105.1
n = "大大"
tall = 165.9
say = "名字是：%s，今年有%d岁，身高有%f米。" % (n, age, tall)
print(f"名字是：{n}，今年有{age}岁，身高有{tall}米。")
# 快速格式化不做精度控制，不限数据类型 f"内容{占位变量}"
message = f"名字是：{n}，今年有{age}岁，身高有{tall}米。"
print(message)