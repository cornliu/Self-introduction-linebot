from app.py import users
import User.py
def add_user(user_id):
    global users
    if user_id not in users.keys():
        users[user_id] = User(user_id)
    return