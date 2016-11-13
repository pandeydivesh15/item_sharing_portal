from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.db.models import Count

# default Dict
from collections import defaultdict
# Create your views here.
from User.models import User, check_if_auth_user
from post.models import Post
from post.views import posts_list
from chat_start.models import Chat

CATEGORIES = {
		1: "Academic books",
		2: "Novels",
		3: "ED/Practical/Workshop Instruments ",
		4: "Daily Needs",
		5: "Electronic Appliances",
		6: "Motor Vehicle",
		7: "Mobiles",
		8: "Others",
	}

def category_match(id):
	global CATEGORIES
	length = len(CATEGORIES)
	if id > length:
		return CATEGORIES[length]
	return CATEGORIES[id]


def index_page(request):
	
	global CATEGORIES
	check = check_if_auth_user(request)
	current_user = None
	if check:
		current_user = User.objects.filter(user_id = check)[0]
	context_data = {
		"user" : current_user,
		"all_posts" : Post.objects.all(),
		"category" : CATEGORIES
	}
	return render(request, "index.html" , context_data)

def query_result(request):
	check =  check_if_auth_user(request)
	if not check:
		messages.error(request,"Perform login first to see any particular posts")
		return redirect("home:welcome")
	current_user = User.objects.filter(user_id = check)[0]

	query = request.GET.get("search_query")
	if not query:
		messages.error(request, "Enter some query first")
		return redirect("home:welcome")
	results = Post.objects.filter(title__icontains=query)
	results = results | Post.objects.filter(author__name__icontains=query)
	results = results | Post.objects.filter(description__icontains=query)
	# sql = """
	# 		SELECT * FROM post_post 
	# 		WHERE title LIKE '%s' OR description LIKE '%s' OR price LIKE '%s'
	# 		""" % (query , query ,query)
	# results = list(Post.objects.raw(sql))
	context_data = {
		"user" : current_user,
	}

	return posts_list(request, results, context_data)
def about_us(request):
        return render(request, "aboutus.html")
def faq(request):
	check =  check_if_auth_user(request)
	context_data = {
		"user" : check,
	}
	return render(request, "FAQ.html",context_data)

def category_result(request,id = None):
	check =  check_if_auth_user(request)
	if not check:
		messages.error(request,"Perform login first to see any particular posts")
		return redirect("home:welcome")

	current_user =  User.objects.filter(user_id = check)[0]
	req_cate = category_match(int(id))
	results = Post.objects.filter(category=req_cate)
	context_data = {
		"user" : current_user,
	}
	return posts_list(request, results, context_data)

def see_chats(request):
	check =  check_if_auth_user(request)
	if not check:
		messages.error(request,"Perform login first to see any chats")
		return redirect("home:welcome")
	current_user =  User.objects.filter(user_id = check)[0]
	objects = Chat.objects.filter(chat_sender=current_user.user_id)
	objects = objects | Chat.objects.filter(chat_reciever=current_user.user_id)
	objects.order_by('-timestamp')
	msg_user_list = defaultdict(int)
	# result = objects.annotate(msg_count=Count('chat_sender'))
	for obj in objects:
		if obj.chat_sender == current_user.user_id:
			temp = User.objects.filter(user_id = obj.chat_reciever)[0]
			msg_user_list[temp]+=1
		else:
			temp = User.objects.filter(user_id = obj.chat_sender)[0]
			msg_user_list[temp]+=1
	
	context_data = {
		"chatList" : dict(msg_user_list),
		"user" : current_user,
	}
	return render(request, "chatList.html", context_data)
	
