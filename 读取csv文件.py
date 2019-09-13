# 读取csv文件
import csv
'''
# 打开文件
with open('D:/ts1.csv') as f:
    # 创建cvs文件读取器
    reader = csv.reader(f)
    # 读取第一行,这行是表头数据
    header_row = next(reader)
    print(header_row)
    # 读取第二行
    first_row = next(reader)
    print(first_row)
'''
'''
# 打开文件
f = open(r'D:\ts1.csv')
# 创建cvs文件读取器
cvs_reader = csv.reader(f)
print(cvs_reader)   # cvs_reader为一个对象
# 循环读取每行内容
for i in cvs_reader:
    print(i)
'''
'''
# 打开文件
f = open(r'D:\ts1.csv')
# 创建cvs文件读取器对象
cvs_reader = csv.reader(f)
# 用一个列表接收所有内容
rows=[row for row in  cvs_reader]
# rows为二维列表，通过索引或遍历取每行的内容
print(rows[0])
print(rows[1])
'''
'''
#获取文件某列数据
import csv
with open(r'D:\ts1.csv') as f:
    reader = csv.reader(f)
    # 读取第二列内容
    column=[row[1] for row in  reader]
    print(column)
    # 读取第三列内容，但由于指针已不在开头
    column1 = [row[2] for row in reader]
    print(column1)
'''
'''
#向csv文件中写入数据
import csv
# 打开文件，如果不加newline=''，会出现空行
f = open("D:\\ts2.csv",'a',newline='')
# 准备两行数据
row=['2019/5/5','28','28']
row1=['2019/5/6','29','29']
# 创建cvs文件写入对象，dialect为指定写入文件的方式
write=csv.writer(f,dialect='excel')
# 调用writerow方法写入数据
# write.writerow(row)
# write.writerow(row1)
#写入多行用writerows
write.writerows([row,row1])
print("写入完毕！")
'''

'''
# 复制CSV格式文件
import csv
# 打开文件,读取数据
f = open('D:/ts1.csv')
# 创建csv读取器
reader = csv.reader(f)
# 读取所有内容
rows = [row for row in reader]
# 打开文件
t = open('D:/ts2.csv','w',newline='')
# 创建csv写入对象
write = csv.writer(t)
# 遍历原文件所有内容，row为每行数据
for row in rows:
    write.writerow(row)
'''
import pandas


# csv文件读取
# 打开文件
# f = open('D:/ts1.csv')
# data = pandas.read_csv(f)
# 读取打印所有数据
# print(data)
# 读取打印正文的前两行
# print(data.head(2))
# 返回全部列名
# print(data.columns)
# 返回csv文件形状
# print(data.shape)
# 打印第1到3行
# print(data.loc[1:3])
#打印行中特定列
# print(data.loc[2:4, ['日期', '最高气温']])
# describe()方法数据统计
# print(data.describe())
# 读取某一行所有数据
# print(data.loc[0,])
#读取第一行、第二行、第四行的所有数据
# print(data.loc[[0,1,3],:])
#读取所有行和列数据
# print(data.loc[:,:])
# 读取某一列的所有行数据
# print(data.loc[:,'最低气温'])
# 读取某几列的某几行
# print(data.loc[[0,1,3],['日期','最高气温']])

# CSV数据的导入导出(复制CSV文件)
# f = open('D:/ts1.csv')
# data = pandas.read_csv(f)
# 将数据写入新文件中
# data.to_csv('D:/ts2.csv')
