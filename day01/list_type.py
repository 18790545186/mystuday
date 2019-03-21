# 声明一个方法 list_demo
def list_demo():
    # 定义一个变量并赋值
    alist = [4, 'ysl', '8', 7, 'style',6, 2, 5]
    # 打印变量的元素(默认正序访问)
    print(alist)

# 更新列表中的元素
def list_update(alist):
    # 更新alist[0]的元素
    alist[0] = 5
    # 打印更新后的alist[0]的元素
    print(alist[0])
    print(alist)


# 声明一个方法 list_demo1
def list_demo1():
    # 定义一个变量并赋值
    alist = [4, 'ysl', '8', 7, 'style', 6, 2, 5]
    # 打印变量的元素(默认正序访问)
    print(alist)
    # 通过索引访问元素
    # 一、打印变量的元素(访问第N个元素，alist[M],M=N-1)
    # 访问第1个元素、第4元素
    print(alist[0])
    print(alist[3])
    # 二、打印变量的元素(访问倒数第N个元素，alist[M],M=-N)
    # 访问倒数第3个元素
    print(alist[-3])
    # 三、切片操作
    # 访问第3个到第5个元素(第3个元素的索引开始、第6个元素的索引结束)
    print(alist[2:5])





if __name__ == '__main__':
    list_demo1()
    # alist = [4, 'ysl', '8', 7, 'style', 6, 2, 5]
    # print(alist)
    # list_update(alist)
    pass