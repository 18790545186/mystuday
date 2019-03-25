import os
def os_demo():
    # 获取当前目录的路径
    getcwd = os.getcwd()
    print(getcwd)
    # 获取上级目录的路径
    abspath = os.path.abspath('..')
    print(abspath)
    # 获取上上级目录的路径
    abspath1 = os.path.abspath('../..')
    print(abspath1)

def open_demo():
    text_io = open('C:/Users/Administrator/PycharmProjects/myedu/DAY03/test.text', 'w+')
    text_io.write('你好，果芽')

def open_demo1():
    text_io = open('C:/Users/Administrator/PycharmProjects/myedu/DAY03/test.text', 'a+')
    text_io.write('1你好，果芽')

def open_demo2():
    text_io = open('C:/Users/Administrator/PycharmProjects/myedu/DAY03/test.text', 'r')
    readline = text_io.readline()
    print(readline)
    readlines = text_io.readlines()
    print(readlines)


if __name__ == '__main__':
    os_demo()
    # 相对路径 ../test.text
    # 绝对路径 C:\Users\Administrator\PycharmProjects\myedu\test.text
    # open_demo()
    open_demo1()
    open_demo2()