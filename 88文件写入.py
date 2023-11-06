# f = open("C:/Users/MsiLeFee/Desktop/LawFee/Test.txt", 'w')
# f.write('hello world') # 文件写入
# f.flush() # 内容刷新
# 直接调用write，写的内容只是保留在内存中；调用了flush后，内容会真正写入文件
f = open("C:/Users/MsiLeFee/Desktop/LawFee/Test_2.txt", 'w')
f.write('hello world')

f.flush()

# import time
# time.sleep(5000000)

f.close() # close其实内置了flush的功能