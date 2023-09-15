num = 100
# 全局变量
def test_a():
    print(f"test_a：{num}")
#
def test_b():
    # print(f"test_b：{num}") # 这句话写在前会报错
    num = 200 # 这个num是函数内的局部变量
    print(f"test_b：{num}") # 输出局部变量

# 关键字global的使用
def test_c():
    global num # 声名这个num变量是全局变量
    num = 500
    print(f"test_c：{num}")

test_a()
test_b()
print(num)
test_c()
print(num)
test_a()
test_b()