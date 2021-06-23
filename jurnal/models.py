from django.db import models
from akun.models import *
# Create your models here.

class jurnal (models.Model):
    kategori = (
        ('Debet', 'Debet'),
        ('Kredit', 'Kredit'),
    )
    akun = models.ForeignKey(akun, null=True, on_delete=models.SET_NULL)
    tanggal = models.DateField(null=True)
    jumlah = models.FloatField(null=True, max_length=20)
    keterangan = models.CharField(null=True, max_length=200)
    kategori = models.CharField(null=True, max_length=20, choices=kategori)

    def __str__(self):
        return "%s %s" % (self.keterangan, self.kategori)
    
