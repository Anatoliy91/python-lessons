import requests
import json


def api_launch(headers):

    protocol = 'https://'
    base_url = 'qa.b2c.api.kantoo.com/'
    body = {
        'productID': 'disneystorytime',
        'deviceID': '781991',
        'ipAddress': '1.33.213.199',
        "appVersion": "1.01",
        "platform": "123",
        "deviceModel": "asda",
        "deviceOS": "123"}

    r = requests.post(protocol + base_url + 'appuser/launchapplication', data=json.dumps(body), headers=headers)
    print(r.text)
    return r



api_launch(headers={'Content-Type': 'application/json'})
