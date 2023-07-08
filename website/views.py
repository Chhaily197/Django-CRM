from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .form import SignUpForm, AddRecordForm
from .models import Records

# Create your views here.

def test(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def home(request):
    recoards = Records.objects.all()

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
        return render(request, 'home.html', {'records':recoards})


def logout_user(request):
    logout(request)
    messages.success(request, "You have been loggout out...")
    return render(request, 'home.html', {})

def register_user(request):
    if request.method == "POST":
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

    return render(request, 'register.html', {'form':form})


def customer_record(request, pk):
    if request.user.is_authenticated:
        # look Up Records
        customer_record = Records.objects.get(id=pk)
        return render(request, 'records.html', {'customer_record':customer_record})
    else:
        messages.success(request, "You Must Be Logged In The Records")
        return redirect('home')

def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Records.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, 'Records Deleted successfully..')
        return redirect('home')
    else:
        messages.success(request, "You Must Be Logged In...")
        return redirect('home')
    

def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, 'Record added...')
                return redirect('home')
        return render(request, 'add.html', {'form':form})
    else:
        messages.success(request, 'You Must Be Logged In...')
        return redirect('home')

def update_record(request, pk):
    if request.user.is_authenticated:
        currect_record = Records.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=currect_record)
        if form.is_valid():
            form.save()
            messages.success(request, 'Record has been Update...')
            return redirect('home')
        return render(request, 'update.html', {'form':form})
    else:
        messages.success(request, 'You Must Be Logged In...')
        return redirect('home')