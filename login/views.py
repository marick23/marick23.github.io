from django.shortcuts import render
from .models import Member

# Create your views here.

def memberjoin(request):
    # members = Member.objects.all()
    return render(
        request,
        'login/memberjoin.html',
        # {
        #     'members': members,
        # }

    )
def index(request):

    return render(
        request,
        'login/login.html',

    )
