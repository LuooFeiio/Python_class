# s1 = "学python，来黑马，月薪不到二百五"
# s2 = s1[::-1]
# print(s2)
# index = s1.index("，")
# print(index)
# s3 = s1.split("，")
# print(s3)
# s4 = s3[1]
# print(s4)
# s5 = s4.replace("来", "")
# print(s5)

ms1 = "五百二到不薪月，马黑来，nohtyp学"
ms2 = ms1[::-1][9:11] # 体会这种写法!
print(ms2)
ms3 = ms1[8:10][::-1]
print(ms3)
ms4 = ms1.split('，')[1].replace("来", "")[::-1]
print(ms4)