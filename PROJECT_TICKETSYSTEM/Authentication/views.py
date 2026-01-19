
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User

def scrLogin(request):
    return render(request, 'scrLogin.html')

# def login(request):
#     if request.method == 'POST':
#         Username = request.POST['username']
#         Password = request.POST['password']
        
        
