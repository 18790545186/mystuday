# coding=gbk
def xunhuan_range():
    print('----��0��ʼ��4����')
    for i in range(5):
        print(i)
        print('hello world')
    print('----��3��ʼ��6����---')
    for i in range(3, 7):
        print(i)
    print('----��3��ʼ��9������ÿ�μ�2----', '*2��ʾ����')
    for i in range(3, 10, 2):
        print(i)
    print('----��10��ʼ��3������ÿ�μ�(-1)----', '*(-1)��ʾ����')
    for i in range(10, 3, -1):
        print(i)


alist = ['��', '��', '��', '��', '��', '��']
def xunhuan_list():
    for i in range(5):
        print(i)
        print(alist[i])
def xunhuan_list1():
    for i in alist:
        print(i)
        print('----')
def duanyan_assert():
    astr = '�����Ϲ��ҵĹ�����'
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
        print('���')
    else:
        print('��')
def bijiao_if():
    a = 4
    if a == 2:
        print('��������')
    elif a == 3:
        print('�ǺǺǺ�')
    elif a == 1:
        print('����������')
    else:
        print('ѽѽѽѽ')
def tiaojian_xunhuan_while():
    a = 0
    while a < 5:
        print('nihao,feng')
        a += 1
def chuli_assert():
    try:
        assert 'ifgjh' in alist
        print('ͨ��')
    except:
        print('�����ˣ�����ûͨ��')
    print('----------')
def zhongzhi_break():   #��ֹ��2�μ�֮���
    for i in range(5):
        print(i)
        if i == 2:
            break
        print('��%s��ѭ�������һ�д���\n'% i)
def zhongzhi_continue(): # ֻ��ֹ��2��
    for j in range(5):
        print(j)
        if j == 2:
            continue
        print('��%s��ѭ�������һ�д���\n'%j)
if __name__ == '__main__':
    # xunhuan_range()
    # print('ѭ��5�Σ���ӡi����ӡalist[i]----')
    # xunhuan_list()
    # print('----i��alist��,ѭ����ÿ��ȡֵ----')
    # xunhuan_list1()
    # print('----����----')
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


