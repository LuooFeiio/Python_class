print("欢迎来到动物园")

# height = int(input("输入身高："))
# vip = int(input("输入你的VIP级别（1~5）："))
# day = int(input("请输入今天几号（1~30）："))

if int(input("输入身高：")) < 120:
    print("身高小于120CM，可以免费玩")
elif int(input("输入你的VIP级别（1~5）：")) > 3:
    print("你的VIP级别大于3，可以免费玩。")
elif int(input("请输入今天几号（1~30）：")) == 1:
    print("今天1号免费玩")
else:
    print("不好意思，所有条件都不满足，需购票。")

# 注释多行：选中多行按Ctrl+/

print("Have a good time")