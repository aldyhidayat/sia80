import django_filters

from . models import *

class JurnalFilter(django_filters.FilterSet):
    class Meta:
        model = jurnal
        fields = ['tanggal','akun','keterangan','kategori']


