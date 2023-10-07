# 列表/元组/字符串 均是序列，支持切片操作
# 切片：从一个序列中，取出一个子序列，即得到了一新的序列
# 语法：序列[起始下标:结束下标:步长]
# 起始下标 可以留空，视作从头开始
# 结束下标(不含) 可以留空，视作截取到结尾(含)
# 步长1表示：一个个取元素；步长N表示：每次跳过N-1个元素取；步长为空：默认1
# 步长为负数：反向取，注意：此时 起始下标&结束下标 也要反向标记

my_list = [0, 1, 2, 3, 4, 5, 6]
n_list = my_list[1:4:1]
# n_list = my_list[1:4] # 步长留空，视作1
print(my_list, '\n', n_list)

my_tuple = (0, 1, 2, 3, 4, 5, 6)
result = my_tuple[:] # 起始、结束都为空，步长也为空
print(result)

my_str = "01234567"
n_str = my_str[ : :2]
print(n_str)
r_str = my_str[ : :-1] # r_str = my_str[-1: :-1]
print(r_str)

my_list = [0, 1, 2, 3, 4, 5, 6]
print(my_list[3:1:-1])

my_tuple = (0, 1, 2, 3, 4, 5, 6)
print(my_tuple[::-2])