from django.shortcuts import render
from django.shortcuts import render

from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django import forms
from django.contrib.auth.forms import UserCreationForm
from models import UserRegistrationForm

# Create your views here.
def index(request):
    return render(request, template_name="index.html", context={"done": True})

def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            print(userObj)
            username = userObj['username']
            password = userObj['password']
            if not (User.objects.filter(username=username).exists()):
                User.objects.create_user(username, email=None, password=password)
                user = authenticate(username=username, password=password)
                login(request,user)
                return HttpResponseRedirect('signup')
            else:
                raise forms.ValidationError('Looks like a username with that email or password already exists')
    else:
        form = UserRegistrationForm()
    return render(request, 'signup.html', {'form': form})

