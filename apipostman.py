import requests
import json
import random

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
        "deviceModel": "asda",
        "deviceOS": "123"}

    r = requests.post(protocol + base_url + 'appuser/launchapplication', data=json.dumps(body), headers=headers)
    print(r.status_code)
    print(r.text)
    dic = json.loads(r.text)
    keys_count = len(dic)
    appUserID = dic["appUserID"]
    print(appUserID)
    return r.text, appUserID


text, userId = api_launch()


def sign_up(appUserID):
    protocol = 'https://'
    base_url = 'qa.b2c.api.kantoo.com/'
    headers = {'Content-Type': 'application/json'}
    body = {
        "deviceID": "anat12345678",
        "productID": "disneystorytime-pt",
        "email": "tester12345678@network-source.com",
        "password": "{}".format(random.randint(1,10)),
        "registrationType": 1,
        'appUserID': "{}".format(appUserID)
    }
    r = requests.post(protocol + base_url + 'appuser/signup', data=json.dumps(body), headers=headers)
    print(r.status_code)
    print(r.text)
    return r.text


sign_up(userId)

def random_password():
    password = ("vasya" + str(random.randrange(random.randint(100,1000), random.randint(1000,10000))))
    return password

print(random_password())


def login_regular(appUserID):
    protocol = 'https://'
    base_url = 'qa.b2c.api.kantoo.com/'
    headers = {'Content-Type': 'application/json'}
    body = {
        "productID": "disneystorytime-pt",
        "deviceID": "denysenko_device_2",
        "registrationType": 3,
        "email": "{{emailuser}}",
        "password": "{{password}}",
        'appUserID': "{}".format(appUserID)
    }
    r = requests.post(protocol + base_url + 'appuser/loginregular', data=json.dumps(body), headers=headers)
    print(r.status_code)
    print(r.text)
    return r.text

login_regular(userId)


sign_up(userId)


def login_regular_fb(appUserID):
    protocol = 'https://'
    base_url = 'qa.b2c.api.kantoo.com/'
    headers = {'Content-Type': 'application/json'}
    body = {
        "productID": "disneystorytime-pt",
        "deviceID": "12345",
        "appUserID": "{{appUserID}}",
        "registrationType": 2,
        "email": "dubinaanatolii@gmail.com",
        "password": "Yakov05042018"
}
    r = requests.post(protocol + base_url + 'appuser/loginregular', data=json.dumps(body), headers=headers)
    print(r.status_code)
    print(r.text)
    return r.text

login_regular_fb(userId)



def str_to_dict(r):
    r = api_launch()
    mydict = json.loads(r)
    return mydict




 # def user_type(userType):
 #     r = api_launch()
 #     r2 = json.loads(r)
 #     if r2["userType"] == userType:
 #         return True





# print(user_type(0))


# def login_regular_fb(appUserID):
#     protocol = 'https://'
#     base_url = 'qa.b2c.api.kantoo.com/'
#     headers = {'Content-Type': 'application/json'}
#     body = {
#         "productID": "disneystorytime-pt",
#         "deviceID": "12345",
#         "appUserID": "{}".format(appUserID),
#         "registrationType": 2,
#         "email": "dubinaanatolii" + str(random.randrange(1,11000)) + "@gmail.com",
#         "password": "Yakov05042018"
# }
#     r = requests.post(protocol + base_url + 'appuser/loginregular', data=json.dumps(body), headers=headers)
#     if r[appUserID] == 201923102619309283324:
#         print("true")
#     print(r.status_code)
#     print(r.text)
#     dic = json.loads(r.text)
#     return r.text
#
# login_regular_fb(userId)