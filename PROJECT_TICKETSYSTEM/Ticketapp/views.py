from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.
def getName (id):
    if id:
        return User.objects.get(id=id).username
@login_required
def home(request):
    return render(request, 'scrHome.html', {'username': getName(request.user.id)})