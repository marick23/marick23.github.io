from django.shortcuts import render
from .models import EVENT

def index(request):
    events = EVENT.objects.all().order_by('-pk')

    return render(
        request,
        'event/Event.html',
        {
            'events': events
        }
    )

def event_detail(request, pk):
    events = EVENT.objects.get(pk=pk)

    return render(
        request,
        'event/Event_detail.html',
        {
            'event': events
        }
    )