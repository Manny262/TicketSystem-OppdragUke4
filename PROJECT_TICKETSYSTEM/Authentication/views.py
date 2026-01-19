
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User


def scrLogin(request):
    return render(request, 'scrLogin.html')

def login(request):
    if request.method == 'POST':
        Username = request.POST['username']
        Password = request.POST['password']
        user = authenticate(username=Username, password=Password)    
        if user is None:
            messages.error(request, 'Feil brukernavn eller passord')
        else:
            auth_login(request, user)
            return render(request, 'Home.html')

def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password1  = request.POST['password1']
        password2 = request.POST['password2']

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Dette brukernavnet er allerede i bruk')
        # elif User.objects.filter(email=email).exists():
        #     messages.error(request, 'emailen er i bruk')
        elif password1 != password2:
            messages.error(request, 'Passordene matcher ikke')
        else:
            user = User.objects.create_user(email=email, username=username, password=password1)
            user.save()
            messages.success(request, 'Bruker opprettet! Logg inn.')
            return render(request, 'scrRegister.html', {'redirect_after': True})
    
    return render(request, 'scrRegister.html')