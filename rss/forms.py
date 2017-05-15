

from django.contrib.auth import(
		authenticate,
		get_user_model,
		login,
		logout,

	)
from django import forms

from .models import Add

User=get_user_model()
class SignUpForm(forms.ModelForm):
	#import pdb;pdb.set_trace()
	email=forms.EmailField(label="Email field",required =True)
	#email2=forms.EmailField(label="confirm email")
	username=forms.CharField(max_length=120,required =True,label="username")
	password=forms.CharField(widget=forms.PasswordInput,label="password",required =True)
	password2=forms.CharField(widget=forms.PasswordInput,label="confirm password",required =True)

	class Meta:
		model=User
		fields=['username','email','password','password2']

	def clean(self,*args,**kwargs):
		#import pdb;pdb.set_trace()
		username=self.cleaned_data.get("username")
		email=self.cleaned_data.get('email')
		password=self.cleaned_data.get('password')
		password2=self.cleaned_data.get('password2')
		

		user_query=User.objects.filter(username=username)
		if user_query.exists():
			raise forms.ValidationError("username is already occur")

		if password != password2:
			raise forms.ValidationError("password miss mach found")
		return super(SignUpForm,self).clean(*args,**kwargs)




class LoginForm(forms.Form):
	#import pdb;pdb.set_trace()
	username=forms.CharField(max_length=120)
	password=forms.CharField(widget=forms.PasswordInput)

	def clean(self,*args,**kwargs):
		#import pdb;pdb.set_trace()
		username=self.cleaned_data.get('username')
		password=self.cleaned_data.get('password')

		login_query=User.objects.filter(username=username)
		if not login_query.exists():
			raise forms.ValidationError("Username or password does not exists")
		return super(LoginForm,self).clean(*args,**kwargs)



class AddForm(forms.ModelForm):
	class Meta:
		model=Add
		fields=['title','link']


