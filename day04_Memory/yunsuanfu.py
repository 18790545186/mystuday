# coding=gbk
# 取余

def jisuan(a,b):
    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)
    print(a % b)

def duibi(a,b,c):
    print(a > b)
    print(a < b)
    print(a == b)
    print(a == c)
    print(a >= b)
    print(a != b)

def deng(a):
    a += 1  # a = a+1
    print(a)
    a *= 2  # a = a*2
    print(a)
    a -= 5  # a = a-5
    print(a)
    a /= 2  # a = a/2
    print(a)


if __name__ == '__main__':
    jisuan(9, 2)
    print('----')
    duibi(1,2,3)
    print('----')
    deng(0)
    pass