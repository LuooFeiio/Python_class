# 通过占位符完成字符串拼接
name = "我是•"
w = "风"
t = "%s自由的%s" % (name, w)
print(t)
t = "%s自由的" % name
print(t)

class_num = 57
avg_salary = 187
message = "班级有%s人，每人要交%s¥" % (class_num, avg_salary)
print(message)

age = 105.1
n = "大大"
tall = 165.9
say = "名字是：%s，今年有%d岁，身高有%f米。" % (n, age, tall)
print(say)