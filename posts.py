import json
import requests
import random


def post_default_request(url, data, headers):
    # метод делает пост запрос и возвращает полностью весь респонс
    response = requests.post(url=url, data=data, headers=headers)
    return response


def default_dict_to_json(di):
    jsondata = json.dumps(di)
    # этот метод превращает дикт в Джейсон. Возвращает джецсон
    return jsondata


def default_json_to_dict(json_data):
    # этот метод парсит Джейсон и возвращает дикт
    dict_data = json.loads(json_data)
    return dict_data


def get_headers():
    # метод в зависимости от енвайрмента возвращает нужные хедеры
    headers = {'Content-Type': 'application/json'}
    return headers


def get_random_password():
    # возвращает рандомные пароль
    password = "qazzxc" + str(random.randrange(20, 2000))
    return password


def get_random_email():
    # возвращает рандомны емейл
    email = "dubinaanatolii" + str(random.randint(100, 1000) + "@gmail.com")
    return email


def get_baseurl(env):
    # возвращает базовую урлу в зависимости от энвайрмента
    if env == "btc-prod":
        return "https://prod.b2c.api.kantoo.com"
    if env == "btc-qa":
        return "https://qa.b2c.api.kantoo.com"
    if env == "btb-prod":
        return "https://apikantoo.com"
    if env == "btb-qa":
        return "https://qa.apikantoo.com"


def test_check_resp():
    body = {"productID": "disneystorytime",
            "deviceID": "12312313123",
            "ipAddress": "1.33.213.199",
            "appVersion": "1.01",
            "platform": "123",
            "deviceModel": "asda",
            "deviceOS": "123",
            "appUserID": "{{appUserID}}",
            "registrationType": 0

            }
    body_json = default_dict_to_json(body)
    headers = get_headers()
    #  headers_json = default_dict_to_json(headers)
    url = get_baseurl('btb-qa') + "/appuser/launchapplication"
    resp = post_default_request(url=url, data=body_json, headers=headers)
    text_data = default_json_to_dict(resp.text)
    print(resp)
    print(text_data)
    if text_data["appUserID"] == "20192262651252483124":
         print("True")
    else:
        print("False")
    return resp


test_check_resp()