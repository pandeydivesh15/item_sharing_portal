from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
from django.dispatch import receiver
from django.db.models.signals import pre_delete

from User.models import User
import os

def upload_loc(instance, filename):
	name = os.path.basename(filename)
	return os.path.join(str(instance.author.user_id),name) 

# Create your models here.
class Post(models.Model):
	"""docstring for Posts"""
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length = 120)
	image = models.ImageField(
		upload_to = upload_loc,
		null = True, blank = True,
		width_field = "width_field",
		height_field = "height_field")
	width_field = models.IntegerField(default = 0)
	height_field = models.IntegerField(default = 0)

	reason_post = models.CharField(max_length = 10)
	description = models.TextField()
	category = models.CharField(max_length = 100)
	price = models.PositiveIntegerField(default = 0)
	updated = models.DateTimeField(auto_now=True,auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False,auto_now_add=True)
		
	def __unicode__(self):
		return self.title
	def __str__(self):
		return self.title
	
	def getAbsoluteURL(self):
		return reverse("post:detail", kwargs={ "id":self.id})

	class Meta:
		ordering = [ "-timestamp", "-updated" ] 

@receiver(pre_delete, sender=Post)
def user_image_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.image.delete(False)