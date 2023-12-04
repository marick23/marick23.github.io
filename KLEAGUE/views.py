from django.shortcuts import render, redirect, get_object_or_404
from .models import KLEAGUE
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Category

def KLEAGUE_list(request):
    kleagues = KLEAGUE.objects.all().order_by('-pk')
    categories = Category.objects.all()
    query = request.GET.get('q')

    if query:
        # 검색어가 있을 경우, 해당하는 게시물 필터링 (리그 이름으로 필터링)
        kleagues = kleagues.filter(league_name__icontains=query)

    paginator = Paginator(kleagues, 9)
    page_number = request.GET.get('page')

    try:
        kleagues = paginator.page(page_number)
    except PageNotAnInteger:
        kleagues = paginator.page(1)
    except EmptyPage:
        kleagues = paginator.page(paginator.num_pages)

    return render(
        request,
        'KLEAGUE/KLEAGUE_list.html',
        {
            'kleagues': kleagues,
            'categories': categories,
            'search_term': query
        }
    )

def index(request):
    kleagues = KLEAGUE.objects.all().order_by('-pk')
    categories = Category.objects.all()

    paginator = Paginator(kleagues, 9)

    page_number = request.GET.get('page')
    try:
        kleagues = paginator.page(page_number)
    except PageNotAnInteger:
        kleagues = paginator.page(1)
    except EmptyPage:
        kleagues = paginator.page(paginator.num_pages)

    return render(
        request,
        'KLEAGUE/KLEAGUE_list.html',
        {
            'kleagues': kleagues,
            'categories': categories,
        }
    )
def KLEAGUE_detail(request, kleague_id):
    kleague = KLEAGUE.objects.get(id=kleague_id)
    selected_option = request.GET.get('selected_option')  # 옵션 선택 여부를 가져옴
    size_option = request.GET.get('size_option')
    categories = Category.objects.all()

    if selected_option == "no_option":
        # "옵션 없음"을 선택한 경우, 옵션 가격을 0으로 설정
        kleague.option_price = 0
    elif selected_option:
        # 선택한 옵션의 가격을 가져와서 기본 가격에 더함
        # 선택한 옵션이 실제로 DB에 존재하는지 확인하고 처리해야 함
        kleague.option_price = 20000

    # 변경된 값을 저장
    kleague.save()

    # 기본 가격에 옵션 가격을 더하여 total_price 계산
    total_price = kleague.base_price + kleague.option_price

    context = {
        'kleague': kleague,
        'total_price': total_price,
        'size_option' : size_option,
        'selected_option': selected_option,
        'categories': categories,
    }
    return render(request, 'KLEAGUE/KLEAGUE_detail.html', context)

    # return render(
    #     request,
    #     'KLEAGUE/KLEAGUE_detail.html',
    #     {
    #         'categories': categories,
    #     }
    # )

class KLEAGUECreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = KLEAGUE
    fields = ['league_name', 'title', 'base_price', 'option_price', 'cont', 'head_image', 'detail_image1', 'detail_image2', 'size_image']
    template_name = 'KLEAGUE/KLEAGUE_form.html'

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff
    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated and (current_user.is_staff or current_user.is_superuser):
            form.instance.author = current_user
            return super(KLEAGUECreate, self).form_valid(form)
        else:
            return redirect('/KLEAGUE/')

class KLEAGUEUpdate(LoginRequiredMixin, UpdateView):
    model = KLEAGUE
    fields = ['league_name', 'title', 'base_price', 'option_price', 'cont', 'head_image', 'detail_image1', 'detail_image2', 'size_image']
    template_name = 'KLEAGUE/KLEAGUE_update.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(KLEAGUEUpdate, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied


def category_page(request, slug):
    category = Category.objects.get(slug=slug)
    categories = Category.objects.all()
    kleagues = KLEAGUE.objects.filter(category=category).order_by('-pk')

    return render(
        request,
        'KLEAGUE/KLEAGUE_list.html',
        {
            'kleagues': kleagues,
            'categories': categories,
        }
    )

