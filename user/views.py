from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,logout as auth_logout,login as auth_login
from django.http import HttpResponse
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from.forms import RegistrationForm,UserEditForm,ProfileEditForm
from .models import Profile
from post.models import Post
from django.contrib import  messages
from post import urls
# Create your views here.

def login(request):

    if request.method=="POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            user=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(request,username=user,password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('feed')
            else:
                msgs= messages.success(request, 'Invalid Credntials')
                return render(request,'user/login.html',{"form":form,'msgs':msgs})

    else:
        form=LoginForm()
        return render(request,'user/login.html',{"form":form})
def logout(request):
    auth_logout(request)
    return redirect('login')
@login_required
def index(request):
    current_user=request.user
    posts=Post.objects.filter(user=current_user)
    profile=Profile.objects.filter(user=current_user).first()


    return render(request,'user/index.html',{"posts":posts,'profile':profile})


def register(request):

    if request.method=="POST":
        user_form=RegistrationForm(request.POST)
        if user_form.is_valid:
            new_user=user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            msg=messages.success(request, 'Registration successful')
            return render(request,'user/login.html',{'msg':msg})
    else:
        user_form=RegistrationForm()
    return render(request,'user/register.html',{'user_form':user_form})
@login_required
def edit(request):
    if request.method=="POST":
        user_form=UserEditForm(instance=request.user,data=request.POST)
        profile_edit_form=ProfileEditForm(instance=request.user.profile,data=request.POST,files=request.FILES)

        if user_form.is_valid and profile_edit_form.is_valid:
            user_form.save()
            profile_edit_form.save()
            msg=messages.success(request, 'Profile updated!')
            return redirect('feed')
    else:
        user_form=UserEditForm(instance=request.user)
        profile_edit_form=ProfileEditForm(instance=request.user.profile)
    return render(request,'user/edit.html',{'user_form':user_form,'profile_form':profile_edit_form})


