from django.shortcuts import render, redirect
from .models import OOTD
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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

def ootd_list(request):
    query = request.GET.get('q')  # GET 요청으로부터 검색어를 가져옵니다.

    if query:
        # 검색어가 있을 경우, 해당하는 게시물 필터링
        ootds = OOTD.objects.filter(title__icontains=query)  # title에 검색어가 포함된 게시물 필터링

    else:
        # 검색어가 없을 경우, 모든 게시물
        ootds = OOTD.objects.all()

    paginator = Paginator(ootds, 9)  # 한 페이지에 9개씩 게시물을 보여줍니다.

    page_number = request.GET.get('page')
    try:
        ootds = paginator.page(page_number)
    except PageNotAnInteger:
        ootds = paginator.page(1)
    except EmptyPage:
        ootds = paginator.page(paginator.num_pages)

    return render(
        request,

        'OOTD/ootd.html',
        {
            'ootds': ootds
        }
    )

class OOTDCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = OOTD
    fields = ['title', 'content', 'head_image']
    template_name = 'OOTD/OOTD_form.html'

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff
    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated and (current_user.is_staff or current_user.is_superuser):
            form.instance.author = current_user
            return super(OOTDCreate, self).form_valid(form)
        else:
            return redirect('/OOTD/')

class OOTDUpdate(LoginRequiredMixin, UpdateView):
    model = OOTD
    fields = ['title', 'content', 'head_image']
    template_name = 'OOTD/OOTD_update.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(OOTDUpdate, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied