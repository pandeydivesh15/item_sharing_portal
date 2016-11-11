from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
# Create your views here.
from User.models import check_if_auth_user
from post.models import Post
from post.views import posts_list

def index_page(request):
	user = check_if_auth_user(request)
	context_data = {
		"user" : user,
		"all_posts" : Post.objects.all(),
	}
	return render(request, "index.html" , context_data)

def query_result(request):
	check =  check_if_auth_user(request)
	if not check:
		messages.error(request,"Perform login first to see any particular posts")
		return redirect("home:welcome")
	current_user =  check

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
        return render(request, "FAQ.html")
