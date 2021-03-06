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

def get_getblacklist_url():
    # возвращает базовую урлу в зависимости от энвайрмента
        return "http://api.yocard.staging.digicode.ua/mobileclient.svc/getblacklist"

def get_appversions_url():
    # возвращает базовую урлу в зависимости от энвайрмента
        return "http://api.yocard.staging.digicode.ua/mobileclient.svc/getappversions"

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
    t = text_data['GetCategoriesResult']
    print(t)
    t2 = t['Data']
    print(t2)
    assert resp.status_code == 200
    assert t2 == [{'Id': 1, 'MapId': 0, 'Name': 'Все'}, {'Id': 10, 'MapId': 0, 'Name': 'Еда и напитки'}, {'Id': 20, 'MapId': 0, 'Name': 'Развлечения'}, {'Id': 30, 'MapId': 0, 'Name': 'Авто'}, {'Id': 40, 'MapId': 0, 'Name': 'Мода'}, {'Id': 45, 'MapId': 0, 'Name': 'Здоровье'}, {'Id': 50, 'MapId': 0, 'Name': 'Электроника'}, {'Id': 60, 'MapId': 0, 'Name': 'Красота'}, {'Id': 70, 'MapId': 0, 'Name': 'Детям'}, {'Id': 80, 'MapId': 0, 'Name': 'Дом'}, {'Id': 100, 'MapId': 0, 'Name': 'Другое'}]

test_get_categories()




def test_get_blacklist():
    #body = default_body()
    #body_json = default_dict_to_json(body)
    body_json = '{"clientApplicationIdentifier":{"DeviceIdentifier":"b5a18f51-162b-4a93-887b-df7f9762321e","MobilePhoneNumber":"dubinaanatolii@gmail.com","Language":"ru","Platform":2,"SecurityKey":"6d8f7c53077f748d8a380048fbbb8919","Version":"3.2.3"}}'
    headers = get_headers()
    url = get_getblacklist_url()
    print(url)
    resp = post_default_request(url=url, data=body_json, headers=headers)
    print(resp.text)
    text_data = default_json_to_dict(resp.text)
    print(text_data)
    print(resp.status_code)
    #temp = text_data['Data']
    t = text_data['GetBlackListResult']
    print(t)
    t2 = t['Data']
    print(t2)
    assert resp.status_code == 200
    #assert t2 == [{'Id': 1, 'MapId': 0, 'Name': 'Все'}, {'Id': 10, 'MapId': 0, 'Name': 'Еда и напитки'}, {'Id': 20, 'MapId': 0, 'Name': 'Развлечения'}, {'Id': 30, 'MapId': 0, 'Name': 'Авто'}, {'Id': 40, 'MapId': 0, 'Name': 'Мода'}, {'Id': 45, 'MapId': 0, 'Name': 'Здоровье'}, {'Id': 50, 'MapId': 0, 'Name': 'Электроника'}, {'Id': 60, 'MapId': 0, 'Name': 'Красота'}, {'Id': 70, 'MapId': 0, 'Name': 'Детям'}, {'Id': 80, 'MapId': 0, 'Name': 'Дом'}, {'Id': 100, 'MapId': 0, 'Name': 'Другое'}]

test_get_blacklist()


def test_getappversions():
    #body = default_body()
    #body_json = default_dict_to_json(body)
    body_json = '{  "platform": "iOS"}'
    headers = get_headers()
    url = get_appversions_url()
    print(url)
    resp = post_default_request(url=url, data=body_json, headers=headers)
    print(resp.text)
    text_data = default_json_to_dict(resp.text)
    print(text_data)
    print(resp.status_code)

    text_data_results = text_data['GetAppVersionsResult']
    text_data_errormessage=text_data_results['ErrorMessage']
    print(text_data_errormessage)
    message_error = text_data_errormessage['Message']
    assert message_error == 'SUCCESS'
    assert resp.status_code == 200

test_getappversions()

