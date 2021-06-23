from django.urls import path
from .views import *

app_name = 'beranda'
urlpatterns = [
    path('', dashboard, name='dashboard'),
]
