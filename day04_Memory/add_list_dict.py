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
    print('----�ַ���ƴ��')
    edd01()
    print('----�������������return 01')
    print(add02(4,5)) # ��1��add02
    print('----�������������return 02')
    add_1 = add02(3, 5)# ��2��add02
    print(add_1)
    print('----�����������û��return')
    cdd1 = cdd03(4, 5)  # û��return������null
    print(cdd1) # û��return�����ؿ�
    print('----�����б�')
    list_demo() # �����б�
    print(alist[-1])
    print('----�����б�')
    list_update(alist)
    print('----ɾ���б�')
    print(alist.pop(0))
    print(alist)
    print('----�����ֵ�')
    print(adict)
    print('----�����ֵ��keyֵ')
    print(adict['name'])
    print('----ɾ���ֵ��keyֵ')
    adict.pop('name')
    print(adict)


