stu_age = [21, 25, 21, 23, 22, 20]
print(f"原有的年龄数据{stu_age}")
stu_age.append(31)
print(f"追加后的年龄数据{stu_age}")
stu_age.extend([29, 33, 30])
print(f"再次追加后的年龄数据{stu_age}")
a1 = stu_age.pop(0)
print(f"取出第一个元素{a1}后，年龄数据{stu_age}")
al = stu_age.pop(len(stu_age) - 1)
print(f"取出最后一个元素{al}后，年龄数据{stu_age}")
print(f"元素31在列表中的位置：{stu_age.index(31) + 1}")