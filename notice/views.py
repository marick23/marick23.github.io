from django.shortcuts import render
from .models import Notice
def index(request):
    notices = Notice.objects.all().order_by('-pk')

    return render(
        request,
        'notice/notice.html',
        {
            'notices' : notices
        }
    )

def single_notice_page(request, pk):
    notice = Notice.objects.get(pk=pk)

    return render(
        request,
        'notice/view.html',
        {
            'notice' : notice,
        }
    )