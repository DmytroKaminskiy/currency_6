from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from currency import model_choices as mch
from currency import consts

import requests

from currency.utils import to_decimal


@shared_task
def parse_privatbank():
    from currency.models import Rate, Source

    code_name = consts.CODE_NAME_PRIVATBANK
    source = Source.objects.filter(code_name=code_name).last()
    if source is None:
        source = Source.objects.create(code_name=code_name, name='PrivatBank')

    response = requests.get(consts.API_PRIVATBANK_URL)
    response.raise_for_status()
    rates = response.json()
    available_currency_types = {
        'USD': mch.RateTypeChoices.USD,
        'EUR': mch.RateTypeChoices.EUR,
    }

    for rate in rates:
        buy = to_decimal(rate['buy'])
        sale = to_decimal(rate['sale'])
        currency_type = rate['ccy']

        # skip rate if our app does not support it
        if currency_type not in available_currency_types:
            continue

        last_rate = Rate.objects \
            .filter(type=available_currency_types[currency_type], source=source) \
            .order_by('-created') \
            .first()

        if last_rate is None or \
                last_rate.buy != buy or \
                last_rate.sale != sale:
            Rate.objects.create(
                buy=buy,
                sale=sale,
                type=available_currency_types[currency_type],
                source=source,
            )


@shared_task(
    autoretry_for=(ConnectionError,),
    retry_kwargs={'max_retries': 5},
)
def send_email_in_background(subject, body):
    send_mail(
        subject,
        body,
        settings.DEFAULT_FROM_EMAIL,
        [settings.DEFAULT_FROM_EMAIL],
        fail_silently=False,
    )
