from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from django.contrib import messages
# Create your views here.
from .models import Post
from User.models import User, check_if_auth_user

def posts_list(request, querySet_list, context_data = None): # Listing Posts
	paginator = Paginator(querySet_list, 6) # Show 5 queries per page

	page = request.GET.get('page') #'page' denotes the page number
	try:
		querySet = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		querySet = paginator.page(1)
	except EmptyPage:
		#If page is out of range (e.g. 9999), deliver last page of results.
		querySet = paginator.page(paginator.num_pages)
	
	new_context_data={
		"all_posts": querySet
	}
	new_context_data.update(context_data)
	return render(request, "postsList.html", new_context_data)

#CRUD implemented here
def posts_create(request):
	check = check_if_auth_user(request)
	if not check:
		messages.error(request, "Perform login first to create new post")
		return redirect("home:welcome")
	current_user = User.objects.filter(user_id = check)[0]

	if request.method == "POST":
		title = request.POST.get('item_title')
		disc = request.POST.get('item_disc')
		category = request.POST.get('item_category')
		image = request.FILES['item_image']	
		price = request.POST.get('item_price')

		new_post = Post(
					title = title,
					author = current_user,
					description = disc,
					category = category,
					image = image,
					price = price)
		new_post.save()
		messages.success(request, "New Post Created")
		return redirect(new_post.getAbsoluteURL())

	contextData={
			"user" : current_user,
	}
	return render(request,"createPost.html")

def posts_detail(request,id=None):
	instance=get_object_or_404(Post,id=id)
	check = check_if_auth_user(request)
	current_user = None
	if check:
		current_user = User.objects.filter(user_id = check)[0]
	contextData={
		"user" : current_user,
		"post_obj": instance,
	}
	return render(request, "showPost.html", contextData)


def posts_update(request,id=None):
	check = check_if_auth_user(request)
	if not check:
		messages.error(request, "Perform login first to edit any post")
		return redirect("home:welcome")

	current_user = User.objects.filter(user_id = check)[0]
	instance=get_object_or_404(Post,id=id)

	if instance.author.user_id != current_user.user_id:
		messages.error(request, "You can't edit this post." + str(instance.author.user_id))
		return redirect("home:welcome")

	contextData={
		"user" : current_user,
		"post_obj": instance,
	}
	if request.method == "POST":
		title = request.POST.get('item_title')
		disc = request.POST.get('item_disc')
		category = request.POST.get('item_category')
		image = request.FILES['item_image']	
		price = request.POST.get('item_price')

		instance.title = title
		instance.description = disc
		instance.category = category
		instance.image = image
		instance.price = price
		instance.save()
		messages.success(request, "Post updated")
		return redirect(instance.getAbsoluteURL())
	return render(request, "editPost.html", contextData)


def posts_delete(request, id=None):
	check = check_if_auth_user(request)
	if not check:
		messages.error(request, "Perform login first to delete any post")
		return redirect("home:welcome")
	current_user = User.objects.filter(user_id = check)[0]
	instance=get_object_or_404(Post,id=id)
	if instance.author != current_user:
		messages.error(request, "You can't delete this post.")
	else:
		instance=get_object_or_404(Post,id=id)
		instance.delete()
		messages.success(request,"Post successfully deleted")
	return redirect("home:welcome")