def test_create_foxtrotcard():
    #body = default_body()
    #body_json = default_dict_to_json(body)
   # body_json = '{"clientApplicationIdentifier":{"DeviceIdentifier":"b5a18f51-162b-4a93-887b-df7f9762321e","MobilePhoneNumber":"dubinaanatolii@gmail.com","Language":"ru","Platform":2,"SecurityKey":"6d8f7c53077f748d8a380048fbbb8919","Version":"3.2.3"}}'
    body = body_for_foxtrotcard()
    headers = get_headers()
    url = get_categories_url()
    print(url)
    resp = post_default_request(url=url, data=body, headers=headers)
    print(resp.text)
    text_data = default_json_to_dict(resp.text)
    print(text_data)
    print(resp.status_code)
    #temp = text_data['Data']
    t = text_data['GetCategoriesResult']
    print(t)
    t2 = t['Data']
    print(t2)
    assert resp.status_code == 200
    assert t2 == [{'Id': 1, 'MapId': 0, 'Name': 'Все'}, {'Id': 10, 'MapId': 0, 'Name': 'Еда и напитки'}, {'Id': 20, 'MapId': 0, 'Name': 'Развлечения'}, {'Id': 30, 'MapId': 0, 'Name': 'Авто'}, {'Id': 40, 'MapId': 0, 'Name': 'Мода'}, {'Id': 45, 'MapId': 0, 'Name': 'Здоровье'}, {'Id': 50, 'MapId': 0, 'Name': 'Электроника'}, {'Id': 60, 'MapId': 0, 'Name': 'Красота'}, {'Id': 70, 'MapId': 0, 'Name': 'Детям'}, {'Id': 80, 'MapId': 0, 'Name': 'Дом'}, {'Id': 100, 'MapId': 0, 'Name': 'Другое'}]

test_get_categories()

def get_foxtrotcard_url():
    # возвращает базовую урлу в зависимости от энвайрмента
        return "http://api.yocard.staging.digicode.ua/mobileclient.svc/createcard"


def body_for_foxtrotcard():
    body = {
        "clientApplicationIdentifier": {
            "DeviceIdentifier": "b5a18f51-162b-4a93-887b-df7f9762321e",
            "MobilePhoneNumber": "dubinaanatolii@gmail.com",
            "SecurityKey": "6d8f7c53077f748d8a380048fbbb8919",
            "Version": "3.2.3",
            "Language": "ru",
            "Platform": 2
        },
        "foxtrotForm": {
            "FirstName": "Test",
            "LastName": "Tet2",
            "Email": "dubinaanatolii@gmail.com",
            "Birthday": "string"
        }
    }
    json_body_for_foxtrot = default_dict_to_json(body)
    return json_body_for_foxtrot


def test_create_foxtrotcard():
    #body = default_body()
    #body_json = default_dict_to_json(body)
   # body_json = '{"clientApplicationIdentifier":{"DeviceIdentifier":"b5a18f51-162b-4a93-887b-df7f9762321e","MobilePhoneNumber":"dubinaanatolii@gmail.com","Language":"ru","Platform":2,"SecurityKey":"6d8f7c53077f748d8a380048fbbb8919","Version":"3.2.3"}}'
    body = body_for_foxtrotcard()
    headers = get_headers()
    url = get_foxtrotcard_url()
    print(url)
    resp = post_default_request(url=url, data=body, headers=headers)
    print(resp.text)
    text_data = default_json_to_dict(resp.text)
    print(text_data)
    print(resp.status_code)
    #temp = text_data['Data']
    #t = text_data['ErrorMessage']
    #print(t)
    #t2 = t['Code']
    #print(t2)
    assert resp.status_code == 200
    #assert t2 == [{'Id': 1, 'MapId': 0, 'Name': 'Все'}, {'Id': 10, 'MapId': 0, 'Name': 'Еда и напитки'}, {'Id': 20, 'MapId': 0, 'Name': 'Развлечения'}, {'Id': 30, 'MapId': 0, 'Name': 'Авто'}, {'Id': 40, 'MapId': 0, 'Name': 'Мода'}, {'Id': 45, 'MapId': 0, 'Name': 'Здоровье'}, {'Id': 50, 'MapId': 0, 'Name': 'Электроника'}, {'Id': 60, 'MapId': 0, 'Name': 'Красота'}, {'Id': 70, 'MapId': 0, 'Name': 'Детям'}, {'Id': 80, 'MapId': 0, 'Name': 'Дом'}, {'Id': 100, 'MapId': 0, 'Name': 'Другое'}]

test_create_foxtrotcard()