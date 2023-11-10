from django.views.generic import ListView, DetailView
from django.shortcuts import render
from .models import KFA

class KFAList(ListView):
    model = KFA
    ordering = '-pk'

class KFADetail(DetailView):
    model = KFA

def KFA_detail(request, kfa_id):
    kfa = KFA.objects.get(id=kfa_id)  # kfa_id에 해당하는 KFA 객체 가져오기
    selected_option = request.GET.get('selected_option')  # 옵션 선택 여부를 가져옴

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
        'selected_option': selected_option,
    }
    return render(request, 'KFA_detail.html', context)





