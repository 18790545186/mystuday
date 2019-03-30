import json

# 声明一个全局dict 变量(字典类型)
adict = {"name":"admin","pwd":"123456"}
# 字典类型转换成字符串类型
adictstr = '{"name":"admin","pwd":"123456"}'

bdict = {"名字":"杨阳洋","性别":"男"}
if __name__ == '__main__':

    s = json.dumps(bdict, ensure_ascii=False)
    print(s)
    print(type(s))
    # 取出并删除名字
    # adict.pop('name')
    # 错误示范：“adict.pop('admin')”括号里面应该是Key 不能直接写value
    #查询：打印出名字
    # print(adict['name'])
    # print(adict)
    aint = '字符串转字典'
    print(aint)
    # 字符串转成字典 str-->dict
    # 打印变量adictstr（字符串）
    bint = '字符串'
    print(bint)
    print(adictstr)
    # 打印adictstr的类型
    bint1 = '类型'
    print(bint1)
    print(type(adictstr))
    # str-->dict 并赋值给loads
    loads = json.loads(adictstr)
    # 打印变量loads
    print(loads)
    # 打印变量loads的类型
    print(type(loads))
    aint1 = '字典转字符串'
    print(aint1)
    # 字典转成字符串 dict-->str
    # 打印变量adict（字典）
    print(adict)
    # 打印adict的类型
    print(type(adict))
    # dict-->str  并赋值给dumps
    dumps = json.dumps(adict)
    # 打印变量dumps
    print(dumps)
    # 打印变量dumps的类型
    print(type(dumps))
    pass