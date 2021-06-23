from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.conf import settings
# Create your views here.
@login_required(login_url=settings.LOGIN_URL)
def dashboard(request):
    akuns = akun.objects.all().order_by('no')

    title = "Daftar Akun"
    context = {
        'akuns' : akuns,
        'title': title,
    }
    return render (request,'akun/dashboard.html', context)

@login_required(login_url=settings.LOGIN_URL)
def tambah_akun(request):
    title = "Tambah Akun"
    if request.POST:
        form = FormAkun(request.POST)
        if form.is_valid():
            form.save()
            form = FormAkun()
            
            context = {
                'form': form,
                'title':title,
            }
            return redirect('akun:dashboard')
    else:       
        form = FormAkun()

        context = {
            'form': form,
            'title':title,
        }
    return render(request, 'akun/add.html', context)

@login_required(login_url=settings.LOGIN_URL)
def hapus_akun(request, id_akun):
    akuns = akun.objects.filter(id=id_akun)
    akuns.delete()
    return redirect('akun:dashboard')

@login_required(login_url=settings.LOGIN_URL)   
def ubah_akun(request, id_akun):
    akuns = akun.objects.get(id=id_akun)
    template = 'akun/edit.html'
    if request.POST:
        form = FormAkun(request.POST, instance=akuns)
        if form.is_valid():
            form.save()
            return redirect('akun:dashboard')
    else:
        form = FormAkun(instance=akuns)
        context = {
            'form': form,
            'akun': akuns,
        }
    return render(request, template, context)