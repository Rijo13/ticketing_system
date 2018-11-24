from django.shortcuts import render
from django.shortcuts import redirect
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.conf import settings
from ticket.models import Ticket
from ticket.forms import TicketForm


def redirect_home(request):
    return redirect(index)

def index(request, category=None):
    if category is not None:
        tickets = Ticket.objects.filter(category=category)
    else:
        tickets = Ticket.objects.all()
        
    data = {
        'categories': settings.CATEGORY_CHOICES,
        'selected_category': category,
        'ticket_count': tickets.count(),
        'tickets': tickets,
    }
    return render(request, 'index.html', context=data)  

def ticket_add(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket_new = form.save()
            ticket_new.save()
            return redirect('index')
    else:
        form = TicketForm()

    context = {
        'form': form,
    }
    return render(request, 'ticket_add.html', context=context)

def ticket_view(request, ticket_id=None):
    data = {}
    if ticket_id:
        # ticket_obj = Ticket.objects.get(id=ticket_id)
        ticket_obj = get_object_or_404(Ticket, id=ticket_id)
        form = TicketForm(request.POST or None, instance=ticket_obj)
        if form.is_valid():
            ticket_updated = form.save()
            ticket_updated.save()
        return render(request, 'ticket_add.html', context={'form': form})
    else:
        raise Http404()
        # return render(request, 'ticket_add.html', context={'form': form}, status=404)

