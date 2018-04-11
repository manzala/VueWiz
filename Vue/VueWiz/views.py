from django.shortcuts import render
from django.shortcuts import render

from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django import forms
from django.contrib.auth.forms import UserCreationForm
from models import UserRegistrationForm
from django.http import HttpResponse
from models import upload

# Create your views here.
def index(request):
    return render(request, template_name="index.html", context={"done": True})

def done(request):
    return render(request, template_name="done.html")

def error(request):
    return render(request, template_name="error.html")

def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            print(userObj)
            email = userObj['email']
            password = userObj['password']
            if not (User.objects.filter(email=email).exists()):
                User.objects.create_user(username=email,email=email, password=password)
                user = authenticate(username=email,email=email,  password=password)
                # login(request,user)
                return HttpResponseRedirect('done')
            else:
                return HttpResponseRedirect('error')
                # raise forms.ValidationError('Looks like a username with that email or password already exists')
    return HttpResponseRedirect('/#contact')
    #     form = UserRegistrationForm()
    # return render(request, 'signup.html', {'form': form})

def signin(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            print(userObj)
            email = userObj['email']
            password = userObj['password']

            user = authenticate(username=email,email=email,  password=password)
            if(user):
                login(request, user)
                return render(request, 'upload.html', {'form': form})
        else:
            raise forms.ValidationError('Looks like BAD PASSWORD DUD')
    else:
        form = UserRegistrationForm()
    return render(request, 'signin.html', {'form': form})

def upload(request):
    if request.method == 'POST':
        form = upload(request.POST, request.FILES)
        if form.is_valid():
            instance = upload(request.FILES['file'])
            instance.save()
            upload()
            return HttpResponseRedirect('/done')
    else:
        form = upload()
    return render(request, 'upload.html', {'form': form})

