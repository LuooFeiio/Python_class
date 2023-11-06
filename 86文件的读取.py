# f = open(name, mode, encoding) 打开一个已存在的文件，或创建一个新文件
# mode访问模式：只读、写入、追加等 r w a
# r: 只读模式，这是默认模式
# w: 若文件存在则打开，并从头开始编辑，原有内容会被删除；若文件不存在，则会创建文件
# a: 追加，若文件已存在，则新的内容会追加到已有内容之后；若文件不存在，则创建新文件写入
# encoding编码格式，推荐使用UTF-8
# E: f = open('python.txt', 'r', encoding = "UTF-8")
# encoding参数的顺序不是第三位，所以不能用位置参数，用关键字参数指定
# f是返回的一个对象

f = open("C:/Users/MsiLeFee/Desktop/LawFee/Test.txt", 'r', encoding = 'UTF-8')

print(type(f))
# print(f)

# read()方法：文件对象.read(num)，表示从文件读取num字节长度的数据，如果没有传入num，则读取文件中的所有数据
part = f.read(3)
print(part)

print(f.read())
print(f.read()) # 指针到文件尾了？

# readlines()方法：按照行的方式将整个文件的内容进行一次性读取，返回一个列表，文件中每一行的数据为一个元素
f = open("C:/Users/MsiLeFee/Desktop/LawFee/Test.txt")
content = f.readlines()
print(content)
print(type(content))

# readline()方法：一次读取一行内容
f = open("C:/Users/MsiLeFee/Desktop/LawFee/Test.txt")
content = f.readline() # 会读取到换行符'\n'
print(content)
print(type(content))
content = f.readline()
print(content)

# for循环逐行读取文件内容
for line in open("C:/Users/MsiLeFee/Desktop/LawFee/Test.txt", 'r'):
    print(line)

f = open("C:/Users/MsiLeFee/Desktop/LawFee/Test.txt", 'r')
for line in f:
    print(line)

# 关闭文件：close()方法可以关闭文件
f.close()
# 若文件未被关闭，而且程序没有停止运行，那么这个文件将一直被Python程序占用
# import time
# time.sleep(5000000) # 此时无法删除文件了

# with open语法
# 通过在with open的语句块中对文件进行操作，在操作完成后自动关闭文件
with open("C:/Users/MsiLeFee/Desktop/LawFee/Test.txt", 'r', encoding = 'UTF-8') as f:
    for line in f:
        print(f"每一行数据是：{line}")