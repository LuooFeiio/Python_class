print("欢迎来到动物园")

name = input("输入你的名字：")

if int(input("你的身高：")) > 120:
    
    print("你的身高大于120cm，不能免费！")
    print("但是，如果你的VIP级别大于3，也可免费。")

    if int(input("输入VIP等级：")) > 3:
        print("你是贵宾，免费玩！")
    else:
        print("你也不是贵宾，掏钱吧<_>")

else:
    print("小朋友免费哦>_<")