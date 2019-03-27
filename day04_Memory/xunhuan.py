# coding=gbk
def xunhuan_range():
    print('----从0开始，4结束')
    for i in range(5):
        print(i)
        print('hello world')
    print('----从3开始，6结束---')
    for i in range(3, 7):
        print(i)
    print('----从3开始，9结束，每次加2----', '*2表示步长')
    for i in range(3, 10, 2):
        print(i)
    print('----从10开始，3结束，每次加(-1)----', '*(-1)表示步长')
    for i in range(10, 3, -1):
        print(i)


alist = ['我', '光', '瓷', '香', '岩', '卿']
def xunhuan_list():
    for i in range(5):
        print(i)
        print(alist[i])
def xunhuan_list1():
    for i in alist:
        print(i)
        print('----')
def duanyan_assert():
    astr = '更符合国家的国防军'
    assert 'you' not in astr
def bidaxiao_if():
    a = 5
    b = 10
    if a > b:
        print(a)
    else:
        print(b)
def zhen_if():
    a = True
    if a:
        print('天地')
    else:
        print('土')
def bijiao_if():
    a = 4
    if a == 2:
        print('哈哈哈哈')
    elif a == 3:
        print('呵呵呵呵')
    elif a == 1:
        print('嘻嘻嘻嘻嘻')
    else:
        print('呀呀呀呀')
def tiaojian_xunhuan_while():
    a = 0
    while a < 5:
        print('nihao,feng')
        a += 1
def chuli_assert():
    try:
        assert 'ifgjh' in alist
        print('通过')
    except:
        print('报错了，断言没通过')
    print('----------')
def zhongzhi_break():   #终止第2次及之后的
    for i in range(5):
        print(i)
        if i == 2:
            break
        print('第%s次循环至最后一行代码\n'% i)
def zhongzhi_continue(): # 只终止第2次
    for j in range(5):
        print(j)
        if j == 2:
            continue
        print('第%s次循环至最后一行代码\n'%j)
if __name__ == '__main__':
    # xunhuan_range()
    # print('循环5次，打印i，打印alist[i]----')
    # xunhuan_list()
    # print('----i在alist里,循环并每次取值----')
    # xunhuan_list1()
    # print('----断言----')
    # duanyan_assert()
    # print('----if----')
    # bidaxiao_if()
    # zhen_if()
    # bijiao_if()
    # tiaojian_xunhuan_while()
    # chuli_assert()
    zhongzhi_break()
    print('****')
    zhongzhi_continue()


