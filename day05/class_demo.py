# coding=utf-8
# class 类
# object 对象 / 或者所有类的父类

# 声明一个语法：class:就是声明一个类； Human：类的名字，首字母大写；（）：括号里面填这个类的父类
class Human(object):
    # 类的初始化（init：初始化） self：就代表类 本身
    def __init__(self,name,age,sex):
        # 讲入参的name赋值给 类本身的name
        # self.name:.后面的name是类的属性
        self.name = name
        self.age =age
        self.sex =sex

        # 类里面声明一个叫 myInfo的方法。类里面的方法必传 self
    def myInfo(self):
        print('我叫%s,我今年%s岁,%s'%(self.name,self.age,self.sex))

    def myInfoStr(self):
        return '我叫%s,我今年%s岁,%s'%(self.name,self.age,self.sex)
# 声明一个Tester类，Tester继承Human
class Tester(Human):
    def zhixingCeshi(self):
        #调用父类的属性
        print(self.name)
        self.myInfo()
        print('娱乐中，勿扰')
        # 调用父类的方法

if __name__ == '__main__':
    # Human('cpp', 18, '女')调用Human这个类，初始化传入参数 = 后面是 对象 = 前面是对象名字
    human = Human('cpp', 18, '女')    # Human('cpp', 18, '女')调用Human这个类，初始化传入参数
    print(type(human))  #  打印传参之后返回结果的类型
    human.myInfo()  # 调用 Human类 里的 myInfo 方法 ，这个方法里没有return
    result = human.myInfoStr()  # 调用 Human类 里的 myInfoStr 方法 ，这个方法里有return
    print(result)

    print('-----')
    # Tester('cpp', 18, '女') 调用Tester类 继承了父类的属性 初始化传入参数 得到参数 起对象名字
    tester = Tester('qq', 18, '女')
    # tester.  对象tester调用方法
    tester.zhixingCeshi()