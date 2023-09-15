"""
输出不换行
"""
print("Hello ", end = '')
print("World")

# 制表符 \t
print("Hello\tWorld")
print("Lawe\tFee")

i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(f"{j} * {i} = {i * j}\t", end = '')
        j += 1
    print() # 换行
    i += 1