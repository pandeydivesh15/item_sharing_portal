from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
# Create your views here.
from .models import User, start_user_session, check_if_auth_user, stop_user_session

def check_login(request):
	if check_if_auth_user(request):
		return redirect("home:welcome")
	temp_id = request.POST.get("username")
	temp_pwd = request.POST.get("password")
	contextData={}
	if temp_pwd and temp_id:
		ans = User.objects.raw('SELECT user_id, user_pwd FROM User_user')
		for person in ans:
			if person.user_id == temp_id:
				if person.user_pwd == temp_pwd:
					messages.success(request, "Successful Login")
					request = start_user_session(request, temp_id)
					return redirect("home:welcome")
				else:
					messages.error(request, "Enter correct password")
					return render(request, "login.html", contextData)

		else:
			messages.error(request, "No such mail ID exists")	
	return render(request, "login.html", contextData)


def signup_user(request):
	if check_if_auth_user(request):
		return redirect("home:welcome")
	name = request.POST.get('userName')
	email = request.POST.get('userEmail')
	pwd = request.POST.get('userPasswd')
	con = request.POST.get('userContact')
	add = request.POST.get('userAddress')

	try:
		if name and email and pwd and con and add:
			#sql = """INSERT INTO User_user( name, user_id, user_pwd, contact, address) 
			#		Values(%s,%s,%s,%s,%s)""" % ( name, email, pwd, con, add)
			usr = User(
					name = name,
					user_id = email,
					user_pwd = pwd,
					contact = con,
					address = add)
			usr.save()
			#ans = User.objects.raw(sql)
			messages.success(request, "Sign up was successful")
			messages.success(request, "Now you may login")
			return redirect("User:login")
	except Exception,error:
		messages.error(request, "Some Internal Error. May be this mail id is already registered.")
	return render(request, "signup.html")

def logout_user(request):
	if stop_user_session(request):
		messages.success(request,"Logout Successful. Thank You for visiting")
		return redirect("home:welcome")											#("feedback.html")
	else:
		messages.error(request,"Cant logout without any login")
		return redirect("home:welcome")

