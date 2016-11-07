from django.contrib import admin

# Register your models here.
from .models import Post

class PostModelAdmin(admin.ModelAdmin):
	"""docstring for PostModelAdmin"""
	class Meta:
		model = Post
	list_display=["author", "title"]
	list_display_links=["title"]
	list_filter= ["timestamp"]
	search_fields =["title","author__name"]

admin.site.register(Post, PostModelAdmin)