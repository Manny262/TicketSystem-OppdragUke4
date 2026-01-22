from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import newTicketsForm, TicketViewForm
from .models import Tickets
# Create your views here.
def getName (id):
    if id:
        return User.objects.get(id=id).username
@login_required
def home(request):
    tickets = Tickets.objects.filter(User_id = request.user.id)
    allCasesView = False 
    if request.method == 'POST' and request.user.is_staff:
        if request.POST['inpallCasesView'] == 'True':
            tickets = Tickets.objects.exclude(Status = 'C')
            allCasesView = True      
        else:
            tickets = Tickets.objects.filter(Casemanager_id = request.user.id)
            allCasesView = False
    return render(request, 'scrHome.html', {'username': getName(request.user.id), 'tickets': tickets, 'allCasesView': allCasesView})        

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

def TicketView(request, Ticket_id):
    ticket = Tickets.objects.get(Ticket_id = Ticket_id)
    if request.method == 'POST':
        form = TicketViewForm(request.POST, instance=ticket, user=request.user)
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
            messages.success(request, 'Sak oppdatert')
            form = TicketViewForm(instance=ticket, user=request.user)
    else:
        form = TicketViewForm(instance=ticket, user=request.user)
    return render(request, 'scrTicketView.html', {'ticket':ticket, 'form': form})