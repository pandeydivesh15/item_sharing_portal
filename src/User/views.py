from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
# Create your views here.
from .models import User, start_user_session, check_if_auth_user, stop_user_session
from .mail import mail_send_to

def check_login(request):
	if check_if_auth_user(request):
		messages.error(request, "Log out to perform Log in")
		return redirect("home:welcome")
	temp_id = request.POST.get("username")
	temp_pwd = request.POST.get("password")
	contextData={}
	if temp_pwd and temp_id:
		ans = User.objects.raw('SELECT user_id, user_pwd, auto_id FROM User_user')
		for person in ans:
			if person.user_id == temp_id:
				if person.user_pwd == temp_pwd:
					messages.success(request, "Successful Login")
					person.is_online = True
					person.save()
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
		messages.error(request, "Log out to perform sign up")
		return redirect("home:welcome")
	name = request.POST.get('userName')
	email = request.POST.get('userEmail')
	pwd = request.POST.get('userPasswd')
	batch = request.POST.get('userBatch')
	department = request.POST.get('userDepartment')
	con = request.POST.get('userContact')
	add = request.POST.get('userAddress')
	


	
	if name and email and pwd and con and add:
		#sql = """INSERT INTO User_user( name, user_id, user_pwd, contact, address) 
		#		Values(%s,%s,%s,%s,%s)""" % ( name, email, pwd, con, add)
		image = request.FILES['user_image']
		usr = User(
				name = name,
				user_id = email,
				user_pwd = pwd,
				batch = batch,
				department = department,
				contact = con,
				address = add,
				image = image)
		usr.save()
		#ans = User.objects.raw(sql)
		messages.success(request, "Sign up was successful")
		messages.success(request, "Now you may login")
		#Send Welcome mail
		mail_send_to(usr)
		return redirect("user:login")
	
	return render(request, "signup.html")

def logout_user(request):
	if stop_user_session(request):
		messages.success(request,"Logout Successful. Thank You for visiting")
		return redirect("home:welcome")											#("feedback.html")
	else:
		messages.error(request,"Cant logout without any login")
		return redirect("home:welcome")

def user_profile(request,id=None):
	check = check_if_auth_user(request);
	if not check:
		messages.success(request,"Perform Login first")
		return redirect("home:welcome")

	current_user = User.objects.filter(user_id = check)[0]
	other_user = get_object_or_404(User, auto_id = id)

	if current_user == other_user:
		contextData = {
			"user" : current_user,
			"profile_user": current_user,
		}
	else:
		contextData = {
		"user" : current_user,
		"chat_link_user" : other_user,
		"profile_user": other_user, 
		}
	return render(request, "profile.html", contextData)