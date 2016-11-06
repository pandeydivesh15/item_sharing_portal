from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
# Create your views here.
from User.models import check_if_auth_user
from post.models import Post

def index_page(request):
	user = check_if_auth_user(request)
	context_data = {
		"user" : user,
		"all_posts" : Post.objects.all(),
	}
	return render(request, "index.html" , context_data)
