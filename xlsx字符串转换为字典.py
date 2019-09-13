import xlrd

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