# 以[]作为标识，列表内的每一个元素之间用, 逗号隔开
# 定义字面量
# [元素1, 元素2, 元素3, 元素3, ...]
#
# 定义变量
# 变量名称 = [元素1, 元素2, 元素3, 元素3, ...]
#
# 定义空列表
# 变量名称 = []
# 变量名称 = list()
#
# 列表内的每一个数据称之为元素
# 列表一次可以存储多个数据，且可以为不同的数据类型，支持嵌套
# 数据是有序存储的（有下标）
# 允许重复的元素
# 可以修改：增加或删除元素

my_list = ["itcast", 'itheima', 666, True]
print(my_list)
print(type(my_list))

# 列表的嵌套
my_list_2 = ['LawFree', my_list, 785]
print(my_list_2)
print(type(my_list_2))
li = [[1, 2], ['fwfw', False]]
print(li)
print(type(li))

# 空列表
my_list_3 = list()
print(my_list_3)

my_list_4 = []
print(my_list_4)