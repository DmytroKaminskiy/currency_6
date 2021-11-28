from django.db import models
from currency import model_choices as mch


class Rate(models.Model):

    buy = models.DecimalField(max_digits=6, decimal_places=2)
    sale = models.DecimalField(max_digits=6, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    type = models.PositiveSmallIntegerField(
        choices=mch.RateTypeChoices.choices,
        # default=1, WRONG
        default=mch.RateTypeChoices.USD,  # correct
    )  # if field contains choices (type), hr = object.get_{field_name}_display() (object.get_type_display())
    source = models.ForeignKey('currency.Source', on_delete=models.CASCADE)

    # to-do, in-progress, done

    # def save(self, *args, **kwargs):
    #     if not self.created:
    #         self.created = datetime.now()
    #     return super().save(*args, **kwargs)


class Source(models.Model):
    '''
    OneToOne - X
    OneToMany - Y
    ManyToMany - X

    N + 1
    '''
    name = models.CharField(max_length=64)
    code_name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name


class ContactUs(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=128)
    reply_to = models.EmailField()
    subject = models.CharField(max_length=128)
    body = models.CharField(max_length=1024)
    raw_content = models.TextField()
