from django.shortcuts import render, redirect
from .forms import *
from .models import *
from .filters import *
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from django.conf import settings
from datetime import date
# Create your views here.

@login_required(login_url=settings.LOGIN_URL)
def dashboard(request):
    jurnals = jurnal.objects.all()
    debets = jurnal.objects.filter(kategori='Debet').aggregate(total=Sum('jumlah'))
    kredits = jurnal.objects.filter(kategori='Kredit').aggregate(total=Sum('jumlah')) 
    title = "Jurnal Umum"
    context = {
        'jurnals' : jurnals,
        'title': title,
        'debets':debets,
        'kredits':kredits,
    }
    return render (request,'jurnal/dashboard.html', context,)

@login_required(login_url=settings.LOGIN_URL)
def category(request, akun_id):
    jurnals = jurnal.objects.filter(akun_id=akun_id)
    debets = jurnal.objects.filter(kategori='Debet').filter(akun_id=akun_id).aggregate(total=Sum('jumlah'))
    kredits = jurnal.objects.filter(kategori='Kredit').filter(akun_id=akun_id).aggregate(total=Sum('jumlah')) 
    title = "Jurnal Umum"
    context = {
        'jurnals' : jurnals,
        'title': title,
        'debets':debets,
        'kredits':kredits,
    }
    return render (request,'jurnal/kategori.html', context)

@login_required(login_url=settings.LOGIN_URL)
def category2(request, date):
    jurnals = jurnal.objects.filter(tanggal=date)
    
    debets = jurnal.objects.filter(kategori='Debet').filter(tanggal=date).aggregate(total=Sum('jumlah'))
    kredits = jurnal.objects.filter(kategori='Kredit').filter(tanggal=date).aggregate(total=Sum('jumlah')) 
    title = "Jurnal Umum"
    print (jurnals)
    context = {
        'jurnals' : jurnals,
        'title': title,
        'debets':debets,
        'kredits':kredits,
    }
    return render (request,'jurnal/kategori.html', context)

@login_required(login_url=settings.LOGIN_URL)
def TambahJurnal(request):
    title = "Tambah Jurnal Umum"
    if request.POST:
        form = FormJurnal(request.POST)
        if form.is_valid():
            form.save()

            context = {
                'form':form,
                'title':title,
            }
            return redirect ( 'jurnal:dashboard')
    else:
        form = FormJurnal()
        context = {
            'form':form,
            'title':title,
            }
    return render(request, 'jurnal/add.html', context)

@login_required(login_url=settings.LOGIN_URL)
def HapusJurnal(request, id_jurnal):
    jurnals = jurnal.objects.filter(id=id_jurnal)
    jurnals.delete()

    return redirect('jurnal:dashboard')


@login_required(login_url=settings.LOGIN_URL)
def UbahJurnal(request, id_jurnal):
    jurnals = jurnal.objects.get(id=id_jurnal)
    template = 'jurnal/edit.html'
    if request.POST:
        form = FormJurnal(request.POST, instance=jurnals)
        if form.is_valid():
            form.save()
            return redirect('jurnal:dashboard')
    else:
        form = FormJurnal(instance=jurnals)
        context = {
            'form': form,
            'jurnals': jurnals,
        }
    return render(request, template, context)