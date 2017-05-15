# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class SignUp(models.Model):
	username=models.CharField(max_length=120,blank=False,null=False)
	email=models.EmailField()
	password=models.CharField(max_length=50,blank=False,null=False)
	timestamp=models.DateTimeField(auto_now_add=True,auto_now=False)

	def __str__(self):
		return self.username

class Add(models.Model):
	author=models.ForeignKey(User)
	title=models.CharField(max_length=120,blank=False,null=False)
	link=models.URLField()

	def __str__(self):
		return self.title