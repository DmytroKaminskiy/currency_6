from currency.views import (
    RateListView,
    RateCreateView,
    RateUpdateView,
    RateDetailsView,
    RateDeleteView,
)

from django.urls import path

app_name = 'currency'


urlpatterns = [
    path('rate/list/', RateListView.as_view(), name='rate-list'),
    path('rate/create/', RateCreateView.as_view(), name='rate-create'),
    path('rate/update/<int:pk>/', RateUpdateView.as_view(), name='rate-update'),
    path('rate/delete/<int:pk>/', RateDeleteView.as_view(), name='rate-delete'),
    path('rate/details/<int:pk>/', RateDetailsView.as_view(), name='rate-details'),
]
