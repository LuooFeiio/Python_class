# range(num)
"""
语法1：
获取从 0 到 num-1的数字序列
如 range(5) 取得的数据是：[0,1,2,3,4]
"""
for i in range(10):
    print(i,"\t", end = '')
print()

# 语法2：
# range(num1, num2)
# 获取从 num1 到 num2 - 1的数字序列
# 如 range(5, 10) 取得的数据是：[5,6,7,8,9]

for i in range(10, 5, -1):
    print(i,"\t", end = '')
print()

for i in range(5, 10):
    print(i,"\t", end = '')
print()

# 语法3：
# range(num1, num2, step)
# 获取从 num1 到 num2 的数字序列（不包含 num2），数字之间的步长，以step为准（默认是 1 ）
# 如 range(5, 10，2) 取得的数据是：[5,7,9]

for i in range(1, 10, 2):
    print(i,"\t", end = '')
print()

num = int(input("请输入一个整数："))
count = 0
for x in range(1, num + 1):
    if x % 2 == 0:
        print(x, "\t", end = '')
        count += 1
print()
print(f"1 ~ {num}间有{count}个偶数")