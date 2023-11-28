from django.shortcuts import render, redirect
from .models import EVENT
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    events = EVENT.objects.all().order_by('-pk')

    paginator = Paginator(events, 4)  # 한 페이지에 9개씩 게시물을 보여줍니다.

    page_number = request.GET.get('page')
    try:
        events = paginator.page(page_number)
    except PageNotAnInteger:
        events = paginator.page(1)
    except EmptyPage:
        events = paginator.page(paginator.num_pages)

    return render(
        request,
        'event/Event.html',
        {
            'events': events
        }
    )

def Event_detail(request, pk):
    events = EVENT.objects.get(pk=pk)

    return render(
        request,
        'event/Event_detail.html',
        {
            'event': events
        }
    )

class EventCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = EVENT
    fields = ['title', 'content', 'head_image']
    template_name = 'event/Event_form.html'

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff
    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated and (current_user.is_staff or current_user.is_superuser):
            form.instance.author = current_user
            return super(EventCreate, self).form_valid(form)
        else:
            return redirect('/event/')

class EventUpdate(LoginRequiredMixin, UpdateView):
    model = EVENT
    fields = ['title', 'content', 'head_image']
    template_name = 'event/Event_update.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(EventUpdate, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied