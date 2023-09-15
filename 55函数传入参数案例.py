def check(Temperature):
    print("欢迎返校！", end = '')
    print("请出示证件，并配合测量体温！")
    # print("你的体温是：%.1f" % Temperature)
    if Temperature > 37.5:
        print("你的体温是：%.1f ℃，需要隔离！" % Temperature)
    else:
        print("你的体温是：%.1f ℃，体温正常请进>_<" % Temperature)

t = float(input("输入你的体温："))
check(t)