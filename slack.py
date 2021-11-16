import os
import userInfo
from slacker import Slacker
import requests


slack = None


def getSlack():
    return slack

def connect_slack():
    slack = Slacker(userInfo.getToken())

def post_message(channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+userInfo.getToken},
        data={"channel": channel,"text": text}
    )
    print(response)