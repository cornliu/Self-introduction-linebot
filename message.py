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
        message.append(TextSendMessage(text="I major in Electrical Engineering. I got GPA: 4.17/4.30 in last semester and I am also the TA of Signals and Systems.\nThe following is my CV."))
        FlexMessage = json.load(open('Basicinfo_CV.json','r',encoding='utf-8'))
        message.append(FlexSendMessage('Basicinfo_CV', FlexMessage))
        return message
    elif msg.lower() == 'side project':
        user.state = 2
        message = list()
        message.append(TextSendMessage(text='I like to discover the inconvenience in our daily life. These following side projects are designed by myself and built in my own free time.'))
        FlexMessage = json.load(open('Sideproject.json','r',encoding='utf-8'))
        message.append(FlexMessage)
        return message
    elif msg.lower() == 'course':
        
    elif msg.lower() == 'contact':
        user.state = 5
        FlexMessage = json.load(open('Contact.json','r',encoding='utf-8'))
        return FlexSendMessage('Contact info',FlexMessage)
    else:
        return TextSendMessage(text='Hi! My name is Ric. You can click \"About Me\" and choose the following squares to know me more.')
