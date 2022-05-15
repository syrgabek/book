
from django.shortcuts import render

from django.views.generic import CreateView,ListView
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from . import forms, models




class RegisterView(CreateView):
    form_class = forms.RegisteForm
    template_name = 'registration.html'
    success_url = '/user/'

class NewLoginView(LoginView):
    form_class = forms.Login
    template_name = 'login.html'
    success_url = '/user/'

class Userllist(LoginView):
    template_name = 'user.html'
    queryset = models.CustomUser.objects.all()


    def get_queryset(self):
        return self
