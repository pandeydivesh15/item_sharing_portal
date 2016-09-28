from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
# Create your views here.

def index_page(request):
	return render(request, "index.html")

def signup_page(request):
	return render(request, "signup.html")

def after_login(request):
	return render(request, "home.html")

def post_create_page(request):
	return render(request, "createPost.html")
