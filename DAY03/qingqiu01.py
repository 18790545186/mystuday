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
    # response.status_code ��Ӧ�����code  code ��Ӧ�������
    assert 200 == response.status_code
    assert '�ɹ�' in json_body['message']
    assert 200 == json_body['code']

    data_dict = json_body['data']
    token_head = data_dict['tokenHead']
    token_ = data_dict['token']
    head = {'Authorization': token_head + ' ' + token_}
    get_info = requests.get(url='http://192.168.60.132:8080/admin/info', headers=head)
    print(get_info.json())
    info_json = get_info.json()
    assert 200 == get_info.status_code
    assert '�ɹ�' in info_json['message']
    assert 200 == info_json['code']
    # ��������װ�ɴʵ� ����ֵ��param
    param = {'pageNum':1,'pageSize':3}
    get_brand = requests.get('http://192.168.60.132:8080/brand/list', params=param, headers=head)
    # ��ӡ����get_brand����Ӧ����
    print(get_brand.text)
    # ��ȡ�ֵ��ʽ����Ӧ����
    json_brand = get_brand.json()
    # ��ȡ���ֵ��ʽ����Ӧ���ģ��е�dataֵ
    data_brand = json_brand['data']
    # ��ȡjson_brand�ֵ��еĿ���Ϊlist��ֵ��ע�����ֵ��һ��list�� ���� ���Ա�����
    list_brand = data_brand['list']
    # ���� list_brand
    for i in list_brand:
        print(i)


if __name__ == '__main__':
    req_demo()





