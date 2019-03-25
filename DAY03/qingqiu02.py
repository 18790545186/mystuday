# coding=gbk
import requests
def ruq_demo():
    # ��¼
    data = {"username": "admin", "password": "123456"}
    response = requests.post(url='http://192.168.60.132:8080/admin/login', json=data)
    text_body = response.text
    print(type(text_body))
    print(text_body)
    #
    json_body = response.json()
    print(type(json_body))
    print(json_body)
    # ��ѯ
    data_dict = json_body['data']
    token_head = data_dict['tokenHead']
    token_ = data_dict['token']
    head = {'Authorization': token_head + ' ' + token_}
    get_info = requests.get(url='http://192.168.60.132:8080/admin/info', headers=head)
    print(get_info.json())
    info_json = get_info.json()
    # ��ѯ����
    get_orderlist = requests.get('http://192.168.60.132:8080/order/list?pageNum=1&pageSize=10&status=1&orderType=',headers=head)
    print(get_orderlist.text)
    json_orderlist = get_orderlist.json()
    data_orderlist = json_orderlist['data']
    list_orderlist = data_orderlist['list']
    list_1 = list_orderlist[0]
    order_id = list_1['id']
    # ����
    delivery_data = [
                {
                  "deliveryCompany": "string",
                  "deliverySn": "string",
                  "orderId": order_id
                }
               ]
    delivery_post = requests.post('http://192.168.60.132:8080/order/update/delivery', headers=head, json=delivery_data)
    print(delivery_post.text)
    json = delivery_post.json()
    # �رն���
    close_param = {'ids':order_id,'note':'wangwang'}
    close_post = requests.post('http://192.168.60.132:8080/order/update/close', headers=head, params=close_param)
    print(close_post.text)
    close_json = close_post.json()


if __name__ == '__main__':
    ruq_demo()