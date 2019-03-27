# coding=utf-8
def write_open():
    t = open('test.text', 'a+')
    t.write('liang的方式来看了')
if __name__ == '__main__':
    write_open()