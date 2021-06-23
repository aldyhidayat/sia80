from django.db import models

# Create your models here.
class JenisAkun(models.Model):
    nama = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.nama
    

class akun(models.Model):
    no = models.IntegerField(null=True)
    nama = models.CharField(max_length=255, null=True)
    jenis = models.ForeignKey(JenisAkun, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return "%s %s" % (self.no, self.nama)
    
    class Meta:
        ordering = ['no']
        