# 元组与列表的区别：元组定义完成后不可修改
# 定义元组字面量
# (元素, 元素, 元素, 元素)
t1 = (1, "hello", True)
print(type(t1))
print(t1)
# 定义元组变量
# 变量名称 = (元素, 元素, 元素, 元素)
# 定义空元组
# 变量名称 = ()
t2 = ()
print(type(t2))
print(t2)
# 变量名称 = tuple()
t3 = tuple()

# 定义只含有一个元素的元组
t4 = ("Hello", ) # t4 = ("Hello") 其实是定义了一个str

# 元组的嵌套
t5 = ((1, 2, 3), (4, 5, 6))
print(type(t5))
print(t5)
# 下标索引
n = t5[1][2]
print(n, type(n))

# 元组的操作：index(元素)、count(元素)、len(元组)
t6 = ("传智教育", "黑马程序员", "python")
index = t6.index("黑马程序员")
print(f" \"黑马程序员的\" 下标是：{index}")

t7 = ("传智教育", "黑马程序员", "黑马程序员", "黑马程序员", "黑马程序员", "python")
num = t7.count("黑马程序员")
print(f"元组 t7 中 \"黑马程序员\" 有 {num} 个")

t8 = ("传智教育", "黑马程序员", "黑马程序员", "黑马程序员", "黑马程序员", "python")
num_2 = len(t8)
print(f"元组 t8 中有 {num_2} 个元素")

# 元组的遍历：while
ind = 0
while ind < len(t8):
    print(f"t8元组的元素有：{t8[ind]}")
    ind += 1

# 元组的遍历：for
for ele in t8:
    print(f"t8_2元组的元素有：{ele}")

# 如果元组中的一个元素是list，那么这个list元素是可以修改的！
t9 = (0, 1, [2, 3, 4])
print(t9)
t9[2].append(5)
print(t9)
t9[2].clear()
print(t9)