from time import time
from django.core.mail import send_mail
from django.urls import reverse, reverse_lazy

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

    def _send_email(self):
        subject = 'User ContactUs'
        body = f'''
            Request From: {self.object.name}
            Email to reply: {self.object.reply_to}
            Subject: {self.object.subject}

            Body: {self.object.body}
        '''
        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [settings.DEFAULT_FROM_EMAIL],
            fail_silently=False,
        )

    def form_valid(self, form):
        redirect = super().form_valid(form)
        self._send_email()
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