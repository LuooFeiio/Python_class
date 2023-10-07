# 集合set不支持元素重复（自动去重），且无序（不支持下标索引）
# 定义集合字面量 {}
# {元素, 元素, 元素, 元素, 元素}
# 定义集合变量
# 变量名称 = {元素, 元素, 元素, 元素, 元素}
# 定义空集合
# 变量名称 = set()

my_set = {"LawFee", "白马", "教育", "LawFee", "白马", "教育", "LawFee", "白马", "教育"}
my_set_empty = set()
print(f"my_set的内容是：{my_set}，类型是：{type(my_set)}")
print(f"my_set_empty的内容是：{my_set_empty}，类型是：{type(my_set_empty)}")

# 添加新元素：集合.add(元素)，集合本身被修改
my_set.add("Python")
my_set.add("白马") # 自动去重
print(my_set)

# 移除元素：集合.remove(元素)，集合本身被修改
my_set.remove("Python")
print(my_set)
# my_set.remove("Python") # 报错

# 随机取出一个元素：集合.pop()，结果是得到一个元素，同时集合被修改
# 集合为空后，再次 集合.pop() 会报错
ele = my_set.pop()
print(ele, my_set)
ele = my_set.pop()
print(ele, my_set)
ele = my_set.pop()
print(ele, my_set)

# 清空集合，集合.clear()
my_set = {"LawFee", "白马", "教育", "LawFee", "白马", "教育", "LawFee", "白马", "教育"}
print(my_set)
my_set.clear()
print(my_set)

# 取出两个集合的差集，语法：集合1.difference(集合2)
# 功能：集合1有而集合2没有的
# 得到一个新的集合，集合1和集合2不变
set1 = {1, 2, 3}
set2 = {1, 5, 6}
set3 = set1.difference(set2)
print(set1, set2, set3)

# 消除2个集合的差集：集合1.difference_update(集合2)
# 功能：在集合1内，删除和集合2相同的元素
# 集合1被修改，集合2不变
set1 = {1, 2, 3}
set2 = {1, 5, 6}
set1.difference_update(set2)
print(set1, set2)

# 集合合并：集合1.union(集合2)
# 得到一个新集合，集合1与集合2不变
set1 = {1, 2, 3}
set2 = {1, 5, 6}
set3 = set1.union(set2)
print(set1, set2, set3)

# 统计集合元素数量：len(集合)
set4 = {1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5}
print(len(set4)) # 5

# 集合的遍历，用for循环
for ele in set4:
    print(f"set4的元素有：{ele}")