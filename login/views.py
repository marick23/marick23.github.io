from django.shortcuts import render
# from .models import Member

# Create your views here.

def memberjoin(request):

    return render(
        request,
        'login/memberjoin.html',
    )
def index(request):

    return render(
        request,
        'login/login.html',

    )
