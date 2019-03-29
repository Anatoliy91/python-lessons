import requests
import json
import random

def ost_request():
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
    data ={
        "protocol" : protocol,
        "base_url" : base_url,
        "headers" : headers,
        "body" : body
    }
    return data

ost_request()

def api_launch():
    data = ost_request()
    protocol =  data["protocol"],
    base_url =  data["base_url"],
    headers = data["headers"],
    body = data["body"],
    bodynew = json.dumps(body)
    bodynew2 = {
        'productID': 'disneystorytime',
        'deviceID': '781991',
        'ipAddress': '1.33.213.199',
        "appVersion": "1.01",
        "platform": "123",
        "deviceModel": "asd",
        "deviceOS": "123"}
    r = requests.post(protocol + base_url + 'appuser/launchapplication', data=json.dumps(body), headers=json.dumps(headers))
    #r = requests.post('https://qa.b2c.api.kantoo.com/appuser/launchapplication', data=bodynew2, headers=headers)
    print(r.status_code)
    print(r.text)
    dic = json.loads(r.text)
    print(dic)
    keys_count = len(dic)
    appUserID = dic["appUserID"]
    print(appUserID)
    return r.text

print(api_launch())