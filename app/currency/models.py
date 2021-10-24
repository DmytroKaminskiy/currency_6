from django.db import models


class Rate(models.Model):
    buy = models.DecimalField(max_digits=6, decimal_places=2)
    sale = models.DecimalField(max_digits=6, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=3)  # noqa: A003
    source = models.CharField(max_length=25)

    # def save(self, *args, **kwargs):
    #     if not self.created:
    #         self.created = datetime.now()
    #     return super().save(*args, **kwargs)
