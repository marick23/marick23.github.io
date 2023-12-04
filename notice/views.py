from django.shortcuts import render, redirect
from .models import Notice
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from KLEAGUE.models import Category

def index(request):
    notices = Notice.objects.all().order_by('-pk')
    categories = Category.objects.all()

    paginator = Paginator(notices, 5)  # 한 페이지에 9개씩 게시물을 보여줍니다.

    page_number = request.GET.get('page')
    try:
        notices = paginator.page(page_number)
    except PageNotAnInteger:
        notices = paginator.page(1)
    except EmptyPage:
        notices = paginator.page(paginator.num_pages)

    return render(
        request,
        'notice/notice.html',
        {
            'notices' : notices,
            'categories': categories
        }
    )

def single_notice_page(request, pk):
    notice = Notice.objects.get(pk=pk)
    categories = Category.objects.all()

    return render(
        request,
        'notice/view.html',
        {
            'notice' : notice,
            'categories': categories
        }
    )

class NoticeCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Notice
    fields = ['title', 'content', 'head_image', 'file_upload']
    template_name = 'notice/write.html'

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff
    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated and (current_user.is_staff or current_user.is_superuser):
            form.instance.author = current_user
            return super(NoticeCreate, self).form_valid(form)
        else:
            return redirect('/notice/')

class NoticeUpdate(LoginRequiredMixin, UpdateView):
    model = Notice
    fields = ['title', 'content', 'head_image', 'file_upload']
    template_name = 'notice/edit.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(NoticeUpdate, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied