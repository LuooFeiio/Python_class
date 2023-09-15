age = 105.1
n = "大大"
tall = 165.9
say = "名字是：%s，今年有%5d岁，身高有%5.1f米。" % (n, age, tall)
print(say)

say = "名字是：%s，今年有%5d岁，身高有%.0f米。" % (n, age, tall)
print(say)