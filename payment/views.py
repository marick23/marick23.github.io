from django.shortcuts import render

from KFA.models import KFA
# Create your views here.

def index(request):
    products = KFA.objects.all()

    return render(
        request,
        'payment/paymentpage.html',
        {
            'pro' : products,
        }
    )