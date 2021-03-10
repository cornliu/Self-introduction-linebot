#這些是LINE官方開放的套件組合透過import來套用這個檔案上
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *
from User import *
import json
from linebot.models import QuickReply, QuickReplyButton, MessageAction

def get_quick_reply(keywords: list):
    items = list()
    for keyword in keywords:
        items.append(QuickReplyButton(
            action=MessageAction(
            label=keyword,
            text=keyword
            )
        ))
    return QuickReply(
        items=items
    )

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
        message.append(TextSendMessage(text='I like to discover the inconvenience in our daily life. These following side projects are designed by myself, using the knowledge which learned in the class and built in my own free time.'))
        FlexMessage = json.load(open('Sideproject.json','r',encoding='utf-8'))
        message.append(FlexSendMessage('Sideproject', FlexMessage))
        return message
    elif msg.lower() == 'course':
        user.state = 3
        FlexMessage = json.load(open('Course.json','r',encoding='utf-8'))
        return FlexSendMessage('Course',FlexMessage)
    elif msg.lower() == 'skills':
        user.state = 4
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/qmzi3q8.jpg',
            preview_image_url='https://i.imgur.com/qmzi3q8.jpg'
        )
        return image_message
    elif msg.lower() == 'contact':
        user.state = 5
        FlexMessage = json.load(open('Contact.json','r',encoding='utf-8'))
        return FlexSendMessage('Contact info',FlexMessage)
    elif msg.lower() == 'extracurricular activities':
        user.state = 6
        FlexMessage = json.load(open('Activities.json','r',encoding='utf-8'))
        return FlexSendMessage('Activities',FlexMessage)
    else:
        # return TextSendMessage(text='Hi! My name is Ric. You can click \"About Me\" and choose the following squares to know me more.')
        return TextSendMessage(
                    text='Hi, If you wanna know me more, please click one topic that you are interested with.',
                    quick_reply=get_quick_reply(['Basic Info', 'Side Project', 'Course', 'Skills', 'Contact', 'Activities'])
        )
        # text_message = TextSendMessage(text='Hello, world',
        #                        quick_reply=QuickReply(items=[
        #                            QuickReplyButton(action=MessageAction(label="Basic Info", text="Basic Info")),
        #                            QuickReplyButton(action=MessageAction(label="Side Project", text="Side Project")),
        #                            QuickReplyButton(action=MessageAction(label="Course", text="Course")),
        #                            QuickReplyButton(action=MessageAction(label="Skills", text="Skills")),
        #                            QuickReplyButton(action=MessageAction(label="Contact", text="Contact")),
        #                            QuickReplyButton(action=MessageAction(label="Activities", text="Extracurricular Activities"))
        #                        ]))
        # return text_message

