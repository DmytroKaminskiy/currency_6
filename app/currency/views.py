from django.urls import reverse, reverse_lazy

from currency.models import Rate
from currency.forms import RateForm

from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DetailView,
    DeleteView,
    TemplateView,
)


# class IndexView(TemplateView):
#     template_name = 'index.html'


class RateListView(ListView):
    queryset = Rate.objects.all()


class RateCreateView(CreateView):
    form_class = RateForm
    success_url = reverse_lazy('currency:rate-list')
    template_name = 'rate_create.html'


class RateUpdateView(UpdateView):
    form_class = RateForm
    model = Rate
    success_url = reverse_lazy('currency:rate-list')
    template_name = 'rate_update.html'


class RateDetailsView(DetailView):
    model = Rate


class RateDeleteView(DeleteView):
    model = Rate
    template_name = 'rate_delete.html'
    success_url = reverse_lazy('currency:rate-list')


# def redirect_example(request):
    # return HttpResponseRedirect('/rate/list/')
    # return HttpResponseRedirect(reverse('rate-list'))
    # return redirect('rate-list')
