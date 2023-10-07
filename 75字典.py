# 字典的定义 my_dict = {key: value, key: value, key: value}
# 空字典：
# my_dict = {}
# 或 my_dict = dict()
# key不可重复！
my_dict = {"Law": 88, "Jack": 100, "Tom": 77}
print(my_dict, type(my_dict))

my_dict2 = {}
my_dict3 = dict()

my_dict4 = {"Law": 88, "Law": 100, "Tom": 77}
print(my_dict4, type(my_dict4))

# 通过key值取得对应的value
print(my_dict["Law"])

# 字典的嵌套：字典的key和value可以是任意的数据类型（key不可以是字典）
d1 = {
    "law":  {"math": 60, "arts": 90, "physics": 85},
    "jack": {"math": 60, "arts": 90, "physics": 85},
    "tom":  {"math": 60, "arts": 90, "physics": 85}
}
print(d1)
print(d1["law"])
print(d1["law"]["math"])