from currency.views import rate_list, status_code

from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),

    path('rate/list/', rate_list),
    path('cs2/', status_code),
]
