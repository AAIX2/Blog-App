from django.contrib.auth.models import User
from  django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
class Userregisterform(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email', 'password1','password2']

class UserUpdateform(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateform(forms.ModelForm):
    class Meta:
        model = Profile
        fields  = ['image']