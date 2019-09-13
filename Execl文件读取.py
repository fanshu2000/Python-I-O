import xlrd

# 读取内容的三种类型
def read_xls():
    # 打开文件
    book = xlrd.open_workbook(r'D:\tst1.xls')
    print(book)
    sheet = book.sheets()[0]   #  sheet为一个对象，[0]代表输出第一页内容

    # 获取行数和列数
    nrows = sheet.nrows
    ncols = sheet.ncols
    print(nrows,ncols)   # 结果为：3 3

    # 获取整行和整列的值（列表）
    print(sheet.row_values(2))
    print(sheet.col_values(2))

    # 获取每个单元格内容
    for i in range(sheet.nrows):
        for j in range(sheet.ncols):
        #     print(sheet.cell(i,j).value,end=' ')
        # print('')   # 换行输出

            pass

    # 获取每一行的内容
    for i in range(sheet.nrows):
        li = sheet.row_values(i)
        # print(li)   # 输出内容为列表

    # 获取每一列的内容
    for i in range(sheet.ncols):
        li = sheet.col_values(i)
        print(li)    # 输出内容为列表

read_xls()

