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
    url = get_baseurl('btc-qa') + "/appuser/launchapplication"
    resp = post_default_request(url=url, data=body_json, headers=headers)
    text_data = default_json_to_dict(resp.text)
    # print(resp)
    # print(text_data)
    # print(code_checker(resp, 201))
    # print(check_userType(text_data, 0))
    if check_deviceid(text_data, "12312313123") == True:
        print("EGEGEGEY")

    if check_productID(text_data, "disneystorytime-pt") == True:
        print("OK")

    if text_data["appUserID"] == "20194254746552375280":
        print("True")
    else:
        print("False")
    return resp


resp = test_check_resp()


def test_check_resp_loginregular():
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
    url = get_baseurl('btc-qa') + "/appuser/launchapplication"
    resp = post_default_request(url=url, data=body_json, headers=headers)
    text_data = default_json_to_dict(resp.text)
    # print(resp)
    # print(text_data)
    # print(code_checker(resp, 201))
    # print(check_userType(text_data, 0))

    body = {
        "productID": "disneystorytime-pt",
        "deviceID": "denysenko_device_2",
        "appUserID": text_data["appUserID"],
        "registrationType": 1,
        "email": get_random_email(),
        "password": get_random_password()
    }
    body_json = default_dict_to_json(body)
    headers = get_headers()
    #  headers_json = default_dict_to_json(headers)
    url = get_baseurl('btc-qa') + "/appuser/loginregular"
    resp = post_default_request(url=url, data=body_json, headers=headers)
    text_data = default_json_to_dict(resp.text)
    # print(resp)
    # print(text_data)
    # print(code_checker(resp, 201))
    # print(check_userType(text_data, 0))


test_check_resp()

print(test_check_resp_loginregular())


def test_check_resp_loginregular():
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
    url = get_baseurl('btc-qa') + "/appuser/launchapplication"
    resp = post_default_request(url=url, data=body_json, headers=headers)
    text_data = default_json_to_dict(resp.text)
    # print(resp)
    # print(text_data)
    # print(code_checker(resp, 201))
    # print(check_userType(text_data, 0))

    password = get_random_password()
    email = get_random_email()
    body = {
        "productID": "disneystorytime-pt",
        "deviceID": "denysenko_device_2",
        "appUserID": text_data["appUserID"],
        "registrationType": 1,
        "email": email,
        "password": password
    }
    body_json = default_dict_to_json(body)
    headers = get_headers()
    #  headers_json = default_dict_to_json(headers)
    url = get_baseurl('btc-qa') + "/appuser/signup"
    resp = post_default_request(url=url, data=body_json, headers=headers)
    text_data = default_json_to_dict(resp.text)
    # print(resp)
    # print(text_data)
    # print(code_checker(resp, 201))
    # print(check_userType(text_data, 0))

    body = {
        "deviceID": "781991",
        "appUserID": text_data["appUserID"],
        "productID": "disneystorytime-pt",
        "email": email,
        "password": password,
        "registrationType": "1",
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
    text_data = default_json_to_dict(resp.text)
    print(resp)
    print(text_data)
    print(code_checker(resp, 201))
    print(check_userType(text_data, 0))
    if text_data["failureReason"] == 3:
        print("failureReason = TRUE")


test_check_resp()

print(test_check_resp_loginregular())

test_check_resp_loginregular()



def test_check_resp_chagelang():
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
    url = get_baseurl('btc-qa') + "/appuser/launchapplication"
    resp = post_default_request(url=url, data=body_json, headers=headers)
    text_data = default_json_to_dict(resp.text)
    # print(resp)
    # print(text_data)
    # print(code_checker(resp, 201))
    # print(check_userType(text_data, 0))

    password = get_random_password()
    email = get_random_email()
    body = {
        "productID": "disneystorytime-pt",
        "deviceID": "denysenko_device_2",
        "appUserID": text_data["appUserID"],
        "registrationType": 1,
        "email": email,
        "password": password
    }
    body_json = default_dict_to_json(body)
    headers = get_headers()
    #  headers_json = default_dict_to_json(headers)
    url = get_baseurl('btc-qa') + "/appuser/signup"
    resp = post_default_request(url=url, data=body_json, headers=headers)
    text_data = default_json_to_dict(resp.text)
    # print(resp)
    # print(text_data)
    # print(code_checker(resp, 201))
    # print(check_userType(text_data, 0))

    body = {
        "deviceID": "781991",
        "appUserID": text_data["appUserID"],
        "productID": "disneystorytime-pt",
        "email": email,
        "password": password,
        "registrationType": "1",
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
    text_data = default_json_to_dict(resp.text)
    print(resp)
    print(text_data)
    print(code_checker(resp, 201))
    print(check_userType(text_data, 0))
    if text_data["failureReason"] == 3:
        print("failureReason = TRUE")

    print("_______________________________________-")

    Body = {
        "productID": "disneystorytime-es",
        "productIDNew": "disneystorytime-pt",
        "deviceID": "781991",
        "appUserID": text_data["appUserID"]
    }
    body_json = default_dict_to_json(body)
    headers = get_headers()
    #  headers_json = default_dict_to_json(headers)
    url = get_baseurl('btc-qa') + "/appuser/edituser"
    resp = post_default_request(url=url, data=body_json, headers=headers)
    text_data = default_json_to_dict(resp.text)
    print(text_data["isSucceeded"])


test_check_resp_chagelang()