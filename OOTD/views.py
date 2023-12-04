from django.shortcuts import render, redirect, get_object_or_404
from .models import OOTD, Comment
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import CommentForm
from KLEAGUE.models import Category


def index(request):
    ootds = OOTD.objects.all().order_by('-pk')
    categories = Category.objects.all()
    return render(
        request,
        'OOTD/OOTD.html',
        {
            'ootds': ootds,
            'categories': categories,
        }
    )

def OOTD_detail(request, pk):
    ootd = OOTD.objects.get(pk=pk)
    ootds = OOTD.objects.exclude(pk=pk).order_by('-created_at')[:3]
    categories = Category.objects.all()

    return render(
        request,
        'OOTD/OOTD_detail.html',
        {
            'ootd': ootd,
            'ootds': ootds,
            'comment_form': CommentForm,
            'categories': categories,
        }
    )


def ootd_list(request):
    categories = Category.objects.all()
    query = request.GET.get('q')  # GET 요청으로부터 검색어를 가져옵니다.

    if query:
        # 검색어가 있을 경우, 해당하는 게시물 필터링
        ootds = OOTD.objects.filter(title__icontains=query)  # title에 검색어가 포함된 게시물 필터링

    else:
        # 검색어가 없을 경우, 모든 게시물
        ootds = OOTD.objects.all()

    paginator = Paginator(ootds, 6)  # 한 페이지에 9개씩 게시물을 보여줍니다.

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
            'ootds': ootds,
            'categories': categories
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

# 댓글 구현
def new_comment(request, pk):
    if request.user.is_authenticated:
        ootd = get_object_or_404(OOTD, pk=pk)

        if request.method == 'POST':
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.ootd = ootd
                comment.author = request.user
                comment.save()

                return redirect('OOTD_detail', pk=ootd.pk)

        comment_form = CommentForm()

        return render(
            request, 'OOTD_detail.html',
            {
                'ootd': ootd,
                'comment_form': comment_form
            }
        )
    else:
        raise PermissionDenied

