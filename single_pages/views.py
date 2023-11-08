from django.shortcuts import render
from event.models import EVENT
def index(request):
    events = EVENT.objects.order_by('-created_at')[:3]
    return render(
        request,
        'single_pages/index.html',
        {
            'events': events
        }
    )

def company(request):
    return render(
        request,
        'single_pages/company.html'
    )
def search(request):
    return render(
        request,
        'single_pages/searchingpage.html'
    )