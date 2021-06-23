from django.urls import path
from .views import *

app_name  = 'jurnal'
urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('tambah', TambahJurnal, name='tambah'),
    path('hapus/<int:id_jurnal>', HapusJurnal, name='hapus'),
    path('ubah/<int:id_jurnal>', UbahJurnal, name='ubah'),
    path('kategori/<int:akun_id>', category,name='kategori'),
    path('tanggal/<int:date>', category2,name='kategori2'),
]