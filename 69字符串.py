name = "lawFeefe and luoofeiio"
print(name[0])
print(name[-1])
print(name[6])

# 统计字符串的长度：len(str)
print(len(name))

# 字符串的元素不可修改
# name[0] = "L" # 报错

# 查找特定字符串的起始下标索引：字符串.index(字符串)
index = name.index("and")
print(index) # 结果7

# 字符串的替换：字符串.replace(字符串1, 字符串2)，功能：将字符串内的：字符串1 替换为：字符串2
# 注意：不是修改字符串，而是得到一个新的字符串！
name_2 = name.replace("lawFee", "lockheed")
print(name_2, name)

# 字符串的分割：字符串.split(分隔符字符串)
# 功能：按照 分隔符字符串，将字符串划分为多个字符串，并存入列表对象中
# 注意：字符串本身不变，而是得到了一个列表对象
list_1 = name.split(" ")
print(list_1, type(list_1))

# 字符串的规整操作（去除前后空格）:字符串.strip()
# 字符串的规整操作（去除前后指定的字符串）:字符串.strip(字符串)
str1 = "            i am luoo       "
str2 = str1.strip()
print(str1, "\n", str2)
print(str2)
str3 = "12fhifbcsbfcw131221"
# str3 = "12fhifbcsbfcw12"
str4 = str3.strip("12")
print(str4)

# 统计字符串中某字符串出现的次数：字符串.count(某字符串)
n = name.count("fe")
print(n)