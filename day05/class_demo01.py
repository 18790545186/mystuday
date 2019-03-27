# coding=utf-8
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


if __name__ == '__main__':
    human = Human('cpp', 18, '女')
    print(type(human))
    human.myInfo()
    result = human.myInfoStr()
    print(result)
    human = Human('qingqing', 27, '女')
    human.myInfo()
