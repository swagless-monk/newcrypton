from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordResetForm
from django.shortcuts import render, redirect

from .forms import SignUpForm, ChangePassword

# Create your views here.
def home(request):
    return render(request, 'authenticate/home.html', {})

def login_user(request):
    if request.method == 'POST':
        
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, ('Login Success'))
            return redirect('home')
        else:
            messages.error(request, ('Unrecognized Username/Password'))
            return redirect('login')   
    else:
        return render(request, 'authenticate/login.html', {})

@login_required
def logout_user(request):
    logout(request)
    messages.success(request, 'Logout Success')
    return redirect('home')

def user_registration(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ('Registration Success'))
            return redirect('home')
    else:
        form = SignUpForm()

    context = {'form': form}
    return render(request, 'authenticate/register.html', context)

@login_required
def change_password(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        form = ChangePassword(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            login(request, user)
            messages.success(request, ('Password Changed'))
            return redirect('home')
    else:
        form = ChangePassword(user=request.user)
    
    context = {'form': form}
    return render(request, 'authenticate/change_password.html', context)

def reset_password(request):
    form = PasswordResetForm()

    context = {'form': form}
    return render(request, 'authenticate/reset_password.html', context)

def bitcoin(request):
    #this_is_my_view()
    return render(request, 'authenticate/bitcoin.html', {})

