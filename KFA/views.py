from django.shortcuts import render, redirect
from .models import KFA
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from KLEAGUE.models import Category, KLEAGUE

def index(request):
    kfas = KFA.objects.all().order_by('-pk')
    return render(
        request,
        'KFA/KFA_list.html',
        {
            'kfas': kfas,
        }
    )
def KFA_detail(request, kfa_id):
    kfa = KFA.objects.get(id=kfa_id)
    selected_option = request.GET.get('selected_option')  # 옵션 선택 여부를 가져옴
    size_option = request.GET.get('size_option')

    if selected_option == "no_option":
        # "옵션 없음"을 선택한 경우, 옵션 가격을 0으로 설정
        kfa.option_price = 0
    elif selected_option:
        # 선택한 옵션의 가격을 가져와서 기본 가격에 더함
        # 선택한 옵션이 실제로 DB에 존재하는지 확인하고 처리해야 함
        kfa.option_price = 20000

    # 변경된 값을 저장
    kfa.save()

    # 기본 가격에 옵션 가격을 더하여 total_price 계산
    total_price = kfa.base_price + kfa.option_price

    context = {
        'kfa': kfa,
        'total_price': total_price,
        'size_option' : size_option,
        'selected_option': selected_option,
    }
    return render(request, 'KFA/KFA_detail.html', context)

class KFACreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = KFA
    fields = ['title', 'hook_text', 'base_price', 'option_price', 'cont', 'head_image', 'detail_image1', 'detail_image2', 'size_image']
    template_name = 'KFA/KFA_form.html'

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff
    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated and (current_user.is_staff or current_user.is_superuser):
            form.instance.author = current_user
            return super(KFACreate, self).form_valid(form)
        else:
            return redirect('/KFA/')

class KFAUpdate(LoginRequiredMixin, UpdateView):
    model = KFA
    fields = ['title', 'hook_text', 'base_price', 'option_price', 'cont', 'head_image', 'detail_image1', 'detail_image2', 'size_image']
    template_name = 'KFA/KFA_update.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(KFAUpdate, self).dispatch(request, *args, **kwargs)
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