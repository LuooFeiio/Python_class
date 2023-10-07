# 新增元素：字典[key] = value
# 修改元素：字典[key] = value
d1 = {
    "law":  {"math": 60, "arts": 90, "physics": 85},
    "jack": {"math": 60, "arts": 90, "physics": 85},
    "tom":  {"math": 60, "arts": 90, "physics": 85}
}

d1["rose"] = {"math": 50, "arts": 75, "physics": 60} # 新增
print(d1)
d1["jack"] = {"math": 30, "arts": 97, "physics": 50} # 更新
print(d1)

# 删除元素：字典.pop(key)
# 作用：获得指定key的value，同时修改了字典
score = d1.pop("tom")
print(f"删除的元素：{score}, 字典修改为：{d1}")

# 清空字典：字典.clear()
d1.clear()
# print(d1.clear())
print(d1)

# 获取全部的key：字典.keys()
d2 = {
    "law":  {"math": 60, "arts": 90, "physics": 85},
    "jack": {"math": 60, "arts": 90, "physics": 85},
    "tom":  {"math": 60, "arts": 90, "physics": 85}
}
keys = d2.keys()
print(keys, type(keys))
# 遍历字典
for key in keys:
    print(f"字典的键值{key} \t对应的value为：{d2[key]}")

# 遍历字典方式2：直接对字典for循环，每次循环都是直接得到key
print(f"字典的遍历：方式2")
for key in d2:
    print(f"字典的键值{key} \t对应的value为：{d2[key]}")

# 统计字典的元素数量：len(字典)
print(len(d2))
print(len(d2["jack"]))