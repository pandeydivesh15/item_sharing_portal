from __future__ import unicode_literals
from django.dispatch import receiver
from django.db.models.signals import pre_delete
from django.db import models
from django.core.urlresolvers import reverse

class User(models.Model):
	"""docstring for Posts"""

	auto_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=30)
	user_id = models.EmailField(max_length=30,unique=True)
	user_pwd = models.CharField(max_length=30)
	is_online = models.BooleanField(default = False)

	image = models.ImageField(
		upload_to = "All Profile Images",
		null = True, blank = True,
		width_field = "width_field",
		height_field = "height_field")
	width_field = models.IntegerField(default = 0)
	height_field = models.IntegerField(default = 0)

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
		user = User.objects.filter(user_id=request.session["user_mail_id"])[0]
		user.is_online = False
		user.save()

		del request.session["user_mail_id"]
		return True
	return False
	
@receiver(pre_delete, sender=User)
def user_image_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.image.delete(False)