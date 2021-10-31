# do not import our code here

# TYPE_USD = 1
# TYPE_EUR = 2
#
# TYPE_CHOICES = (
#     (TYPE_USD, 'Dollar'),
#     (TYPE_EUR, 'Euro'),
# )

from django.db import models


class RateTypeChoices(models.IntegerChoices):
    USD = 1, 'Dollar'
    EUR = 2, 'Euro'
