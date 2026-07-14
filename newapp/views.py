from django.shortcuts import render, redirect
from .forms import UserCreate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate, login,logout,update_session_auth_hash


def sign_up(request):
    if request.method == 'POST':
        form = UserCreate(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully.')
            return redirect('login')   # Redirect after successful signup
    else:
        form = UserCreate()

    return render(request, 'signup.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('profile')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


def profile(request):
    return render(request, 'profile.html')



def user_logout(request):
    logout(request)
    return redirect('login')


def pass_change(request):
    if request.method=='POST':
        form=PasswordChangeForm(user=request.user,data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,request.user)
            return redirect('profile')
    else:
        form=PasswordChangeForm(user=request.user)
    return render(request,'passchange.html',{'form':form})


def change_pass(request):
    if request.method=='POST':
        form=SetPasswordForm(user=request.user,data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,request.user)
            return redirect('profile')
    else:
        form=SetPasswordForm(user=request.user)
    return render(request,'passchange.html',{'form':form})