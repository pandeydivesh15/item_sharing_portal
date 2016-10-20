from django.contrib import admin

# Register your models here.
from .models import User

class UserModelAdmin(admin.ModelAdmin):
	"""docstring for PostModelAdmin"""
	class Meta:
		model = User
	list_display=["name", "user_id", "user_pwd"]
	list_display_links=["name"]
	list_filter= ["timestamp"]
	search_fields =["name","user_id"]

admin.site.register(User, UserModelAdmin)