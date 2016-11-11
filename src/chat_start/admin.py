from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import Chat

class UserModelAdmin(admin.ModelAdmin):
	"""docstring for PostModelAdmin"""
	class Meta:
		model = Chat
	list_display=["message", "chat_sender", "chat_reciever"]
	list_display_links=["message"]
	list_filter= ["timestamp"]
	
admin.site.register(Chat, UserModelAdmin)