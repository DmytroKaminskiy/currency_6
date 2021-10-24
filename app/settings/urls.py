from currency.views import (
    rate_list, status_code,
    test_template, rate_create,
    request_methods, update_rate,
    delete_rate, rate_details
)

from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),

    path('rate/list/', rate_list),
    path('rate/create/', rate_create),
    path('rate/update/<int:pk>/', update_rate),
    path('rate/delete/<int:pk>/', delete_rate),
    path('rate/details/<int:pk>/', rate_details),
    path('template/', test_template),
    path('cs2/', status_code),
    path('rm/', request_methods),
]
