from django.shortcuts import render, redirect
from .models import Notice
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
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

class NoticeCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Notice
    fields = ['title', 'content', 'head_image', 'file_upload']
    # template_name = 'notice/edit.html'
    template_name = 'notice/write1.html'

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