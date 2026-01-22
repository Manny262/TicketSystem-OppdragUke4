from django import forms
from .models import Tickets
from django.contrib.auth.models import User


class newTicketsForm(forms.ModelForm):
    
    class Meta:
        model = Tickets
        fields = ['Title', 'Description', 'Deadline']
        widgets ={ 
            'Deadline': forms.DateInput(attrs={'type': 'date'})
        }
        labels = {
            'Title': 'Tittel',
            'Description': 'Beskrivelse',
            'Deadline': 'Frist',
        }
        
class TicketViewForm(forms.ModelForm):
    class Meta:
        model = Tickets
        fields = ['User_id', 'Title', 'Description', 'Status', 'Deadline', 'Casemanager_id']
        widgets={
            'Deadline': forms.DateInput(attrs={'type': 'date'})
        }
        labels = {
            'User_id': 'Bruker',
            'Title': 'Tittel',
            'Description': 'Beskrivelse',
            'Status': 'Status',
            'Deadline': 'Frist',
            'Casemanager_id': 'Saksbehandler'
        }
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        self.fields['User_id'].disabled = True
        self.fields['Title'].help_text = False
        self.fields['Casemanager_id'].queryset = User.objects.filter(is_staff=True)
        if user and not user.is_staff:
            self.fields['Status'].disabled = True
            self.fields['Casemanager_id'].disabled = True
        else:
            self.fields['Title'].disabled = True
            self.fields['Description'].disabled = True 
            self.fields['Deadline'].disabled = True 