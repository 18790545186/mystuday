# list 可读 可改

# 访问方法
# 声明一个方法 list_demo
def list_demo():
    # 定义一个变量并赋值
    alist = [4, 'ysl', '8', 7, 'style',6, 2, 5]
    # 打印变量的元素(默认正序访问)
    # print(alist)
    print(blist)

# 更新列表中的元素
def list_update(alist):
    # 更新alist[0]的元素
    alist[0] = 5
    # 打印更新后的alist[0]的元素
    print(alist[0])
    print(alist)
    return alist
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
    print(alist[2:5])\


blist = [1,2,3,5]
def len_demo():
    print(blist)
    # 获取变量（blist）的长度  len()取括号里面的变量有多少个
    print(len(blist))
    print(alist)
    # 获取变量（alist）的长度
    print(len(alist))
# 取出并删除集合中的数据
def pop_demo(alist):
    # 打印取出来的变量（alist）集合的最后一个数，并且把alist集合中最后一个元素
    print(alist.pop())
    # 打印去掉最后一个元素之后的alist变量
    print(alist)
    # 取出并删除第五个元素，取索引/下标
    alist.pop(4)
    print(alist)
alist = [9,8,7,6,5,4,10,25,13,1]
# 将列表排序
def orderby_demo():
    print('调用正序排的方法')
    sort_demo()
    print('调用倒序排的方法')
    reverse_demo()
    pass
# 正序
def sort_demo():
    alist.sort()
    print(alist)
    pass
# 倒序
def reverse_demo():
    alist.reverse()
    print(alist)
    pass

if __name__ == '__main__':
    orderby_demo()
    # 注意方法调用执行的顺序
    # pop_demo(alist)
    # alist = [11, 8, 7, 6, 5, 4, 'cpp']
    # print('world')
    # print(blist)
    # list_demo()
    # len_demo()
    # list_update(alist)


    #
    # alist = [4, 'ysl', '8', 7, 'style', 6, 2, 5]
    # print(alist)
    # list_update(alist)
    pass