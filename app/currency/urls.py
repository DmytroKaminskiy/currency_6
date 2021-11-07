from currency.views import (
    RateListView,
    RateCreateView,
    RateUpdateView,
    RateDetailsView,
    RateDeleteView,
    ContactUsCreateView,
    ProfileView,
)

from django.urls import path

app_name = 'currency'


urlpatterns = [
    path('rate/list/', RateListView.as_view(), name='rate-list'),
    path('rate/create/', RateCreateView.as_view(), name='rate-create'),
    path('rate/update/<int:pk>/', RateUpdateView.as_view(), name='rate-update'),
    path('rate/delete/<int:pk>/', RateDeleteView.as_view(), name='rate-delete'),
    path('rate/details/<int:pk>/', RateDetailsView.as_view(), name='rate-details'),

    path('profile/', ProfileView.as_view(), name='profile'),

    path('contact-us/create/', ContactUsCreateView.as_view(), name='contactus-create'),
]
