a = 'pageSize=50&pageIndex=1'
li = a.split('&')
# print(li)
di = {}
for i in li:
    i = i.split('=')
    di[i[0]] = i[-1]
# print(di)

string = 'helloworld'
assert 'world1' in string     # '输入的字符中不包含world'
print('输入的字符中包含world')    #执行下来会输出：输入的字符中包含world