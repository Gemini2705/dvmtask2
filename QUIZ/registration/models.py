from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class usertype(models.Model):
	username = models.ForeignKey(User, on_delete=models.CASCADE)
	utype = models.TextField(max_length=10 , default = 'taker')