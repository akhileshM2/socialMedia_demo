from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Profile

class UserEditForm(forms.ModelForm):

    class Meta:
        model=User
        fields=['first_name','last_name','email']

class ProfileEditForm(forms.ModelForm):

    class Meta:
        model=Profile
        fields=['profile_photo']

class LoginForm(forms.Form):
    username=forms.CharField(max_length=200)
    password=forms.CharField(widget=forms.PasswordInput)


class RegistrationForm(forms.ModelForm):
    password=forms.CharField(label="password",widget=forms.PasswordInput)
    password_2=forms.CharField(label="confirm password",widget=forms.PasswordInput)
    
    class Meta:
        model=User
        fields=['username','email','first_name','last_name']
        
    def check(self):
        if self.cleaned_data['password']!=self.cleaned_data['password_2']:
            raise ValidationError('password_2','Password do not match')
        return self.cleaned_data['password_2']
    