from django import forms

from ticket.models import Ticket

class TicketForm(forms.ModelForm):

    class Meta:
        model = Ticket
        fields = ('title', 'content', 'author', 'category')
