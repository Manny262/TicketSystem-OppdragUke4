from django.urls import path
from . import views

urlpatterns=[
    path('home/', views.home, name='home'),
    path('Newticket/', views.Newticket, name='Newticket'),
    path('TicketView/<int:Ticket_id>/', views.TicketView, name='TicketView')
]