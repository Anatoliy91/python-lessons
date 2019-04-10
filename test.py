import requests
import json
import random

def get_headers():
    # метод в зависимости от енвайрмента возвращает нужные хедеры
    headers = {'Content-Type': 'application/json'}
    return headers

def default_json_to_dict(json_data):
    # этот метод парсит Джейсон и возвращает дикт
    dict_data = json.loads(json_data)
    return dict_data

def get_cards_url():
    # возвращает базовую урлу в зависимости от энвайрмента
        return "http://api.yocard.staging.digicode.ua/mobileclient.svc/getCards"

def get_categories_url():
    # возвращает базовую урлу в зависимости от энвайрмента
        return "http://api.yocard.staging.digicode.ua/mobileclient.svc/getcategories"

def post_default_request(url, data, headers):
    # метод делает пост запрос и возвращает полностью весь респонс
    response = requests.post(url=url, data=data, headers=headers)
    return response

def default_dict_to_json(diction):
    jsondata = json.dumps(diction)
    # этот метод превращает дикт в Джейсон. Возвращает джейсон
    return jsondata

def default_body():
    body = {"clientApplicationIdentifier":{"DeviceIdentifier":"9988150e-2f3d-4281-b4d1-16ea96b2f7e7","MobilePhoneNumber":"ctanok@gmail.com","Language":"uk","Platform":2,"SecurityKey":"35caaa9fc0ecae8abbb8edc4d1bac17d","Version":"3.2.3"}}

    body_json = default_dict_to_json(body)
    return body_json


def test_get_cards():
    #body = default_body()
    #body_json = default_dict_to_json(body)
    body_json = '{"clientApplicationIdentifier":{"DeviceIdentifier":"b5a18f51-162b-4a93-887b-df7f9762321e","MobilePhoneNumber":"dubinaanatolii@gmail.com","Language":"ru","Platform":2,"SecurityKey":"6d8f7c53077f748d8a380048fbbb8919","Version":"3.2.3"}}'
    headers = get_headers()
    url = get_cards_url()
    print(url)
    resp = post_default_request(url=url, data=body_json, headers=headers)
    text_data = default_json_to_dict(resp.text)
    print(text_data)
    print(resp.status_code)
    assert resp.status_code == 200

test_get_cards()



def test_get_categories():
    #body = default_body()
    #body_json = default_dict_to_json(body)
    body_json = '{"clientApplicationIdentifier":{"DeviceIdentifier":"b5a18f51-162b-4a93-887b-df7f9762321e","MobilePhoneNumber":"dubinaanatolii@gmail.com","Language":"ru","Platform":2,"SecurityKey":"6d8f7c53077f748d8a380048fbbb8919","Version":"3.2.3"}}'
    headers = get_headers()
    url = get_categories_url()
    print(url)
    resp = post_default_request(url=url, data=body_json, headers=headers)
    print(resp.text)
    text_data = default_json_to_dict(resp.text)
    print(text_data)
    print(resp.status_code)
    #temp = text_data['Data']
    t = text_data['Data']
    print(t)

test_get_categories()
