from __future__ import unicode_literals

from django.db import models


class User(models.Model):
	"""docstring for Posts"""

	name = models.CharField(max_length=30)
	user_id = models.EmailField(max_length=30,primary_key=True)
	user_pwd = models.CharField(max_length=30)
	contact = models.IntegerField()
	address = models.TextField()
	timestamp = models.DateTimeField(auto_now=False,auto_now_add=True)
	

	def __unicode__(self):
		return self.name
	def __str__(self):
		return self.name
	
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
	
