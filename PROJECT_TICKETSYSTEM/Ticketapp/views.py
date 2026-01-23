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
    

def pagination(table, reqPage):
    paginator = Paginator(table, 15)
    try:
        tickets = paginator.page(reqPage)
    except PageNotAnInteger:
        tickets = paginator.page(1)
    except EmptyPage:
        tickets = paginator.page(paginator.num_pages)

    return tickets

@login_required
def home(request):
    reqPage = request.GET.get('page')

    if request.method == 'POST' and request.user.is_staff:
        inpAllCases = request.POST['inpallCasesView'] 
        if inpAllCases == 'True':
            request.session['allCasesView'] = True
        else:
            request.session['allCasesView'] = False

    allCasesView = request.session.get('allCasesView', False)
    
 
    if request.user.is_staff and allCasesView:
        tickets = Tickets.objects.exclude(Status = 'C').order_by('-Created_at')
    elif request.user.is_staff and not allCasesView:
        tickets = Tickets.objects.filter(Casemanager_id = request.user.id).order_by('-Created_at')
    else:
        tickets = Tickets.objects.filter(User_id = request.user.id).order_by('-Created_at')
    
    tickets = pagination(tickets, reqPage)
    
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