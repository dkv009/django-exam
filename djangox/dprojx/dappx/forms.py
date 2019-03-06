from django.forms import ModelForm
from django import forms
from dappx.models import UserProfileInfo
from django.contrib.auth.models import User

from .models import Post


class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
 
	class Meta():
		model = User
		fields = ('username','password','email')
class UserProfileInfoForm(forms.ModelForm):
 
	class Meta():
		model = UserProfileInfo
		fields = ('portfolio_site','profile_pic')
		

		
		
		
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','text',)		