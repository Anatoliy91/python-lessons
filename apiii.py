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
    email = "dubinaanatolii" + str(random.randint(100, 1000)) + "@gmail.com"
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


def code_checker(resp, code):
    if resp.status_code == code:
        print("Response code is OK, equal: " + str(code))
    else:
        raise Exception('Code should equals code: {}'.format(code))


def check_userType(text_data, usertype):
    if text_data["userType"] == usertype:
        print("User type =" + str(usertype))
    # else:
    #     print("Usertype")


def check_productID(text_data, productID):
    if text_data["productID"] == productID:
        return True
    else:
        return False


def check_deviceid(text_data, deviceID):
    if text_data["deviceID"] == deviceID:
        return True
    else:
        return False

def default_body(productID, deviceID, ipAddress, appVersion, platform):
    body = {"productID": "productID",
            "deviceID": "deviceID",
            "ipAddress": "ipAddress",
            "appVersion": "appVersion",
            "platform": "platform",
            }
    body_json = default_dict_to_json(body)



def test_check_resp_chagelang():
    body = default_body(productID = 123123, deviceID=123123, ipAddress=123123, appVersion=123, platform-123)
    body['email'] = "dubinaanatolii@gmail.com",
    body["password"] = "qwerty"
    headers = get_headers()
    url = get_baseurl('btc-qa') + "/appuser/launchapplication"
    resplaunch = post_default_request(url=url, data=default_body("body_json"), headers=headers)
    text_datalaunch = default_json_to_dict(resplaunch.text)
    # print(resp)
    print(text_datalaunch)
    # print(code_checker(resp, 201))
    # print(check_userType(text_data, 0))

    password = get_random_password()
    email = get_random_email()
    body = {
        "productID": "disneystorytime-pt",
        "deviceID": "denysenko_device_2",
        "appUserID": text_datalaunch["appUserID"],
        "registrationType": 0,
        "email": email,
        "password": password
    }
    body_json = default_dict_to_json(body)
    headers = get_headers()
    #  headers_json = default_dict_to_json(headers)
    url = get_baseurl('btc-qa') + "/appuser/signup"
    resp = post_default_request(url=url, data=body_json, headers=headers)
    text_datasignup = default_json_to_dict(resp.text)
    # print(resp)
    # print(text_data)
    # print(code_checker(resp, 201))
    # print(check_userType(text_data, 0))

    body = {
        "deviceID": "781991",
        "appUserID": text_datalaunch["appUserID"],
        "productID": "disneystorytime-pt",
        "email": email,
        "password": password,
        "registrationType": "0",
        "appVersion": "1.01",
        "platform": "123",
        "deviceModel": "123",
        "deviceOS": "123"
    }
    body_json = default_dict_to_json(body)
    headers = get_headers()
    #  headers_json = default_dict_to_json(headers)
    url = get_baseurl('btc-qa') + "/appuser/loginregular"
    resp = post_default_request(url=url, data=body_json, headers=headers)
    text_datalogin = default_json_to_dict(resp.text)
    print(resp)
    print(text_datalogin)
    print(code_checker(resp, 201))
    print(check_userType(text_datalogin, 0))
    if text_datalogin["failureReason"] == 3:
        print("failureReason = TRUE")

    print("_______________________________________-")

    Body = {
        "productID": "disneystorytime-es",
        "productIDNew": "disneystorytime-pt",
        "deviceID": "781991",
        "appUserID": text_datalaunch["appUserID"]
    }
    body_json2 = default_dict_to_json(body)
    headers = get_headers()
    #  headers_json = default_dict_to_json(headers)
    url = get_baseurl('btc-qa') + "/appuser/edituser"
    resp = post_default_request(url=url, data=body_json, headers=headers)
    text_dataas = default_json_to_dict(resp.text)
    print(text_dataas["isSucceeded"])


test_check_resp_chagelang()

