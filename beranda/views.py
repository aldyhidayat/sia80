from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings
from akun.models import *
from django.db.models import Sum
from jurnal.models import *
# Create your views here.

@login_required(login_url=settings.LOGIN_URL)
def dashboard(request):
    jmlhakun = akun.objects.all().count
    jmlhjurnal = jurnal.objects.all().count
    jmlhjurnaldebet = jurnal.objects.filter(kategori='Debet').count
    jmlhjurnalkredit = jurnal.objects.filter(kategori='Kredit').count
    debets = jurnal.objects.filter(kategori='Debet').aggregate(total=Sum('jumlah'))
    kredits = jurnal.objects.filter(kategori='Kredit').aggregate(total=Sum('jumlah')) 
    
    context = {
        'jmlhakun':jmlhakun,
        'jmlhjurnal':jmlhjurnal,
        'jmlhjurnaldebet':jmlhjurnaldebet,
        'jmlhjurnalkredit':jmlhjurnalkredit,
        'debets':debets,
        'kredits':kredits,
    }

    return render(request, 'beranda/dashboard.html', context)
