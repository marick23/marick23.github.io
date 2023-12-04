from django.shortcuts import render
from KFA.models import KFA
from KLEAGUE.models import Category
# Create your views here.

def index(request):
    products = KFA.objects.all()
    categories = Category.objects.all()
    return render(
        request,
        'payment/paymentpage.html',
        {
            'pro' : products,
            'categories': categories,
        }
    )