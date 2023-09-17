# 1、查找某元素的下标，若找不到，报错ValueError
my_list = ["itheima", "itcast", "itheima", "python"]
print(my_list.index("itheima"))
# print(my_list.index("itheim"))

# 2、修改元素的值
my_list[0] = 1
print(my_list)
my_list[-3] = 3
print(my_list)

# 3、插入元素：列表.insert(下标, 元素)
my_list.insert(0, "Law")
print(my_list.insert(1, "Fee"))
print(my_list)

# 4、追加元素：列表.append(元素)，将元素追加到列表的尾部
my_list.append(5) # 追加单个元素
print(my_list)
my_list.append([6, "Luoo"])
print(my_list)
my_list[7].append("Feiio")
print(my_list)
my_list[7].insert(1, "I'm")
print(my_list)
# 5、追加多个元素：列表.extend(其他数据容器)，将其他数据容器的内容取出，一一追加到列表尾部
list_1 = [1, 2, 3]
list_1.extend([4, 5, 6])
print(list_1)
list_2 = [7, 8, 9]
list_1.extend(list_2)
print(list_1)
# list_1.extend(list_1)
# print(list_1)
list_1.append(list_2)
print(list_1)
print(list_1[9])

# 6、删除元素：del 列表[下标]
# 6、删除元素：列表.pop(下标)
del list_1[9]
print(f"list_1列表删除元素后{list_1}")
del list_1[0]
print(f"list_1列表删除元素后{list_1}")
element = list_1.pop(2)
print(element, list_1)

# 7、删除某元素在列表中的第一个匹配项：列表.remove(元素)
list_3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_3.remove(2)
print(list_3)
# list_3.remove(10) # 报错
# print(list_3)
list_3.remove(4)
print(list_3)

# 8、清空列表 列表.clear()
list_3.clear()
print(list_3)

# 9、统计某元素在列表内的数量：列表.count(元素)
list_4 = ["itheima", "itcast", "itheima", "python"]
print(list_4.count("itheima"))

# 10、统计列表共有多少个元素：len(列表)
print(len(list_4))