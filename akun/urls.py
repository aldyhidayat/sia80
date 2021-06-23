from django.urls import path
from .views import *

app_name = 'akun'
urlpatterns = [
    path('dashboard', dashboard, name='dashboard'),
    path('tambah', tambah_akun, name='tambah'),
    path('hapus/<int:id_akun>', hapus_akun, name='hapus'),
    path('ubah/<int:id_akun>', ubah_akun, name='ubah'),
]
