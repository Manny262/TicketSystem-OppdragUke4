from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import newTicketsForm, TicketViewForm
from .models import Tickets
# Create your views here.

def getName (id):
    if id:
        return User.objects.get(id=id).username
    

def pagination(request, table):
    paginator = Paginator(table, 15)
    page_numb = request.GET.get('page')
    try:
        page_obj = paginator.page(page_numb)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    return page_obj

@login_required
def home(request):
    tickets = Tickets.objects.filter(User_id = request.user.id)
    allCasesView = False 
    if request.method == 'POST' and request.user.is_staff:
        inpAllCases = request.POST['inpallCasesView'] 
       
        if inpAllCases == 'True':
            tickets = Tickets.objects.exclude(Status = 'C')
            allCasesView = True      
        else:
            tickets = Tickets.objects.filter(Casemanager_id = request.user.id)
            allCasesView = False
    context = {'username': getName(request.user.id), 'tickets': tickets, 'allCasesView': allCasesView}
    return render(request, 'scrHome.html', context)        

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
    context = {'form': form}
    return render(request, 'scrNewticket.html', context)

@login_required 
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
    context = {'ticket':ticket, 'form': form}
    return render(request, 'scrTicketView.html', context )