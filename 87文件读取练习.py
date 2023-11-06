f = open("C:/Users/MsiLeFee/Desktop/LawFee/Test.txt", 'r', encoding = 'UTF-8')
# content = f.read()
# count = content.count('itheima')
# print(f"itheima在文件中出现了：{count}次")

count = 0

for line in f:
    line = line.strip()

    words = line.split(' ')
    print(words)

    for word in words:
        if word == 'itheima':
            count += 1

print(f"itheima在文件中出现了：{count}次")
f.close()