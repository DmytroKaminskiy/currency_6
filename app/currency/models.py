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
    source = models.CharField(max_length=25)

    # to-do, in-progress, done

    # def save(self, *args, **kwargs):
    #     if not self.created:
    #         self.created = datetime.now()
    #     return super().save(*args, **kwargs)


class Source(models.Model):
    name = models.CharField(max_length=64)
