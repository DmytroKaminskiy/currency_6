from time import time

from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django_filters.views import FilterView
from django.urls import reverse, reverse_lazy

from currency.filters import RateFilter
from currency.tasks import send_email_in_background

from currency.models import Rate, ContactUs
from currency.forms import RateForm

from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DetailView,
    DeleteView,
)
from django.conf import settings


# class IndexView(TemplateView):
#     template_name = 'index.html'


class RateListView(FilterView):
    paginate_by = 10
    queryset = Rate.objects.all().order_by('-created').select_related('source')
    filterset_class = RateFilter
    # queryset = Rate.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['pagination_filter'] = "&".join(
            f"{key}={value}"
            for key, value in self.request.GET.items()
            if key != 'page'
        )
        return context


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


class ContactUsCreateView(CreateView):
    model = ContactUs
    template_name = 'contactus_create.html'
    success_url = reverse_lazy('index')
    fields = (
        'name',
        'reply_to',
        'subject',
        'body',
    )

    def form_valid(self, form):
        redirect = super().form_valid(form)
        subject = 'User ContactUs'
        body = f'''
            Request From: {self.object.name}
            Email to reply: {self.object.reply_to}
            Subject: {self.object.subject}

            Body: {self.object.body}
        '''
        send_email_in_background.delay(subject, body)
        # send_email_in_background.apply_async(args=(subject, body))
        '''
        00-8.59 | 9.00-19.00 | 19.01 - 23.59
        9.00    |    send    | 9.00 next day
        '''
        # from datetime import datetime, timedelta
        # eta = datetime(2021, 11, 21, 19, 00, 00)
        # send_email_in_background.apply_async(
        #     kwargs={'subject': subject, 'body': body},
        #     countdown=120,
            # eta=eta,
        # )
        return redirect


'''
User form
name: Dima
reply_to: fenderoksp@gmail.com
subject: Test
body: Test body

SMTP - simple mail transfer protocol

send email to support
recipient: support@fakemail.com
Subject: User ContactUs
Body: Request from: Dima. Email to reply: fenderoksp@gmail.com. Subject: Test, Body: Test Body
'''