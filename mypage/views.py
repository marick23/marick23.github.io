from django.shortcuts import render
from login.models import Member

# Create your views here.
def infor(request):
    members = Member.objects.all()
    return render(
        request,
        'mypage/infor.html',
        {
            'members':members
        }
    )
def index(request):

    return render(
        request,
        'mypage/mypage.html',

    )