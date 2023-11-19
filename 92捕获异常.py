# 对BUG进行提醒，程序继续运行
# try:
#     可能发生错误的代码
# except:
#     如果出现异常执行的代码
try:
    f = open('C:/Users/Administrator/Desktop/LawFee/linus.txt', 'r')
except:
    print('出现异常了，因为文件不存在，将open模式改为w模式去新建并打开一个文件')
    f = open('C:/Users/Administrator/Desktop/LawFee/linus.txt', 'w')

# 捕获指定的异常
try:
    print(name)
except NameError as e: # 指定捕获NameError异常
    print('name变量名称未定义错误')
    print(e)

# 捕获多种类型的异常，可以把要捕获的异常类型的名字，放到except后，并使用元组的方式进行书写
try:
    print(1/0)
except (NameError, ZeroDivisionError) as e:
    print('There is an error!!!')
    print(e)

# 捕获所有类型的异常
try:
    1 / 0
except Exception as e: # Exception应该是个关键字，可以代表所有的异常类型
    print('出现了异常')
    print(e)

# try:
#     1 op
# except:
#     print('出现了异常')

# 异常的else，表示的是如果没有异常要执行的代码
try:
    print(1)
except Exception as e:
    print(e)
else: # else是可选的
    print('这是else，是没有异常的时候执行的代码')

# 异常的finally，表示无论是否有异常都要执行的代码，例如关闭文件
try:
    f = open('C:/Users/Administrator/Desktop/LawFee/linu.txt', 'r')
except Exception as e:
    print(e)
    print('出现异常了，因为文件不存在，将open模式改为w模式去新建并打开一个文件')
    f = open('C:/Users/Administrator/Desktop/LawFee/linu.txt', 'w')
else:
    print('未出现异常，Good!')
finally:
    f.close()