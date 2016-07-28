from mongoengine import *

connect('test', host='127.0.0.1', port=27017)


class User(Document):
    userid = UUIDField(required=True, unique=True)
    username = StringField(required=True)
    usernickname = StringField(default='default')
    password = StringField(required=True)
    email = EmailField(required=True)
    register_date = DateTimeField(required=True)
    login_time = DateTimeField(required=True)
    logout_time = DateTimeField(required=True)


class Post(Document):
    postid = UUIDField(required=True, unique=True)
    postcomment = StringField(default='this is  a empty post')
    postcreattime = DateTimeField(required=True)
    postedittime = DateTimeField(required=True)
    postkeywords = StringField(default=None)
    postfllower = IntField(default=0)

