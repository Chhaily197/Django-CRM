from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import SignUpForm

# Create your views here.

def test(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def home(request):
    # Check to use logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        #autheticate
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "You have been loggin in!")
            return redirect('home')
        else:
            messages.success(request, "There was an error loggin in...")
            return redirect('home')
    else:
        return render(request, 'home.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, "You have been loggout out...")
    return render(request, 'home.html', {})

def register_user(request):
    if request.methos == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            
            user = authenticate(username=username,password=password)
            login(request, user)
            messages.success(request, "You Have Successfully Registered")
            return redirect('home')
    else:
        form = SignUpForm()

        return render(request, 'register.html', {'form':form})

