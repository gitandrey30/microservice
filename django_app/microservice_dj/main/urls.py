from django.urls import path, include

from .views import get_data, get_auth, get_start_page, get_error

urlpatterns = [
    path('', get_start_page),
    path('auth/', get_auth, name='auth'),
    path('service/', get_data, name='service'),
    path('error/', get_error, name='error'),
]