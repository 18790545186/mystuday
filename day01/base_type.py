# 多行加备注Ctrl+/
# model 模块
# main 主要的
# print 打印
# def 声明方法
# int 整数
# demo 例子
# class 类、类型
# str string 字符

# 声明一个int_demo方法
def int_demo():
    # 声明一个变量aint并赋值 1
    aint = 1
    # 打印出aint的值
    print(aint)
    # 打印aint的类型 type(aint)：获取aint的类型
    print(type(aint))


# 声明一个str_demo方法
def str_demo():
    # 声明一个变量aint并赋值 '1'
    astr = '1'
    # 打印出astr的值
    print(astr)
    # 打印aint的类型 type(astr)：获取astr的类型
    print(type(astr))


# 声明一个str_demo方法
def float_demo():
    # 声明一个变量aint并赋值 '1'
    afloat = 1.88
    # 打印出astr的值
    print(afloat)
    # 打印aint的类型 type(astr)：获取astr的类型
    print(type(afloat))


# 声明一个add方法，参数有两个 aint，bint
def add(aint, bint):
    # 打印aint参数
    print(aint)
    # 打印bint参数
    print(bint)
    # 返回aint+bint
    return aint + bint


# 声明一个sub方法，参数有两个: aint，bint
def sub(aint, bint):
    # 打印aint参数
    print(aint)
    # 打印bint的参数
    print(bint)
    # 返回aint+bint
    return aint - bint


# return后的代码不执行

def jiafa(aint,bint):
    print(aint)
    print(bint)
    return aint + bint


if __name__ == '__main__':
    result = jiafa(5,3)
    # result = jiafa(aint=5,bint=3)
    print(result)
    # float_demo()

    pass


    # float_demo()
    # float_demo()
    # str_demo()
    # int_demo()
    # result = add(1, 2)
    # print(result)
#  写add（值）点击Ctri+Alt+V出现位置写result（结果）
# result0 = add(3, 4)
# print(result0)
# result1 = sub(3, 4)
