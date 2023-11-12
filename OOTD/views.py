from django.shortcuts import render
from .models import OOTD
from django.views.generic import ListView


def index(request):
    ootds = OOTD.objects.all().order_by('-pk')

    return render(
        request,
        'OOTD/OOTD.html',
        {
            'ootds': ootds
        }
    )

def OOTD_detail(request, pk):
    ootd = OOTD.objects.get(pk=pk)

    return render(
        request,
        'OOTD/OOTD_detail.html',
        {
            'ootd': ootd
        }
    )

