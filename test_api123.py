import requests
import json
import random
import pytest

def ran_email():
    email = "dubinaanatolii" + str(random.randrange(1, 11000)) + "@gmail.com"
    return email


def ran_password():
    password = "qaz" + str(random.randrange(20, 2000))
    return password


def api_launch():
    protocol = 'https://'
    base_url = 'qa.b2c.api.kantoo.com/'
    headers = {'Content-Type': 'application/json'}
    body = {
        'productID': 'disneystorytime',
        'deviceID': '781991',
        'ipAddress': '1.33.213.199',
        "appVersion": "1.01",
        "platform": "123",
        "deviceModel": "asd",
        "deviceOS": "123"}
    r = requests.post(protocol + base_url + 'appuser/launchapplication', data=json.dumps(body), headers=headers)
    print(r.status_code)
    print(r.text)
    dic = json.loads(r.text)
    print(dic)
    keys_count = len(dic)
    appUserID = dic["appUserID"]
    print(appUserID)
    return r.text, dic


r_text, dic = api_launch()


def check_appUserId():
   if dic["appUserID"] == 201923102619309283324:
       print("true")
      return True




print(check_appUserId())


def check_productID():
    if dic["productID"] == 'disneystorytime-pt':
        return True


print(check_productID())


def sign_up():
    protocol = 'https://'
    base_url = 'qa.b2c.api.kantoo.com/'
    headers = {'Content-Type': 'application/json'}
    body = {
        "deviceID": "anat12345678",
        "productID": "disneystorytime-pt",
        "email": "tester12345678@network-source.com",
        # "email": "{}".format
        "password": ran_password(),
        # "password": "{}".format(random.randint(1,10)),
        "registrationType": 1,
        'appUserID': "{}".format(dic["appUserID"])
    }
    r = requests.post(protocol + base_url + 'appuser/signup', data=json.dumps(body), headers=headers)
    print(r.status_code)
    print(r.text)
    return r.text


sign_up()


def login_regular_fb(dic):
    protocol = 'https://'
    base_url = 'qa.b2c.api.kantoo.com/'
    headers = {'Content-Type': 'application/json'}
    body = {
        "productID": "disneystorytime-pt",
        "deviceID": "12345",
        'appUserID': "{}".format(dic["appUserID"]),
        "registrationType": 2,
        "email": "dubinaanatolii" + str(random.randrange(1, 11000)) + "@gmail.com",
        "password": ran_password()
    }
    r = requests.post(protocol + base_url + 'appuser/loginregular', data=json.dumps(body), headers=headers)

    print(r.status_code)
    print(r.text)
    if r.status_code == 201:
        print("test Passed")
    else:
        print('test failed error #' + " " + str(r.status_code))
    dic1 = json.loads(r.text)
    print(dic1)
    appusertmp = int(dic1["appUserID"])
    #print(appusertmp)
    if appusertmp == 201923102619309283324:
        print("true")
    userType = dic1["userType"]
    if userType == 0:
        print("sdfgsdfgsdfgsdfgdfgsdfgdfg")
    return r.text, appusertmp
    failureReason = dic1[failureReason]



login_regular_fb(dic)

def check_failurereason():
    protocol = 'https://'
    base_url = 'qa.b2c.api.kantoo.com/'
    headers = {'Content-Type': 'application/json'}
    body = {
        "productID": "disneystorytime-pt",
        "deviceID": "12345",
        'appUserID': "{}".format(dic["appUserID"]),
        "registrationType": 2,
        "email": "dubinaanatolii" + str(random.randrange(1, 11000)) + "@gmail.com",
        "password": ran_password()
    }
    r = requests.post(protocol + base_url + 'appuser/loginregular', data=json.dumps(body), headers=headers)
    if r.text["failureReason"] == 0:
        print("ok")
    elif r.text["failureReason"] == 1:
        print("not ok")
    elif r.text["failureReason"] == 2:
        print("not ok")
    elif r.text["failureReason"] == 3:
        print("not ok")