
# 常见属性
def attribute():
    # 以默认方式打开文件
    f = open('D:/456.txt','r+')
    # 访问文件的编码方式
    print(f.encoding)  # cp936
    # 访问文件的访问模式
    print(f.mode)  # r
    # 访问文件是否已经关闭
    print(f.closed)  # False
    # 访问文件对象打开的文件名
    print(f.name)  # open_test.py
    # 关闭文件
    f.close()
# attribute()

'''
# 只读模式
# 文件打开
f = open('D:/456.txt', 'rb')
print(f.read())
# # 指针移到到末尾
# f.seek(0, 2)
# 写入
# f.write("admin")  #  会报错io.UnsupportedOperation: not writable
f.close()
'''

'''
# 只写模式
f = open('D:/456.txt', 'w')
f.read()    # 会报错io.UnsupportedOperation: not readable
# 指针移到到末尾
f.seek(0, 2)
# 写入
f.write("admin")  # 结果依然是覆盖原有内容，指针在此无用
f.close()
'''
'''
# 只写追加模式
f = open('D:/456.txt', 'a')
# 将指针移到到开头，
f.seek(0)
# 写入，即使指针在开头，也会从末尾追加
f.write("admin")
# # 打印读取的内容
# print(f.read())
f.close()
'''

'''
# w+读写模式
f = open('D:/456.txt', 'w+')
# 自动清空原先内容，即使没有写入操作，也会清空
# 指针移到到开头
f.seek(0)
# 打印读取的内容
print(f.read())
# 写入
f.write("admin")
f.close()
'''

'''
# r+读写模式
f = open('D:/456.txt', 'r+')
# 指针移到到末尾
# f.seek(0,2)
# 打印读取的内容
print(f.read())
# 读取一次后，指针到末尾，写入就从末尾写
f.write("admin1")
# 指针移到到开头
f.seek(0)
f.close()
'''

'''
# 二进制只写模式
# 文件打开
f = open('D:/456.txt', 'rb')
print(f.read())
# 指针移到到末尾
f.seek(0, 2)
# 写入,必须写入二进制文件，不然报错
f.write("admin")
f.close()
'''
'''
# 二进制模式混合模式
# 打开图片
f = open('D:/1.jpg','rb')
# 文件读取，二进制内容
img = f.read()
# 文件打开,若无则创建新文件
# 最后选择相应的打开方式即可
g = open('D:/2','wb')
# 将二进制内容写入到文件中
g.write(img)
f.close()
g.close()
'''
