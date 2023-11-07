from django.shortcuts import render
from .models import Detail

def index(request):
    details = Detail.objects.all().order_by('-pk')

    return render(
        request,
        'product_detail/product_busan_away.html',
        {
            'details': details
        }
    )