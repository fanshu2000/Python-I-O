# 在D:\log文件夹中的.log文件中找到所有的内容含error字符串，并重新输入到newerror.log文件中
import glob

def  glob_test():
    # 以列表的形式返回所有匹配的文件路径，*.log代表匹配以.log结尾的所有文件
    li = glob.glob('D:\\log\\*.log')
    # 打开一个文件，创建一个file对象，然后可以调用其方法
    f = open('D:\\newerror.log','a')
    for i in li:
        # 循环打开每个文件，创建file对象，然后可以调用其方法
        file = open(i)
        # 以列表形式返回各行内容，每行内容为列表的一个元素
        content_li = file.readlines()
        # 遍历列表元素，即原文件的每行内容
        for j in content_li:
            # 判断‘error’是否在每个元素中
            if 'error' in j:
                # 将这行内容写进新文件中
                f.write(j)
                print('写入成功')
        file.close()
    f.close()
# glob_test()

# 复制图片
def copy_pi():
    # 打开一个文件，创建一个file对象，然后可以调用其方法
    f = open('D:\\1.jpg','rb')
    img = f.read()   # 返回的是二进制文件
    print(img)
    f.close()
    # 打开一个文件，若文件不存在则创建一个空文件
    k = open('D:\\4.jpg','wb')
    # 在k对象内写入img的内容
    k.write(img)
    k.close()
    print('完成')
# copy_pi()

#混合模式
def Mixed_mode():
    # 'a+'会自动将光标移到文件最后
    f = open(r'D:\test1.txt','a+')
    # 在前面加\n表示换行添加
    f.write('\nzhou,123,5000')
    # 刷新，将前面添加的内容立即添加至内存，避免异常，若有f.close(),刷新可以省略
    f.flush()
    # 强制将光标移动至文件最前面，不然后面无法读取内容，因为此时光标在最后面
    f.seek(0)
    # 将文件中的内容全部以字符串方式显示
    print(f.read())
# Mixed_mode()


# 文件with方式打开文件
def with_open():
    with open(r'D:\test1.txt','a+') as f:
        f.write('\nqiang,123,1000')
        f.flush()
        f.seek(0)
        print(f.read())
# with_open()

# 读取csv文件
import csv
f = open(r'D:\12.csv')
#
csv_reader = csv.reader(f)
print(csv_reader)
for i in csv_reader:
    print(i)
