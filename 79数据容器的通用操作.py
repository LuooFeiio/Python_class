# len(容器)、max(容器)、min(容器)
my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)
my_str = "abcdefg"
my_set = {1, 2, 3, 4, 5}
my_dict = {"key1": 1, "key2": 2, "key3": 3, "key4": 4, "key5": 5}

print(f"列表有元素：{len(my_list)}")
print(f"元组有元素：{len(my_tuple)}")
print(f"字符串有元素：{len(my_str)}")
print(f"集合有元素：{len(my_set)}")
print(f"字典有元素：{len(my_dict)}")

print(f"列表最大的元素是：{max(my_list)}")
print(f"元组最大的元素是：{max(my_tuple)}")
print(f"字符串最大的元素是：{max(my_str)}") # g
print(f"集合有最大的元素是：{max(my_set)}")
print(f"字典有最大的元素是：{max(my_dict)}") # key5

# 容器的通用转换：list(容器)-将给定容器转换为列表、str(容器)-将给定容器转换为字符串、tuple(容器)-将给定容器转换为元组、set(容器)-将给定容器转换为集合
print(f"列表转列表的结果是：  {list(my_list)}")
print(f"元组转列表的结果是：  {list(my_tuple)}")
print(f"字符串转列表的结果是： {list(my_str)}")
print(f"集合转列表的结果是：  {list(my_set)}")
print(f"字典转列表的结果是：  {list(my_dict)}")
# tuple(容器)-将给定容器转换为元组
print(f"列表转元组的结果是：  {tuple(my_list)}")
print(f"元组转元组的结果是：  {tuple(my_tuple)}")
print(f"字符串转元组的结果是： {tuple(my_str)}")
print(f"集合转元组的结果是：  {tuple(my_set)}")
print(f"字典转元组的结果是：  {tuple(my_dict)}")
# str(容器)-将给定容器转换为字符串
print(f"列表转字符串的结果是：  {str(my_list)}")
print(f"元组转字符串的结果是：  {str(my_tuple)}")
print(f"字符串转字符串的结果是： {str(my_str)}")
print(f"集合转字符串的结果是：  {str(my_set)}")
print(f"字典转字符串的结果是：  {str(my_dict)}")
# set(容器)-将给定容器转换为集合
print(f"列表转集合的结果是：  {set(my_list)}")
print(f"元组转集合的结果是：  {set(my_tuple)}")
print(f"字符串转集合的结果是： {set(my_str)}")
print(f"集合转集合的结果是：  {set(my_set)}")
print(f"字典转集合的结果是：  {set(my_dict)}")

# 容器的通用排序：sorted(容器, [reverse = True])，生成一个列表
print(f"列表对象的排序结果是：  {sorted(my_list)}")
print(f"元组对象的排序结果是：  {sorted(my_tuple)}")
print(f"字符串对象的排序结果是： {sorted(my_str)}")
print(f"集合对象的排序结果是：  {sorted(my_set)}")
print(f"字典对象的排序结果是：  {sorted(my_dict)}") # 转为list

print(f"列表对象的反向排序结果是：  {sorted(my_list, reverse = True)}")
print(f"元组对象的反向排序结果是：  {sorted(my_tuple, reverse = True)}")
print(f"字符串对象的反向排序结果是： {sorted(my_str, reverse = True)}")
print(f"集合对象的反向排序结果是：  {sorted(my_set, reverse = True)}")
print(f"字典对象的反向排序结果是：  {sorted(my_dict, reverse = True)}") # 转为list