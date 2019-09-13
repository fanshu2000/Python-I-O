import csv

# 打开文件
import xlrd

f = open(r'D:\接口参数.csv')
# 创建cvs文件读取器
reader = csv.reader(f)
# 读取第一行,这行是表头数据
header_row = next(reader)
li = []
di = {}    # 空字典接收每行的键值对
# 遍历除去第一行后的所有行
for j in reader:
    di = {}    # 空字典接收每行的键值对
    # 遍历第一行
    for i in header_row:
        # 第一行的每个元素作为键，后面行对应索引位置的元素作为值
        # di.setdefault(i,j[header_row.index(i)])
        di[i] = j[header_row.index(i)]
    li.append(di)
print(li)
# 文件写入必须是字符串，所有此处强转
li = str(li)
with open(r"D:\80808080.txt",'w') as f:
    f.write(li)


# 将xlsx中单元格内字符串转换为字典
book = xlrd.open_workbook(r"D:\就业管理.xlsx")
sheet = book.sheets()[0]
for i in range(5,sheet.nrows):
    # 取每行的值
    li = sheet.row_values(i)
    di = {}   # 空列表接收元素
    a = li[4].split(',')
    for i in a:
        j = i.split("=")
        di.setdefault(j[0],j[1])
    di = str(di)  # 文件读写只能写入str,不能是dict
    with open(r"D:\789098.txt","a") as f:
        f.write(di)
