from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
# Create your views here.
from User.models import User, check_if_auth_user
from .models import Chat

def recv_chat(request, id = None):
	check = check_if_auth_user(request)
	if not check:
		messages.error(request, "Perform login first to start chatting")
		return redirect("home:welcome")

	current_user = User.objects.filter(user_id = check)[0]
	other_user = get_object_or_404(User, auto_id = id)
	message = request.POST.get('chat_msg')

	try:
		if current_user and other_user and message:
			#sql = """INSERT INTO User_user( name, user_id, user_pwd, contact, address) 
			#		Values(%s,%s,%s,%s,%s)""" % ( name, email, pwd, con, add)
			chat = Chat(
					chat_sender = current_user,
					chat_reciever = other_user,
					message = message)
			chat.save()
			return redirect(chat.get_return_url())
	except Exception,error:
		messages.error(request, "Some Internal Error. Try again")
	return redirect(chat.get_return_url())


def begin_chat(request, id = None):
	check = check_if_auth_user(request)
	if not check:
		messages.error(request, "Perform login first to start chatting")
		return redirect("home:welcome")
	current_user = User.objects.filter(user_id = check)[0]
	other_user = get_object_or_404(User, auto_id = id)
	print type(current_user)
	print type(other_user)
	sql = """SELECT * FROM chat_start_chat
			 WHERE chat_sender='{0}' and chat_reciever='{1}'
			 OR chat_sender='{1}' and chat_reciever='{0}';"""

	chat_list = Chat.objects.raw(sql.format(current_user,other_user))
	context_data = {
		"user" : current_user,
		"other_user" : other_user,
		"chatmessage_list": chat_list,
	}
	return render(request, "chat.html",context_data)

