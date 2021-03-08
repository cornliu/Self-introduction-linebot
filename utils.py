from app import users
import User
def add_user(user_id):
    global users
    if user_id not in users.keys():
        users[user_id] = User(user_id)
    return