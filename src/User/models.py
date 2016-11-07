from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

class User(models.Model):
	"""docstring for Posts"""

	auto_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=30)
	user_id = models.EmailField(max_length=30,unique=True)
	user_pwd = models.CharField(max_length=30)

	department = models.CharField(max_length=30)
	batch = models.CharField(max_length=10)
	contact = models.IntegerField()
	address = models.TextField()
	timestamp = models.DateTimeField(auto_now=False,auto_now_add=True)
	
	def __unicode__(self):
		return self.name
	def __str__(self):
		return self.name

	def get_chat_URL(self):
		return reverse("chat:chat_start", kwargs={ "id":self.auto_id})

	def get_absolute_url(self):
		return reverse("user:profile", kwargs={ "id":self.auto_id})

	
def start_user_session(request, user_id):
	request.session["user_mail_id"] = user_id
	return request

def check_if_auth_user(request):
	if request.session.has_key("user_mail_id"):
		return request.session["user_mail_id"]
	else:
		return None

def stop_user_session(request):
	if request.session.has_key("user_mail_id"):
		del request.session["user_mail_id"]
		return True
	return False
	
