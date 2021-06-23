from django.urls import path
from .views import *

app_name= 'neraca'
urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('bulan/',tanggal,name='filter'),
]
