import requests
import json
import random

def ran_email():
    email = "dubinaanatolii" + str(random.randrange(1000,10000)) + "@gmail.com"
    return email

def ran_password():
    password = "qwerty" + str(random.randrange(100,10000))
    return password

def post_default_request(url, data, headers):
    # метод делает пост запрос и возвращает полностью весь респонс
    response = requests.post(url=url, data=data, headers=headers)
    return response

def default_dict_to_json(diction):
    jsondata = json.dumps(diction)
    # этот метод превращает дикт в Джейсон. Возвращает джейсон
    return jsondata


def default_json_to_dict(json_data):
    # этот метод парсит Джейсон и возвращает дикт
    dict_data = json.loads(json_data)
    return dict_data

def get_headers():
    # метод в зависимости от енвайрмента возвращает нужные хедеры
    headers = {'Content-Type': 'application/json'}
    return headers

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


def code_checker(resp, code):
    if resp.status_code == code:
        print("Response code is OK, equal: " + str(code))

def default_body(productID,
                 deviceID,
                 ipAddress,
                 appVersion,
                 platform,
                 deviceModel,
                 deviceOS):
    body = {"productID": productID,
            "deviceID": deviceID,
            "ipAddress": ipAddress,
            "appVersion": appVersion,
            "platform": platform,
            "deviceModel": deviceModel,
            "deviceOS": deviceOS
            }
    # body_json = default_dict_to_json(body)
    return body


def test_check_resp():
    body = default_body("disneystorytime", "123", "1.33.213.199", "123", "iOS", "SGS S6", "Andr")
    body_json = default_dict_to_json(body)
    headers = get_headers()
    url = get_baseurl('btc-qa') + "/appuser/launchapplication"
    print(url)
    resp = post_default_request(url=url, data=body_json, headers=headers)
    text_data = default_json_to_dict(resp.text)
    print(text_data)

    body1 = default_body("disneystorytime-pt", "123", "1.33.213.199", "123", "iOS", "SGS S6", "Andr")
    body1['email']= ran_email()
    body1['password']= ran_password()
    body1['appUserID']= text_data["appUserID"]
    body1['registrationType']= "1"
    body_jsonsignup = default_dict_to_json(body1)
    headers = get_headers()
    urlq = get_baseurl('btc-qa') + "/appuser/signup"
    print(urlq)
    respsignup = post_default_request(url=urlq, data=body_jsonsignup, headers=headers)
    text_data1 = default_json_to_dict(respsignup.text)
    print(text_data1)


test_check_resp()