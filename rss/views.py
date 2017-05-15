# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import feedparser
from django.shortcuts import render,redirect

# from .forms import SignUpForm,LoginForm
from .models import Add
from .forms import SignUpForm,LoginForm,AddForm
from django.contrib.auth import(
	authenticate,
	login,
	logout,
	)



def sign_in(request):
	#import pdb;pdb.set_trace()
	title="Login"
	form=LoginForm(request.POST or None)

	context={
		'form':form,
		'title':title,
	}

	if form.is_valid():
		username=form.cleaned_data.get('username')
		password=form.cleaned_data.get('password')
		user=authenticate(username=username,password=password)
		login(request,user)
		print(request.user.is_authenticated())
		return redirect('/')
		# context={
		# 'title':"thank you",
		# }


	return render(request,'login.html',context)





def register(request):
	#import pdb;pdb.set_trace()
	title="Register"
	form=SignUpForm(request.POST or None)
	context={
		'form':form,
		'title':title,
	}
	if form.is_valid():
		instance=form.save(commit=False)
		password=form.cleaned_data.get('password')
		instance.set_password(password)
		instance.save()
		return redirect('/sign/')
		# context={
		# 	'title':"Thank you"
		# }
	return render(request,'register.html',context)



def add_data(request):
	#import pdb;pdb.set_trace()
	heading="Add Feed"
	form=AddForm(request.POST or None)
	context={
		'form':form,
		'heading':heading,
	}

	if form.is_valid():
		instance=form.save(commit=False)
		instance.author=request.user
		instance.save()
		return redirect('/display/')
	return render(request,'add.html',context)


def display_all(request):
	#import pdb;pdb.set_trace()
	data_list=Add.objects.filter(author=request.user)
	context={
		'data_list':data_list,
	}
	return render(request,'userhome.html',context)


def content(request,pk):
	#import pdb;pdb.set_trace()
	details=Add.objects.get(pk=pk)


	link =details.link	
	d = feedparser.parse(link)
	context = {
		"d": d, 
	}
	
	return render(request,'userdisplay.html',context)

def home(request):
	return render(request,'first.html',{})


def logout_view(request):
	logout(request)
	return render(request,'logout.html',{})
