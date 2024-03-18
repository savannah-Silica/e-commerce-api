from django.shortcuts import render, redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from .forms import UserRegistrationForm,UserLoginForm


def sign_in(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(email=email, password=password)
            if user is not None and user.is_active:
                login(request, user)
                messages.success(request, "You have successfully logged in")
                return redirect('home') # Remember to update here with home page list view
            else:
                messages.error(request, "Invalid username or password")
    else:
        form = UserLoginForm()
    return render(request, 'accounts/login.html', {'form': form}) 

def sign_out(request):
    logout(request)
    messages.success(request, "You have successfully logged out")
    return redirect('login')

def sign_up(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.email=user.email.lower()
            user.save()
            return render(request, 'accounts/signup_success.html', {    
                'user': user
            })
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/signup.html', {'form': form})  