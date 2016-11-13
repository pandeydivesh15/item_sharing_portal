import json
from channels import Group
from channels.sessions import channel_session

from User.models import User
from .models import Chat

@channel_session
def ws_connect(message):
    prefix, other, user = message['path'].strip('/').split('/')
    session_check = user + '-' + other

    Group('chat-' + session_check).add(message.reply_channel)
    message.channel_session['chat'] = session_check
    

@channel_session
def ws_receive(message):
    chat_users = message.channel_session['chat'].split('-')
    current_user = User.objects.filter(auto_id = int(chat_users[0]))[0]
    other_user = User.objects.filter(auto_id = int(chat_users[1]))[0]
    session_check1 = str(current_user.auto_id) + "-" + str(other_user.auto_id)
    session_check2 = str(other_user.auto_id) + "-" + str(current_user.auto_id)

    data = json.loads(message['text'])
    message=data['message']
    chat = Chat(
                chat_sender = current_user.user_id,
                chat_reciever = other_user.user_id, 
                message = message)
    chat.save()
    temp_dict = { "senderID": current_user.auto_id, 
                  "message" : message, 
                  "other_status" : other_user.is_online}
    Group('chat-'+ session_check1).send({'text': json.dumps(temp_dict)})
    Group('chat-'+ session_check2).send({'text': json.dumps(temp_dict)})

@channel_session
def ws_disconnect(message):
    chat_users = message.channel_session['chat'].split('-')
    current_user = User.objects.filter(auto_id = int(chat_users[0]))[0]
    other_user = User.objects.filter(auto_id = int(chat_users[1]))[0]
    session_check = str(current_user.auto_id) + "-" + str(other_user.auto_id)

    Group('chat-'+ session_check).discard(message.reply_channel)
