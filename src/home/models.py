from __future__ import unicode_literals

from django.db import models

# Create your models here.
class feedback_data(models.Model):
	improvements=models.CharField(max_length=500)
	complain=models.CharField(max_length=500)
