from django.urls import path
from . views import *
app_name ='labarugi'

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('bulan', filterbulan, name='filter'),
]
