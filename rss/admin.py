# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import SignUp
# from .forms import SignUpForm
# from django.contrib.auth import(
# 	authenticate,
# 	get_user_model,
# 	login,
# 	logout,
# 	)

# User=get_user_model()
# class SignUpAdmin(admin.ModelAdmin):
# 	# list_display=['__str__','email','timestamp']
# 	class Meta:
# 		model=User
# 	# form=SignUpForm

# admin.site.register(SignUpAdmin)
from .forms import SignUpForm


class SignUpAdmin(admin.ModelAdmin):
	form=SignUpForm

admin.site.register(SignUp,SignUpAdmin)