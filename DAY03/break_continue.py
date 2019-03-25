# break:终止全体循环  continue：终止本次循环
def break_demo():
    for i in range(5):
        print('第%s次循环'%i)
        if i ==2:
            break

def continue_demo():
    for i in range(5):
        print('第%s次循环'%i)
        if i ==2:
            print(' ')
            continue
        print('第%s次循环,if判断之后'%i)
        print(' ')


if __name__ == '__main__':
    break_demo()
    print('结束')
    print(' ')
    continue_demo()