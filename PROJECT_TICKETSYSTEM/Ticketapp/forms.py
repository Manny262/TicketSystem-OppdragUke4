from django import forms
from .models import Tickets

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