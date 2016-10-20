from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
# Create your views here.
from User.models import check_if_auth_user

def index_page(request):
	user = check_if_auth_user(request)
	context_data = {
		"user" : user,
	}
	return render(request, "index.html" , context_data )

def signup_page(request):
	return render(request, "signup.html")


def post_create_page(request):
	return render(request, "createPost.html")
