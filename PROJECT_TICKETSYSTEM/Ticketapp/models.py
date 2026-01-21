from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta, date
# Create your models here.

def get_default_deadline():
    return date.today() + timedelta(days=7)

class Tickets(models.Model):
    Ticket_id = models.BigAutoField(primary_key=True)
    User_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_tickets')
    Title = models.CharField(max_length=150, help_text='Tittel på din henvendelse')
    Description = models.TextField()
    status_choices = {'O': "åpen", 'U': 'under arbeid', 'C': 'lukket'}
    Status = models.CharField(max_length=1, choices=status_choices)
    Created_at = models.DateTimeField(auto_now_add=True)
    Changed_at = models.DateTimeField(auto_now=True)
    Deadline = models.DateField(default=get_default_deadline)
    Casemanager_id = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='Assigned_tickets')