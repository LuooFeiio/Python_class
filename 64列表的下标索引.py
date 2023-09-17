name_list = ['tom', 'jack', 'lily']
print(name_list[0])
print(name_list[1])
print(name_list[2])
# print(name_list[3]) 运行这句话会报错
# list还可以反向索引
print(name_list[-3])
print(name_list[-2])
print(name_list[-1])

#嵌套列表的下标索引
num_list = [[1, 2], [3, 4]]
print(num_list[-1])
print(num_list[-1][0])
print(num_list[1][0])
print(num_list[-1][-2])

num_list_2 = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
print(num_list_2)
print(num_list_2[0])
print(num_list_2[0][-3])