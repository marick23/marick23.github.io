from django.shortcuts import render

# Create your views here.
def grade(request):
    return render(
        request,
        'mypage/grade.html',
    )
def index(request):

    return render(
        request,
        'mypage/mypage.html',

    )