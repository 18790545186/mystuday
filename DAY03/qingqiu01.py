# coding=gbk
import requests

def req_demo():
    data = {"username": "admin", "password": "123456"}
    response = requests.post(url='http://192.168.60.132:8080/admin/login', json=data)
    text_body = response.text
    print(type(text_body))
    print(text_body)

    json_body1= response.json()
    print(json_body1)
    print(type(json_body1))

    json_body2 = response.json
    print(json_body2)
    print(type(json_body2))

    json_body = response.json()
    print(type(json_body))
    print(json_body)
    # response.status_code 响应行里的code  code 响应正文里的
    assert 200 == response.status_code
    assert '成功' in json_body['message']
    assert 200 == json_body['code']

    data_dict = json_body['data']
    token_head = data_dict['tokenHead']
    token_ = data_dict['token']
    head = {'Authorization': token_head + ' ' + token_}
    get_info = requests.get(url='http://192.168.60.132:8080/admin/info', headers=head)
    print(get_info.json())
    info_json = get_info.json()
    assert 200 == get_info.status_code
    assert '成功' in info_json['message']
    assert 200 == info_json['code']
    # 讲参数封装成词典 并赋值给param
    param = {'pageNum':1,'pageSize':3}
    get_brand = requests.get('http://192.168.60.132:8080/brand/list', params=param, headers=head)
    # 打印出来get_brand的响应正文
    print(get_brand.text)
    # 获取字典格式的响应正文
    json_brand = get_brand.json()
    # 获取（字典格式的响应正文）中的data值
    data_brand = json_brand['data']
    # 获取json_brand字典中的可以为list的值，注意这个值是一个list的 对象 可以被遍历
    list_brand = data_brand['list']
    # 遍历 list_brand
    for i in list_brand:
        print(i)


if __name__ == '__main__':
    req_demo()





