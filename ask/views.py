from django.shortcuts import render, redirect, get_object_or_404
from .models import Ask
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from KLEAGUE.models import Category

def index(request):
    asks = Ask.objects.all().order_by('-pk')
    categories = Category.objects.all()

    paginator = Paginator(asks, 5)  # 한 페이지에 5개씩 게시물을 보여줍니다.

    page_number = request.GET.get('page')
    try:
        asks = paginator.page(page_number)
    except PageNotAnInteger:
        asks = paginator.page(1)
    except EmptyPage:
        asks = paginator.page(paginator.num_pages)

    return render(
        request,
        'ask/ask.html',
        {
            'asks': asks,
            'categories': categories
        }
    )

def single_ask_page(request, pk):
    ask = Ask.objects.get(pk=pk)

    return render(
        request,
        'ask/view1.html',
        {
            'ask' : ask,
        }
    )

class AskCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Ask
    fields = ['title', 'content', 'head_image', 'file_upload']
    template_name = 'ask/write1.html'

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff
    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated and (current_user.is_staff or current_user.is_superuser):
            form.instance.author = current_user
            return super(AskCreate, self).form_valid(form)
        else:
            return redirect('/ask/')

class AskUpdate(LoginRequiredMixin, UpdateView):
    model = Ask
    fields = ['title', 'content', 'head_image', 'file_upload']
    template_name = 'ask/edit1.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(AskUpdate, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied
