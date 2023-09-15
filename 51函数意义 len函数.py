s = """dfqfkpasokas"""
# 统计字符串的长度 len函数
n = len(s)
print(n)

str1 = "itheima"
str2 = "itcast"
str3 = "python"

# count = 0
# for i in str1:
#     count += 1
# print(f"字符串 \"{str1}\" 的长度是：{count}")

def my_len(date):
    count = 0
    for i in date:
        count += 1
    print(f"字符串 \"{date}\" 的长度是：{count}")

my_len(str2)
my_len(str3)