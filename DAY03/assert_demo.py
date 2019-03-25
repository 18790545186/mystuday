# assert:断言、声明      except：把……除外
# try except 用来捕捉异常
def try_demo():
    a = "1234567"
    try:
        assert '8' in a
    except:
        print('a里面没有8')
    print('----')
def try_demo1():
    a = "1234567"
    try:
        assert '8' in a
    except:
        print('a里面没有8')
    finally:
        print('----')


if __name__ == '__main__':
    # try_demo()
    try_demo1()
    pass