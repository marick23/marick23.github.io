from django.shortcuts import render
from KLEAGUE.models import Category

# Create your views here.
def grade(request):
    categories = Category.objects.all()
    return render(
        request,
        'mypage/grade.html',
        {
            'categories': categories,
        }
    )
def index(request):
    categories = Category.objects.all()
    return render(
        request,
        'mypage/mypage.html',
        {
            'categories': categories,
        }

    )