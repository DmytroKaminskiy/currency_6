from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from account.models import User


@receiver(pre_save, sender=User)
def user_pre_save_email_field(sender, instance, **kwargs):
    print('user_pre_save')
    if instance.email:
        instance.email = instance.email.lower()


@receiver(pre_save, sender=User)
def user_pre_save_phone_field(sender, instance, **kwargs):
    print('USER CLEAN PHONE')
    #
    #
    #
    #
    #
    print('USER CLEAN PHONE')


@receiver(pre_save, sender=User)
def user_pre_save_first_name_field(sender, instance, **kwargs):
    print('USER CLEAN FIRST NAME')
    #
    #
    #
    #
    #
    print('USER CLEAN FIRST NAME')


@receiver(pre_save, sender=User)
def user_pre_save_last_name_field(sender, instance, **kwargs):
    print('USER CLEAN LAST NAME')
    #
    #
    #
    #
    #
    print('USER CLEAN LAST NAME')


@receiver(post_save, sender=User)
def user_post_save(sender, instance, **kwargs):
    print('post_save')
