import requests
import json
import random
import pytest
import behave


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

def check_failereason(text_data):
    if text_data["failureReason"]==0:
        print("No error")
    if text_data["failureReason"]==1:
        print("Unknown")
    if text_data["failureReason"]==2:
        print("email already exists")
    if text_data["failureReason"]==3:
        print("email doesn't exists")
    if text_data["failureReason"]==4:
        print("Incorrect password")
    if text_data["failureReason"]==5:
        print("Incorrect MSISDN")
    if text_data["failureReason"]==6:
        print("Cancelled user")
    if text_data["failureReason"]==7:
        print("disabled user")
    if text_data["failureReason"]==8:
        print("User is logged on another devices")
    if text_data["failureReason"]==9:
        print("Incorrect email")
    if text_data["failureReason"]==10:
        print("Email and password are empty")
    if text_data["failureReason"]==11:
        print("Email is empty")

def default_body(productID, deviceID, ipAddress, appVersion, platform, deviceModel, deviceOS):
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
    url = get_baseurl('btc-prod') + "/appuser/launchapplication"
    print(url)
    resp = post_default_request(url=url, data=body_json, headers=headers)
    text_data = default_json_to_dict(resp.text)
    print(text_data)

    email = ran_email()
    password = ran_password()

    body1 = default_body("disneystorytime-pt", "123", "1.33.213.199", "123", "iOS", "SGS S6", "Andr")
    body1['email']= email
    body1['password']= password
    body1['appUserID']= text_data["appUserID"]
    body1['registrationType']= "1"
    body_jsonsignup = default_dict_to_json(body1)
    headers = get_headers()
    urlq = get_baseurl('btc-prod') + "/appuser/signup"
    print(urlq)
    respsignup = post_default_request(url=urlq, data=body_jsonsignup, headers=headers)
    text_data1 = default_json_to_dict(respsignup.text)
    print(text_data1)

    body2 = default_body("disneystorytime-pt", "123", "1.33.213.199", "123", "iOS", "SGS S6", "Andr")
    body1['email']= email
    body1['password']= password
    body1['appUserID'] = text_data["appUserID"]
    body1['registrationType'] = "1"
    body_jsonsignup = default_dict_to_json(body1)
    headers = get_headers()
    urlqw = get_baseurl('btc-prod') + "/appuser/loginregular"
    print(urlqw)
    resplogin = post_default_request(url=urlqw, data=body_jsonsignup, headers=headers)
    text_data2 = default_json_to_dict(resplogin.text)
    print(text_data2)
#    if text_data2.status_code == 201:
#        print("test Passed")
#    else:
#        print('test failed error #' + " " + str(text_data2.status_code))
#    assert text_data2.status_code == 201
    # check_failereason(text_data)
    assert respsignup.status_code == 201
    check_failereason(text_data1)
    check_failereason(text_data2)
    assert text_data2["failureReason"] == 3

def test_check_resp1():
    body = default_body("disneystorytime", "123", "1.33.213.199", "123", "iOS", "SGS S6", "Andr")
    body_json = default_dict_to_json(body)
    headers = get_headers()
    url = get_baseurl('btc-prod') + "/appuser/launchapplication"
    print(url)
    resp = post_default_request(url=url, data=body_json, headers=headers)
    text_data = default_json_to_dict(resp.text)
    print(text_data)

    email = ran_email()
    password = ran_password()

    body1 = default_body("disneystorytime-pt", "123", "1.33.213.199", "123", "iOS", "SGS S6", "Andr")
    body1['email']= email
    body1['password']= password
    body1['appUserID']= text_data["appUserID"]
    body1['registrationType']= "1"
    body_jsonsignup = default_dict_to_json(body1)
    headers = get_headers()
    urlq = get_baseurl('btc-prod') + "/appuser/signup"
    print(urlq)
    respsignup = post_default_request(url=urlq, data=body_jsonsignup, headers=headers)
    text_data1 = default_json_to_dict(respsignup.text)
    print(text_data1)

    body2 = default_body("disneystorytime-pt", "123", "1.33.213.199", "123", "iOS", "SGS S6", "Andr")
    body1['email']= email
    body1['password']= password
    body1['appUserID'] = text_data["appUserID"]
    body1['registrationType'] = "1"
    body_jsonsignup = default_dict_to_json(body1)
    headers = get_headers()
    urlqw = get_baseurl('btc-prod') + "/appuser/loginregular"
    print(urlqw)
    resplogin = post_default_request(url=urlqw, data=body_jsonsignup, headers=headers)
    text_data2 = default_json_to_dict(resplogin.text)
    print(text_data2)
#    if text_data2.status_code == 201:
#        print("test Passed")
#    else:
#        print('test failed error #' + " " + str(text_data2.status_code))
#    assert text_data2.status_code == 201
    # check_failereason(text_data)
    assert respsignup.status_code == 201
    check_failereason(text_data1)
    check_failereason(text_data2)
    assert text_data2["failureReason"] == 3

@given('we can launch application')
def test_check_resp2():
    body = default_body("disneystorytime", "123", "1.33.213.199", "123", "iOS", "SGS S6", "Andr")
    body_json = default_dict_to_json(body)
    headers = get_headers()
    url = get_baseurl('btc-prod') + "/appuser/launchapplication"
    print(url)
    resp = post_default_request(url=url, data=body_json, headers=headers)
    text_data = default_json_to_dict(resp.text)
    print(text_data)

    email = ran_email()
    password = ran_password()

    body1 = default_body("disneystorytime-pt", "123", "1.33.213.199", "123", "iOS", "SGS S6", "Andr")
    body1['email']= email
    body1['password']= password
    body1['appUserID']= text_data["appUserID"]
    body1['registrationType']= "1"
    body_jsonsignup = default_dict_to_json(body1)
    headers = get_headers()
    urlq = get_baseurl('btc-prod') + "/appuser/signup"
    print(urlq)
    respsignup = post_default_request(url=urlq, data=body_jsonsignup, headers=headers)
    text_data1 = default_json_to_dict(respsignup.text)
    print(text_data1)

    body2 = default_body("disneystorytime-pt", "123", "1.33.213.199", "123", "iOS", "SGS S6", "Andr")
    body1['email']= email
    body1['password']= password
    body1['appUserID'] = text_data["appUserID"]
    body1['registrationType'] = "1"
    body_jsonsignup = default_dict_to_json(body1)
    headers = get_headers()
    urlqw = get_baseurl('btc-prod') + "/appuser/loginregular"
    print(urlqw)
    resplogin = post_default_request(url=urlqw, data=body_jsonsignup, headers=headers)
    text_data2 = default_json_to_dict(resplogin.text)
    print(text_data2)
#    if text_data2.status_code == 201:
#        print("test Passed")
#    else:
#        print('test failed error #' + " " + str(text_data2.status_code))
#    assert text_data2.status_code == 201
    # check_failereason(text_data)
    assert respsignup.status_code == 201
    check_failereason(text_data1)
    check_failereason(text_data2)
    assert text_data1["failureReason"] == 0

test_check_resp()

test_check_resp2()

test_check_resp1()