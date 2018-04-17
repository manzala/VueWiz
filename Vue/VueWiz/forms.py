from __future__ import unicode_literals
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django.db import models

# Create your models here.

class UserRegistrationForm(forms.Form):
    email= forms.EmailField(

        required = True,
        label = 'Email',
        max_length = 32
	)
    password = forms.CharField(
        required = True,
        label = 'Password',
        max_length = 32,
        widget = forms.PasswordInput()
    )


class uploadForm(forms.Form):
    uploadField = forms.FileField(
        required = True,
    )
class videoForm(forms.Form):
    videoField = forms.FileField(
        required = True,
    )