#  ���� j

# ����һ��list
# def list_bianli():
#     # ����һ��alist
#     alist = ['��', '������', '����', '���']
#     # ��alist ����ѭ��, ѭ�������� list �ĳ���������, ��һ��ѭ��
#     for i in alist:
#         print("--����")
#         print(i)
#         print(i + '__hello')

def nei_xunhuan():
    for i in range(5):
        print('hello word')
        for j in range(2):
            print('��ѭ��')

# ��ӡ �žų˷���
def chenfabiao():
    for i in range(1,10):
        for j in range(1,i+1):
            print('%s X %s = %s ' %(i,j,i*j),end=' ')
        print('     ')

# ���� if else �﷨��ʾ
def if_demo():
    a = False
    if a:
        print('a �� �Ե�')
    else:
        print('a �� ���')

# �ж� a �� b�Ĵ�С
def if_demo1():
    a = 10
    b = 20
    if a>b:
        print('a ���� b')
    else:
        print('a С�� b')

# ��� �Ƚϴ��ֵ
def if_demo2():
    a = 10
    b = 20
    if a>b:
        print(a)
    else:
        print(b)

def elif_demo():
    a = 4
    if a == 2:
        print('��1��if')
    elif a == 3:
        print('��2��if')
    elif a == 1:
        print('��3��if')
    else:
        print('else ��֧')

if __name__ == '__main__':
    # list_bianli()
    # nei_xunhuan()
    # �� 1��50 ������ ������
    nub=0
    for i in range(1,51):
        if i%2 != 0:
            nub = nub+i
    print(nub)
    # ��ĩ��ҵ
    # дһ������,�������� int����, ����������֮��� ż��������

