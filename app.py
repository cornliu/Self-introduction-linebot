from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *


#======這裡是呼叫的檔案內容=====
from User import *
from message import *
#======這裡是呼叫的檔案內容=====

#======python的函數庫==========
import tempfile, os
import datetime
import time
#======python的函數庫==========

app = Flask(__name__)
static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp')
# Channel Access Token
line_bot_api = LineBotApi('kI7T/eUfF5eSYM+BhMK7LrzWuZyud3JVLsbMopPPFBaAWD/mo1T/JDzW2m+s62ynU/30o1r+59JFHBiO/KDGmrJZ4JwKZaxyQ6rMFXtd4z56KAjL/zmB6WjQ7gKgScVzKmIf+focFvhZYEhDwLHcxAdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('c0f6c754735cb9b273cc8158710cb4de')

users = dict()

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    global users
    if event.source.user_id not in users.keys():
        users[event.source.user_id] = User(event.source.user_id)
    line_bot_api.reply_message(event.reply_token, text_msg(users[line_id], event.message.text))

@handler.add(FollowEvent)
def handle_follow(event):
    global users
    if event.source.user_id not in users.keys():
        users[event.source.user_id] = User(event.source.user_id)
    line_bot_api.reply_message(event.reply_token, follow_event_message())

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
