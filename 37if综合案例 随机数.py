# 1~10随机数生成
import random
num = random.randint(1, 10)

a = int(input("第一次猜："))

if a == num:
    print("第一次就猜对了！")
else:
    if a < num:
        print("第一次没猜对，往大猜，再来一次")
    else:
        print("第一次没猜对，往小猜，再来一次")

    b = int(input("第二次猜："))

    if b == num:
        print("第二次猜对！")
    else:
        if b < num:
            print("第二次还没猜对，往大猜，最后再来一次")
        else:
            print("第二次还没猜对，往小猜，最后再来一次")

        c = int(input("最后一次猜："))
        if c == num:
            print("最后猜对了")
        else:
            print("最后还是没猜对")
            print(f"其实结果是：{num}")
            print("其实结果是 %d %d %d 啊" % (num, num, num))

print("Game over!!!")