from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import newTicketsForm
# Create your views here.
def getName (id):
    if id:
        return User.objects.get(id=id).username
@login_required
def home(request):
    return render(request, 'scrHome.html', {'username': getName(request.user.id)})

@login_required
def Newticket(request):
    if request.method == 'POST':
        form = newTicketsForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.User_id = request.user
            item.save()
            messages.success(request, 'Sak opprettet!')
            form = newTicketsForm()
        else:
            messages.error(request, 'Obs! Noe gikk galt')
    else:
        form = newTicketsForm()
    return render(request, 'scrNewticket.html', {'form': form})