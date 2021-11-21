from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def slow():
    from time import sleep
    sleep(10)


@shared_task(
    autoretry_for=(ConnectionError, ),
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
