import json
import requests

class Sender(object):
    def __init__(self):
        pass

    def sendTextMsg(self,api , msg):
        headers={'Content-Type': 'application/json'}
        data = {
        "msgtype":"text",
        "text": {"content":msg},
        "isAtAll": True,
        }
        requests.post(api, headers = headers, data = json.dumps(data))