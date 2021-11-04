import debug_toolbar

from django.views.generic import (
    TemplateView,
)

from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),

    path('__debug__/', include(debug_toolbar.urls)),

    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('currency/', include('currency.urls')),
]
