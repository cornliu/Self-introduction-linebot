#這些是LINE官方開放的套件組合透過import來套用這個檔案上
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *
from User import *
import json

def follow_event_message():
    return TextSendMessage(text='Hi! My name is Ric. You can click \"About Me\" and choose the following squares to know me more.')

def text_msg(user, msg):
    if msg.lower() == 'basic info':
        user.state = 1
        message = list()
        message.append(TextSendMessage(text="I major in Electrical Engineering, and I'm also a fast learner in many area\
 especially in software engineering.\nThe following is my projects experience and also tips of iceberg in my college life."))
        FlexMessage = json.load(open('Basicinfo_CV.json','r',encoding='utf-8'))
        message.append(FlexSendMessage('Basicinfo_CV', FlexMessage))
        return message
    if msg.lower() == 'side project':
        user.state = 2
        FlexMessage = json.load(open('Sideproject.json','r',encoding='utf-8'))
        return FlexSendMessage('Sideproject',FlexMessage)

    elif msg.lower() == 'contact':
        user.state = 5
        FlexMessage = json.load(open('Contact.json','r',encoding='utf-8'))
        return FlexSendMessage('Contact info',FlexMessage)