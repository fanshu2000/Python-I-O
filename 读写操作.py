'''
# read函数
# 打开文件
f = open("D:/456.txt")
# 读取5个字符
r1 = f.read(5)
print(r1)
# 读取这5个字符后，指针会移动后第六个字符开头
# 读取指针开始的所有内容
r2 = f.read()
print(r2)
f.close()
'''
'''
# reading函数
# 打开文件
f = open("D:/456.txt")
# 读取整行，不会打印\n，但有换行效果
r1 = f.readline()
print(r1)
# 读取指针开始后的5个字符
r2 = f.readline(5)
print(r2)
f.close()
'''

'''
# readline函数循环
# 打开文件
f = open("D:/456.txt")
# 读取整行，不会打印\n，但有换行效果
while True:
    # 每次读取一行
    r1 = f.readline()
    # 如果没有读到数据，跳出循环
    if not r1:
        break
    print(r1)
f.close()
'''
'''
# readlines函数
# 打开文件
f = open("D:/456.txt")
# 读取所有行，末尾带\n
r = f.readlines()
print(r)
f.close()
'''
'''
# write()方法
# 打开文件
f = open("D:/456.txt",'w')
# 写入内容
r = f.write('文件读写123')
# print(r)
# f.close()
'''
'''
#  writeline()方法
# 打开文件
f = open("D:/456.txt",'w')
# 写入内容
seq = "Process finished with exit code 0"
f.write( seq )

# f.close()
'''
'''
# 打开文件
f = open("D:/456.txt",'rb+')
# 指针偏移,从开头向后移动两个字符
# f.seek(2,0)
# 指针偏移,从末尾向后移动两个字符
f.seek(-2,2)
# 返回当前指针位置
# 写入内容
# r = f.write('文件读写')
# f.close()
'''

# 以二进制模式打开文件
f = open("D:/456.txt",'rb+')
print(f.read())
# 指针偏移,从末尾向前移动两个字节
f.seek(-2,2)
# 返回当前指针位置
print(f.tell())
# 读取指针后的内容，此时指针就会跑到末尾
print(f.read())
# 写入二进制内容
r = f.write(b'\xce\xc4')
f.close()
