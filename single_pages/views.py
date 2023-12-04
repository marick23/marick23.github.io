from django.shortcuts import render
from event.models import EVENT
from KLEAGUE.models import KLEAGUE
def index(request):
    events = EVENT.objects.order_by('-created_at')[:3]
    kleagues = KLEAGUE.objects.all()
    return render(
        request,
        'single_pages/index.html',
        {
            'events': events,
            'KLEAGUES':kleagues
        }
    )

def company(request):
    return render(
        request,
        'single_pages/company.html'
    )
