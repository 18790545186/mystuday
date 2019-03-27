# coding=utf-8
import requests
def dianshang_request():
    # 登录
    login_data = {"username":"admin","password":"123456"}
    login_response = requests.post(url='http://192.168.60.132:8080/admin/login', json=login_data)
    login_response_json = login_response.json()
    print(type(login_response_json))
    print(login_response_json)
    # 从登录的response中
    data_login = login_response_json['data']
    tokenhead_login = data_login['tokenHead']
    token_login = data_login['token']
    head = {'Authorization':tokenhead_login+token_login}
    #查询用户信息
    response_info = requests.get(url='http://192.168.60.132:8080/admin/info', headers=head)
    print(response_info.json())
    #查询订单代发货的订单信息
    id_params={'pageNum':1,'pageSize':10,'status':1}
    response_id = requests.get(url='http://192.168.60.132:8080/order/list', headers=head, params=id_params)
    print(response_id.json())
    # 订单发货
    requests.post(url='http://192.168.60.132:8080/order/update/delivery',)


if __name__ == '__main__':
    dianshang_request()



    pass