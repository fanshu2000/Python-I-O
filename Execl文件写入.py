import hashlib,xlrd

from xlutils.copy import copy

# 密码加密
def md5(pwd):
    # 实例化md5对象
    md5_pwd = hashlib.md5()
    md5_pwd.update(pwd.encode())
    # 返回加密后的密文
    return md5_pwd.hexdigest()

# 登录功能
def login(user,pwd):
    pwd1 = md5(pwd)
    # 读取xls中的内容，用户名和密码
    book = xlrd.open_workbook('D:/tst1.xls')
    # print(book.sheet_names())
    sheet = book.sheets()[2]
    for i in range(sheet.nrows):
        li = sheet.row_values(i)
        print(li)
        # 判断输入的用户名和密码是否正确
        if user == li[0] and pwd1 == li[1]:
            print("登录成功")
            break
    else:
        print("用户名或密码有误")

# 注册功能
def register(user,pwd):

    # 打开文件，获得该文件对象
    book = xlrd.open_workbook('D:/tst1.xls')
    # 得到第三张工作表的对象
    sheet = book.sheets()[2]
    # 获得当前sheet的行数
    nrows = sheet.nrows
    # 调用xlutils.copy模块的copy()方法复制book给new_book
    new_book = copy(book)
    # 通过get_sheet()获取的sheet有write()方法
    new_sheet = new_book.get_sheet(2)
    # 写入数据new_sheet.write(行, 列, value),从第nrows开始，避免先前的内容被修改
    new_sheet.write(nrows, 0, user)
    new_sheet.write(nrows, 1, pwd)
    # 保存文件
    new_book.save('D:/tst1.xls')

    print("注册成功")

while True:
    num = input("请选择：")
    if num == '1':
        print("欢迎来到注册界面")
        user = input("请输入用户名：")
        pwd = input("请输入密码：")
        # 给输入进来的密码加密
        pwd = md5(pwd)
        register(user, pwd)
    elif num == '2':
        print("欢迎来到登录界面")
        user = input("请输入用户名：")
        pwd = input("请输入密码：")
        login(user,pwd)
    else:
        quit()
