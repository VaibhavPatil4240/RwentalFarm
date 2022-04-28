from dataclasses import field
import email
from pyexpat import model
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Account
from django.contrib.auth.models import AbstractUser
from .models import Account
from django.db import models

class UserRegisterForm(UserCreationForm):
   
    class Meta:
        model=User
        fields=['username','email','password1','password2']





