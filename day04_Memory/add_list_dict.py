# coding=gbk
# print('----')
a = 'hello'
b = 222
def edd01():
    print('%s %s' % (a, b))
def add02(aint,bint):
    print(aint)
    print(bint)
    sub = aint + bint
    return sub
def cdd03(aint,bint):
    print(aint)
    print(bint)
    sub = aint + bint
def list_demo():
    alist = [5,'qingqing','3',9,]
    print(alist)
alist = [5,'qingqing','3',9,]
def list_update(alist):
    alist[3] = 10
    print(alist[3])
    print(alist)

adict = {"name":"admin","pwd":"123456"}

if __name__ == '__main__':
    print('----字符串拼接')
    edd01()
    print('----两个数字相加有return 01')
    print(add02(4,5)) # 第1种add02
    print('----两个数字相加有return 02')
    add_1 = add02(3, 5)# 第2种add02
    print(add_1)
    print('----两个数字相加没有return')
    cdd1 = cdd03(4, 5)  # 没有return，返回null
    print(cdd1) # 没有return，返回空
    print('----访问列表')
    list_demo() # 访问列表
    print(alist[-1])
    print('----更新列表')
    list_update(alist)
    print('----删除列表')
    print(alist.pop(0))
    print(alist)
    print('----访问字典')
    print(adict)
    print('----访问字典的key值')
    print(adict['name'])
    print('----删除字典的key值')
    adict.pop('name')
    print(adict)


