from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Chat(models.Model):
	auto_id = models.AutoField(primary_key=True)
	chat_sender = models.CharField(max_length=30)
	chat_reciever = models.CharField(max_length=30)
	message = models.TextField()
	timestamp = models.DateTimeField(auto_now=False,auto_now_add=True)

	def __unicode__(self):
		return self.message
	def get_return_url(self):
		return reverse("chat:chat_start", kwargs={ "id":self.chat_reciever.auto_id})
