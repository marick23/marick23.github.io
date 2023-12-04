from django.shortcuts import render
from event.models import EVENT
from KLEAGUE.models import KLEAGUE, Category
def index(request):
    events = EVENT.objects.order_by('-created_at')[:3]
    categories = Category.objects.all()
    kleagues = KLEAGUE.objects.all()

    return render(
        request,
        'single_pages/index.html',
        {
            'events': events,
            'categories': categories,
            'KLEAGUES':kleagues
        }
    )

def company(request):
    categories = Category.objects.all()
    return render(
        request,
        'single_pages/company.html',
        {
            'categories': categories,
        }
    )
