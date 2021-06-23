from django.shortcuts import render
from akun.models import akun
from jurnal.models import jurnal
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from django.conf import settings
import datetime
# Create your views here.

@login_required(login_url=settings.LOGIN_URL)
def dashboard(request):
    title = "Neraca"
    print(request.POST)
    akuns = akun.objects.all().order_by('no')
    id1 = jurnal.objects.filter(akun_id=1).filter(kategori="Debet").aggregate(total=Sum('jumlah'))
    id2 = jurnal.objects.filter(akun_id=2).filter(kategori="Debet").aggregate(total=Sum('jumlah'))
    id3 = jurnal.objects.filter(akun_id=3).filter(kategori="Debet").aggregate(total=Sum('jumlah'))
    id4 = jurnal.objects.filter(akun_id=4).filter(kategori="Debet").aggregate(total=Sum('jumlah'))
    id5 = jurnal.objects.filter(akun_id=5).filter(kategori="Debet").aggregate(total=Sum('jumlah'))
    id6 = jurnal.objects.filter(akun_id=6).filter(kategori="Debet").aggregate(total=Sum('jumlah'))
    id11 = jurnal.objects.filter(akun_id=1).filter(kategori="Kredit").aggregate(total=Sum('jumlah'))
    id12 = jurnal.objects.filter(akun_id=2).filter(kategori="Kredit").aggregate(total=Sum('jumlah'))
    id13 = jurnal.objects.filter(akun_id=3).filter(kategori="Kredit").aggregate(total=Sum('jumlah'))
    id14 = jurnal.objects.filter(akun_id=4).filter(kategori="Kredit").aggregate(total=Sum('jumlah'))
    id15 = jurnal.objects.filter(akun_id=5).filter(kategori="Kredit").aggregate(total=Sum('jumlah'))
    id16 = jurnal.objects.filter(akun_id=6).filter(kategori="Kredit").aggregate(total=Sum('jumlah'))
    totaldebet1 = jurnal.objects.filter(kategori="Debet").filter(akun__jenis_id=2).aggregate(total=Sum('jumlah'))
    totalkredit1 = jurnal.objects.filter(kategori="Kredit").filter(akun__jenis_id=2).aggregate(total=Sum('jumlah'))
    id46 = jurnal.objects.filter(akun_id=46).filter(kategori="Debet").aggregate(total=Sum('jumlah'))
    id26 = jurnal.objects.filter(akun_id=46).filter(kategori="Kredit").aggregate(total=Sum('jumlah'))
    id47 = jurnal.objects.filter(akun_id=47).filter(kategori="Debet").aggregate(total=Sum('jumlah'))
    id27 = jurnal.objects.filter(akun_id=47).filter(kategori="Kredit").aggregate(total=Sum('jumlah'))
    id48 = jurnal.objects.filter(akun_id=48).filter(kategori="Debet").aggregate(total=Sum('jumlah'))
    id28 = jurnal.objects.filter(akun_id=48).filter(kategori="Kredit").aggregate(total=Sum('jumlah'))
    id49 = jurnal.objects.filter(akun_id=49).filter(kategori="Debet").aggregate(total=Sum('jumlah'))
    id29 = jurnal.objects.filter(akun_id=49).filter(kategori="Kredit").aggregate(total=Sum('jumlah'))
    totaldebet2 = jurnal.objects.filter(kategori="Debet").filter(akun__jenis_id=3).aggregate(total=Sum('jumlah'))
    totalkredit2 = jurnal.objects.filter(kategori="Kredit").filter(akun__jenis_id=3).aggregate(total=Sum('jumlah'))
    totaldebet3 = jurnal.objects.filter(kategori="Debet").filter(akun__jenis_id__in=[2,3]).aggregate(total=Sum('jumlah'))
    totalkredit3 = jurnal.objects.filter(kategori="Kredit").filter(akun__jenis_id__in=[2,3]).aggregate(total=Sum('jumlah'))
    totaldebet4 = jurnal.objects.filter(kategori="Debet").filter(akun__jenis_id=4).aggregate(total=Sum('jumlah'))
    totalkredit4 = jurnal.objects.filter(kategori="Kredit").filter(akun__jenis_id=4).aggregate(total=Sum('jumlah'))
    totaldebet5 = jurnal.objects.filter(kategori="Debet").filter(akun__jenis_id__in=[2,3,4]).aggregate(total=Sum('jumlah'))
    totalkredit5 = jurnal.objects.filter(kategori="Kredit").filter(akun__jenis_id__in=[2,3,4]).aggregate(total=Sum('jumlah'))
    totaldebet6 = jurnal.objects.filter(kategori="Debet").filter(akun__jenis_id=11).aggregate(total=Sum('jumlah'))
    totalkredit6 = jurnal.objects.filter(kategori="Kredit").filter(akun__jenis_id=11).aggregate(total=Sum('jumlah'))
    totaldebet7 = jurnal.objects.filter(kategori="Debet").filter(akun__jenis_id=12).aggregate(total=Sum('jumlah'))
    totalkredit7 = jurnal.objects.filter(kategori="Kredit").filter(akun__jenis_id=12).aggregate(total=Sum('jumlah'))
    totaldebet8 = jurnal.objects.filter(kategori="Debet").filter(akun__jenis_id=13).aggregate(total=Sum('jumlah'))
    totalkredit8 = jurnal.objects.filter(kategori="Kredit").filter(akun__jenis_id=13).aggregate(total=Sum('jumlah'))
    totaldebet9 = jurnal.objects.filter(kategori="Debet").filter(akun__jenis_id=15).aggregate(total=Sum('jumlah'))
    totalkredit9 = jurnal.objects.filter(kategori="Kredit").filter(akun__jenis_id=15).aggregate(total=Sum('jumlah'))
    totaldebet10 = jurnal.objects.filter(kategori="Debet").filter(akun__jenis_id__in=[11,12,13,14,15]).aggregate(total=Sum('jumlah'))
    totalkredit10 = jurnal.objects.filter(kategori="Kredit").filter(akun__jenis_id__in=[11,12,13,14,15]).aggregate(total=Sum('jumlah'))
    id51 = jurnal.objects.filter(akun_id=51).filter(kategori="Debet").aggregate(total=Sum('jumlah'))
    id52 = jurnal.objects.filter(akun_id=51).filter(kategori="Kredit").aggregate(total=Sum('jumlah'))
    id53 = jurnal.objects.filter(akun_id=52).filter(kategori="Debet").aggregate(total=Sum('jumlah'))
    id54 = jurnal.objects.filter(akun_id=52).filter(kategori="Kredit").aggregate(total=Sum('jumlah'))
    id55 = jurnal.objects.filter(akun_id=53).filter(kategori="Debet").aggregate(total=Sum('jumlah'))
    id56 = jurnal.objects.filter(akun_id=53).filter(kategori="Kredit").aggregate(total=Sum('jumlah'))
    id57 = jurnal.objects.filter(akun_id=54).filter(kategori="Debet").aggregate(total=Sum('jumlah'))
    id58 = jurnal.objects.filter(akun_id=54).filter(kategori="Kredit").aggregate(total=Sum('jumlah'))
    id59 = jurnal.objects.filter(akun_id=55).filter(kategori="Debet").aggregate(total=Sum('jumlah'))
    id60 = jurnal.objects.filter(akun_id=55).filter(kategori="Kredit").aggregate(total=Sum('jumlah'))
    id61 = jurnal.objects.filter(akun_id=56).filter(kategori="Debet").aggregate(total=Sum('jumlah'))
    id62 = jurnal.objects.filter(akun_id=56).filter(kategori="Kredit").aggregate(total=Sum('jumlah'))
    id63 = jurnal.objects.filter(akun_id=74).filter(kategori="Debet").aggregate(total=Sum('jumlah'))
    id64 = jurnal.objects.filter(akun_id=74).filter(kategori="Kredit").aggregate(total=Sum('jumlah'))
    id65 = jurnal.objects.filter(akun_id=75).filter(kategori="Debet").aggregate(total=Sum('jumlah'))
    id66 = jurnal.objects.filter(akun_id=75).filter(kategori="Kredit").aggregate(total=Sum('jumlah'))
    id67 = jurnal.objects.filter(akun_id=76).filter(kategori="Debet").aggregate(total=Sum('jumlah'))
    id68 = jurnal.objects.filter(akun_id=76).filter(kategori="Kredit").aggregate(total=Sum('jumlah'))
    id69 = jurnal.objects.filter(akun_id=84).filter(kategori="Debet").aggregate(total=Sum('jumlah'))
    id70 = jurnal.objects.filter(akun_id=84).filter(kategori="Kredit").aggregate(total=Sum('jumlah'))   
    id71 = jurnal.objects.filter(akun_id=85).filter(kategori="Debet").aggregate(total=Sum('jumlah'))
    id72 = jurnal.objects.filter(akun_id=85).filter(kategori="Kredit").aggregate(total=Sum('jumlah'))
    id73 = jurnal.objects.filter(akun_id=86).filter(kategori="Debet").aggregate(total=Sum('jumlah'))
    id74 = jurnal.objects.filter(akun_id=86).filter(kategori="Kredit").aggregate(total=Sum('jumlah'))   
    id75 = jurnal.objects.filter(akun_id=87).filter(kategori="Debet").aggregate(total=Sum('jumlah'))
    id76 = jurnal.objects.filter(akun_id=87).filter(kategori="Kredit").aggregate(total=Sum('jumlah')) 
    id77 = jurnal.objects.filter(akun_id=88).filter(kategori="Debet").aggregate(total=Sum('jumlah'))
    id78 = jurnal.objects.filter(akun_id=88).filter(kategori="Kredit").aggregate(total=Sum('jumlah'))
    id79 = jurnal.objects.filter(akun_id=90).filter(kategori="Debet").aggregate(total=Sum('jumlah'))
    id80 = jurnal.objects.filter(akun_id=90).filter(kategori="Kredit").aggregate(total=Sum('jumlah'))   
    id81 = jurnal.objects.filter(akun_id=91).filter(kategori="Debet").aggregate(total=Sum('jumlah'))
    id82 = jurnal.objects.filter(akun_id=91).filter(kategori="Kredit").aggregate(total=Sum('jumlah')) 
    id83 = jurnal.objects.filter(akun_id=92).filter(kategori="Debet").aggregate(total=Sum('jumlah'))
    id84 = jurnal.objects.filter(akun_id=92).filter(kategori="Kredit").aggregate(total=Sum('jumlah'))
    id85 = jurnal.objects.filter(akun_id=94).filter(kategori="Debet").aggregate(total=Sum('jumlah'))
    id86 = jurnal.objects.filter(akun_id=94).filter(kategori="Kredit").aggregate(total=Sum('jumlah'))
    id87 = jurnal.objects.filter(akun_id=95).filter(kategori="Debet").aggregate(total=Sum('jumlah'))
    id88 = jurnal.objects.filter(akun_id=95).filter(kategori="Kredit").aggregate(total=Sum('jumlah'))
    id89 = jurnal.objects.filter(akun_id=97).filter(kategori="Debet").aggregate(total=Sum('jumlah'))
    id90 = jurnal.objects.filter(akun_id=97).filter(kategori="Kredit").aggregate(total=Sum('jumlah'))
    id91 = jurnal.objects.filter(akun_id=98).filter(kategori="Debet").aggregate(total=Sum('jumlah'))
    id92 = jurnal.objects.filter(akun_id=98).filter(kategori="Kredit").aggregate(total=Sum('jumlah'))
    id93 = jurnal.objects.filter(akun_id=99).filter(kategori="Debet").aggregate(total=Sum('jumlah'))
    id94 = jurnal.objects.filter(akun_id=99).filter(kategori="Kredit").aggregate(total=Sum('jumlah'))
    
    mydate= datetime.datetime.now()
    context = {
        'title':title,
        'akuns':akuns,
        'id1':id1,
        'id2':id2,
        'id3':id3,
        'id4':id4,
        'id5':id5,
        'id6':id6,
        'id11':id11,
        'id12':id12,
        'id13':id13,
        'id14':id14,
        'id15':id15,
        'id16':id16,
        'id46':id46,
        'id26':id26,
        'id47':id47,
        'id27':id27,
        'id48':id48,
        'id28':id28,
        'id49':id49,
        'id29':id29,
        'totaldebet1':totaldebet1,
        'totalkredit1':totalkredit1,
        'totaldebet2':totaldebet2,
        'totalkredit2':totalkredit2,
        'totaldebet3':totaldebet3,
        'totalkredit3':totalkredit3,
        'totaldebet4':totaldebet4,
        'totalkredit4':totalkredit4,
        'totaldebet5':totaldebet5,
        'totalkredit5':totalkredit5,
        'totaldebet6':totaldebet6,
        'totalkredit6':totalkredit6,
        'totaldebet7':totaldebet7,
        'totalkredit7':totalkredit7,
        'totaldebet8':totaldebet8,
        'totalkredit8':totalkredit8,
        'totaldebet9':totaldebet9,
        'totalkredit9':totalkredit9,
        'totaldebet10':totaldebet10,
        'totalkredit10':totalkredit10,
        'id51':id51,
        'id52':id52,
        'id53':id53,
        'id54':id54,
        'id55':id55,
        'id56':id56,
        'id57':id57,
        'id58':id58,
        'id59':id59,
        'id60':id60,
        'id61':id61,
        'id62':id62,
        'id63':id63,
        'id64':id64,
        'id65':id65,
        'id66':id66,
        'id67':id67,
        'id68':id68,
        'id69':id69,
        'id70':id70,
        'id71':id71,
        'id72':id72,
        'id73':id73,
        'id74':id74,
        'id75':id75,
        'id76':id76,
        'id77':id77,
        'id78':id78,
        'id79':id79,
        'id80':id80,
        'id81':id81,
        'id82':id82,
        'id83':id83,
        'id84':id84,
        'id85':id85,
        'id86':id86,
        'id87':id87,
        'id88':id88,
        'id89':id89,
        'id90':id90,
        'id91':id91,
        'id92':id92,
        'id93':id93,
        'id94':id94,
        'mydate':mydate,
    }
    
    return render(request, 'neraca/dashboard.html', context)

@login_required(login_url=settings.LOGIN_URL)
def tanggal(request):
    month=request.POST.get('bulan')
    year=request.POST.get('tahun')
    if not month:
        month = "1"
    if not year:
        year = "12"
    print(request.POST)
    title = "Neraca"
    akuns = akun.objects.all().order_by('no')
    id1 = jurnal.objects.filter(akun_id=1).filter(kategori="Debet").filter(tanggal__month__gte=month).filter(tanggal__month__lte=year).aggregate(total=Sum('jumlah'))
    id2 = jurnal.objects.filter(akun_id=2).filter(kategori="Debet").filter(tanggal__month__gte=month).filter(tanggal__month__lte=year).aggregate(total=Sum('jumlah'))
    id3 = jurnal.objects.filter(akun_id=3).filter(kategori="Debet").filter(tanggal__month__gte=month).filter(tanggal__month__lte=year).aggregate(total=Sum('jumlah'))
    id4 = jurnal.objects.filter(akun_id=4).filter(kategori="Debet").filter(tanggal__month__gte=month).filter(tanggal__month__lte=year).aggregate(total=Sum('jumlah'))
    id5 = jurnal.objects.filter(akun_id=5).filter(kategori="Debet").filter(tanggal__month__gte=month).filter(tanggal__month__lte=year).aggregate(total=Sum('jumlah'))
    id6 = jurnal.objects.filter(akun_id=6).filter(kategori="Debet").filter(tanggal__month__gte=month).filter(tanggal__month__lte=year).aggregate(total=Sum('jumlah'))
    id11 = jurnal.objects.filter(akun_id=1).filter(kategori="Kredit").filter(tanggal__month__gte=month).filter(tanggal__month__lte=year).aggregate(total=Sum('jumlah'))
    id12 = jurnal.objects.filter(akun_id=2).filter(kategori="Kredit").filter(tanggal__month__gte=month).filter(tanggal__month__lte=year).aggregate(total=Sum('jumlah'))
    id13 = jurnal.objects.filter(akun_id=3).filter(kategori="Kredit").filter(tanggal__month__gte=month).filter(tanggal__month__lte=year).aggregate(total=Sum('jumlah'))
    id14 = jurnal.objects.filter(akun_id=4).filter(kategori="Kredit").filter(tanggal__month__gte=month).filter(tanggal__month__lte=year).aggregate(total=Sum('jumlah'))
    id15 = jurnal.objects.filter(akun_id=5).filter(kategori="Kredit").filter(tanggal__month__gte=month).filter(tanggal__month__lte=year).aggregate(total=Sum('jumlah'))
    id16 = jurnal.objects.filter(akun_id=6).filter(kategori="Kredit").filter(tanggal__month__gte=month).filter(tanggal__month__lte=year).aggregate(total=Sum('jumlah'))
    totaldebet1 = jurnal.objects.filter(kategori="Debet").filter(akun__jenis_id=2).filter(tanggal__month__gte=month).filter(tanggal__month__lte=year).aggregate(total=Sum('jumlah'))
    totalkredit1 = jurnal.objects.filter(kategori="Kredit").filter(akun__jenis_id=2).filter(tanggal__month__gte=month).filter(tanggal__month__lte=year).aggregate(total=Sum('jumlah'))
    id46 = jurnal.objects.filter(akun_id=46).filter(kategori="Debet").filter(tanggal__month__gte=month).filter(tanggal__month__lte=year).aggregate(total=Sum('jumlah'))
    id26 = jurnal.objects.filter(akun_id=46).filter(kategori="Kredit").filter(tanggal__month__gte=month).filter(tanggal__month__lte=year).aggregate(total=Sum('jumlah'))
    id47 = jurnal.objects.filter(akun_id=47).filter(kategori="Debet").filter(tanggal__month__gte=month).filter(tanggal__month__lte=year).aggregate(total=Sum('jumlah'))
    id27 = jurnal.objects.filter(akun_id=47).filter(kategori="Kredit").filter(tanggal__month__gte=month).filter(tanggal__month__lte=year).aggregate(total=Sum('jumlah'))
    id48 = jurnal.objects.filter(akun_id=48).filter(kategori="Debet").filter(tanggal__month__gte=month).filter(tanggal__month__lte=year).aggregate(total=Sum('jumlah'))
    id28 = jurnal.objects.filter(akun_id=48).filter(kategori="Kredit").filter(tanggal__month__gte=month).filter(tanggal__month__lte=year).aggregate(total=Sum('jumlah'))
    id49 = jurnal.objects.filter(akun_id=49).filter(kategori="Debet").filter(tanggal__month__gte=month).filter(tanggal__month__lte=year).aggregate(total=Sum('jumlah'))
    id29 = jurnal.objects.filter(akun_id=49).filter(kategori="Kredit").filter(tanggal__month__gte=month).filter(tanggal__month__lte=year).aggregate(total=Sum('jumlah'))
    totaldebet2 = jurnal.objects.filter(kategori="Debet").filter(tanggal__month__gte=month).filter(tanggal__month__lte=year).filter(akun__jenis_id=3).aggregate(total=Sum('jumlah'))
    totalkredit2 = jurnal.objects.filter(kategori="Kredit").filter(tanggal__month__gte=month).filter(tanggal__month__lte=year).filter(akun__jenis_id=3).aggregate(total=Sum('jumlah'))
    totaldebet3 = jurnal.objects.filter(kategori="Debet").filter(tanggal__month__gte=month).filter(tanggal__month__lte=year).filter(akun__jenis_id__in=[2,3]).aggregate(total=Sum('jumlah'))
    totalkredit3 = jurnal.objects.filter(kategori="Kredit").filter(tanggal__month__gte=month).filter(tanggal__month__lte=year).filter(akun__jenis_id__in=[2,3]).aggregate(total=Sum('jumlah'))
    totaldebet4 = jurnal.objects.filter(kategori="Debet").filter(tanggal__month__gte=month).filter(tanggal__month__lte=year).filter(akun__jenis_id=4).aggregate(total=Sum('jumlah'))
    totalkredit4 = jurnal.objects.filter(kategori="Kredit").filter(tanggal__month__gte=month).filter(tanggal__month__lte=year).filter(akun__jenis_id=4).aggregate(total=Sum('jumlah'))
    totaldebet5 = jurnal.objects.filter(kategori="Debet").filter(tanggal__month__gte=month).filter(tanggal__month__lte=year).filter(akun__jenis_id__in=[2,3,4]).aggregate(total=Sum('jumlah'))
    totalkredit5 = jurnal.objects.filter(kategori="Kredit").filter(tanggal__month__gte=month).filter(tanggal__month__lte=year).filter(akun__jenis_id__in=[2,3,4]).aggregate(total=Sum('jumlah'))
    totaldebet6 = jurnal.objects.filter(kategori="Debet").filter(tanggal__month__gte=month).filter(tanggal__month__lte=year).filter(akun__jenis_id=11).aggregate(total=Sum('jumlah'))
    totalkredit6 = jurnal.objects.filter(kategori="Kredit").filter(tanggal__month__gte=month).filter(tanggal__month__lte=year).filter(akun__jenis_id=11).aggregate(total=Sum('jumlah'))
    totaldebet7 = jurnal.objects.filter(kategori="Debet").filter(tanggal__month__gte=month).filter(tanggal__month__lte=year).filter(akun__jenis_id=12).aggregate(total=Sum('jumlah'))
    totalkredit7 = jurnal.objects.filter(kategori="Kredit").filter(tanggal__month__gte=month).filter(tanggal__month__lte=year).filter(akun__jenis_id=12).aggregate(total=Sum('jumlah'))
    totaldebet8 = jurnal.objects.filter(kategori="Debet").filter(tanggal__month__gte=month).filter(tanggal__month__lte=year).filter(akun__jenis_id=13).aggregate(total=Sum('jumlah'))
    totalkredit8 = jurnal.objects.filter(kategori="Kredit").filter(tanggal__month__gte=month).filter(tanggal__month__lte=year).filter(akun__jenis_id=13).aggregate(total=Sum('jumlah'))
    totaldebet9 = jurnal.objects.filter(kategori="Debet").filter(tanggal__month__gte=month).filter(tanggal__month__lte=year).filter(akun__jenis_id=15).aggregate(total=Sum('jumlah'))
    totalkredit9 = jurnal.objects.filter(kategori="Kredit").filter(tanggal__month__gte=month).filter(tanggal__month__lte=year).filter(akun__jenis_id=15).aggregate(total=Sum('jumlah'))
    totaldebet10 = jurnal.objects.filter(kategori="Debet").filter(tanggal__month__gte=month).filter(tanggal__month__lte=year).filter(akun__jenis_id__in=[11,12,13,14,15]).aggregate(total=Sum('jumlah'))
    totalkredit10 = jurnal.objects.filter(kategori="Kredit").filter(tanggal__month__gte=month).filter(tanggal__month__lte=year).filter(akun__jenis_id__in=[11,12,13,14,15]).aggregate(total=Sum('jumlah'))
    id51 = jurnal.objects.filter(akun_id=51).filter(kategori="Debet").filter(tanggal__month__gte=month).filter(tanggal__month__lte=year).aggregate(total=Sum('jumlah'))
    id52 = jurnal.objects.filter(akun_id=51).filter(kategori="Kredit").filter(tanggal__month__gte=month).filter(tanggal__month__lte=year).aggregate(total=Sum('jumlah'))
    id53 = jurnal.objects.filter(akun_id=52).filter(kategori="Debet").filter(tanggal__month__gte=month).filter(tanggal__month__lte=year).aggregate(total=Sum('jumlah'))
    id54 = jurnal.objects.filter(akun_id=52).filter(kategori="Kredit").filter(tanggal__month__gte=month).filter(tanggal__month__lte=year).aggregate(total=Sum('jumlah'))
    id55 = jurnal.objects.filter(akun_id=53).filter(kategori="Debet").filter(tanggal__month__gte=month).filter(tanggal__month__lte=year).aggregate(total=Sum('jumlah'))
    id56 = jurnal.objects.filter(akun_id=53).filter(kategori="Kredit").filter(tanggal__month__gte=month).filter(tanggal__month__lte=year).aggregate(total=Sum('jumlah'))
    id57 = jurnal.objects.filter(akun_id=54).filter(kategori="Debet").filter(tanggal__month__gte=month).filter(tanggal__month__lte=year).aggregate(total=Sum('jumlah'))
    id58 = jurnal.objects.filter(akun_id=54).filter(kategori="Kredit").filter(tanggal__month__gte=month).filter(tanggal__month__lte=year).aggregate(total=Sum('jumlah'))
    id59 = jurnal.objects.filter(akun_id=55).filter(kategori="Debet").filter(tanggal__month__gte=month).filter(tanggal__month__lte=year).aggregate(total=Sum('jumlah'))
    id60 = jurnal.objects.filter(akun_id=55).filter(kategori="Kredit").filter(tanggal__month__gte=month).filter(tanggal__month__lte=year).aggregate(total=Sum('jumlah'))
    id61 = jurnal.objects.filter(akun_id=56).filter(kategori="Debet").filter(tanggal__month__gte=month).filter(tanggal__month__lte=year).aggregate(total=Sum('jumlah'))
    id62 = jurnal.objects.filter(akun_id=56).filter(kategori="Kredit").filter(tanggal__month__gte=month).filter(tanggal__month__lte=year).aggregate(total=Sum('jumlah'))
    id63 = jurnal.objects.filter(akun_id=74).filter(kategori="Debet").filter(tanggal__month__gte=month).filter(tanggal__month__lte=year).aggregate(total=Sum('jumlah'))
    id64 = jurnal.objects.filter(akun_id=74).filter(kategori="Kredit").filter(tanggal__month__gte=month).filter(tanggal__month__lte=year).aggregate(total=Sum('jumlah'))
    id65 = jurnal.objects.filter(akun_id=75).filter(kategori="Debet").filter(tanggal__month__gte=month).filter(tanggal__month__lte=year).aggregate(total=Sum('jumlah'))
    id66 = jurnal.objects.filter(akun_id=75).filter(kategori="Kredit").filter(tanggal__month__gte=month).filter(tanggal__month__lte=year).aggregate(total=Sum('jumlah'))
    id67 = jurnal.objects.filter(akun_id=76).filter(kategori="Debet").filter(tanggal__month__gte=month).filter(tanggal__month__lte=year).aggregate(total=Sum('jumlah'))
    id68 = jurnal.objects.filter(akun_id=76).filter(kategori="Kredit").filter(tanggal__month__gte=month).filter(tanggal__month__lte=year).aggregate(total=Sum('jumlah'))
    id69 = jurnal.objects.filter(akun_id=84).filter(kategori="Debet").filter(tanggal__month__gte=month).filter(tanggal__month__lte=year).aggregate(total=Sum('jumlah'))
    id70 = jurnal.objects.filter(akun_id=84).filter(kategori="Kredit").filter(tanggal__month__gte=month).filter(tanggal__month__lte=year).aggregate(total=Sum('jumlah'))   
    id71 = jurnal.objects.filter(akun_id=85).filter(kategori="Debet").filter(tanggal__month__gte=month).filter(tanggal__month__lte=year).aggregate(total=Sum('jumlah'))
    id72 = jurnal.objects.filter(akun_id=85).filter(kategori="Kredit").filter(tanggal__month__gte=month).filter(tanggal__month__lte=year).aggregate(total=Sum('jumlah'))
    id73 = jurnal.objects.filter(akun_id=86).filter(kategori="Debet").filter(tanggal__month__gte=month).filter(tanggal__month__lte=year).aggregate(total=Sum('jumlah'))
    id74 = jurnal.objects.filter(akun_id=86).filter(kategori="Kredit").filter(tanggal__month__gte=month).filter(tanggal__month__lte=year).aggregate(total=Sum('jumlah'))   
    id75 = jurnal.objects.filter(akun_id=87).filter(kategori="Debet").filter(tanggal__month__gte=month).filter(tanggal__month__lte=year).aggregate(total=Sum('jumlah'))
    id76 = jurnal.objects.filter(akun_id=87).filter(kategori="Kredit").filter(tanggal__month__gte=month).filter(tanggal__month__lte=year).aggregate(total=Sum('jumlah')) 
    id77 = jurnal.objects.filter(akun_id=88).filter(kategori="Debet").filter(tanggal__month__gte=month).filter(tanggal__month__lte=year).aggregate(total=Sum('jumlah'))
    id78 = jurnal.objects.filter(akun_id=88).filter(kategori="Kredit").filter(tanggal__month__gte=month).filter(tanggal__month__lte=year).aggregate(total=Sum('jumlah'))
    id79 = jurnal.objects.filter(akun_id=90).filter(kategori="Debet").filter(tanggal__month__gte=month).filter(tanggal__month__lte=year).aggregate(total=Sum('jumlah'))
    id80 = jurnal.objects.filter(akun_id=90).filter(kategori="Kredit").filter(tanggal__month__gte=month).filter(tanggal__month__lte=year).aggregate(total=Sum('jumlah'))   
    id81 = jurnal.objects.filter(akun_id=91).filter(kategori="Debet").filter(tanggal__month__gte=month).filter(tanggal__month__lte=year).aggregate(total=Sum('jumlah'))
    id82 = jurnal.objects.filter(akun_id=91).filter(kategori="Kredit").filter(tanggal__month__gte=month).filter(tanggal__month__lte=year).aggregate(total=Sum('jumlah')) 
    id83 = jurnal.objects.filter(akun_id=92).filter(kategori="Debet").filter(tanggal__month__gte=month).filter(tanggal__month__lte=year).aggregate(total=Sum('jumlah'))
    id84 = jurnal.objects.filter(akun_id=92).filter(kategori="Kredit").filter(tanggal__month__gte=month).filter(tanggal__month__lte=year).aggregate(total=Sum('jumlah'))
    id85 = jurnal.objects.filter(akun_id=94).filter(kategori="Debet").filter(tanggal__month__gte=month).filter(tanggal__month__lte=year).aggregate(total=Sum('jumlah'))
    id86 = jurnal.objects.filter(akun_id=94).filter(kategori="Kredit").filter(tanggal__month__gte=month).filter(tanggal__month__lte=year).aggregate(total=Sum('jumlah'))
    id87 = jurnal.objects.filter(akun_id=95).filter(kategori="Debet").filter(tanggal__month__gte=month).filter(tanggal__month__lte=year).aggregate(total=Sum('jumlah'))
    id88 = jurnal.objects.filter(akun_id=95).filter(kategori="Kredit").filter(tanggal__month__gte=month).filter(tanggal__month__lte=year).aggregate(total=Sum('jumlah'))
    id89 = jurnal.objects.filter(akun_id=97).filter(kategori="Debet").filter(tanggal__month__gte=month).filter(tanggal__month__lte=year).aggregate(total=Sum('jumlah'))
    id90 = jurnal.objects.filter(akun_id=97).filter(kategori="Kredit").filter(tanggal__month__gte=month).filter(tanggal__month__lte=year).aggregate(total=Sum('jumlah'))
    id91 = jurnal.objects.filter(akun_id=98).filter(kategori="Debet").filter(tanggal__month__gte=month).filter(tanggal__month__lte=year).aggregate(total=Sum('jumlah'))
    id92 = jurnal.objects.filter(akun_id=98).filter(kategori="Kredit").filter(tanggal__month__gte=month).filter(tanggal__month__lte=year).aggregate(total=Sum('jumlah'))
    id93 = jurnal.objects.filter(akun_id=99).filter(kategori="Debet").filter(tanggal__month__gte=month).filter(tanggal__month__lte=year).aggregate(total=Sum('jumlah'))
    id94 = jurnal.objects.filter(akun_id=99).filter(kategori="Kredit").filter(tanggal__month__gte=month).filter(tanggal__month__lte=year).aggregate(total=Sum('jumlah'))
    id95 = jurnal.objects.filter(kategori="Debet").filter(akun_id__in=[51,52,53]).filter(tanggal__month__gte=month).filter(tanggal__month__lte=year).aggregate(total=Sum('jumlah'))
    id96 = jurnal.objects.filter(kategori="Kredit").filter(akun_id__in=[51,52,53]).filter(tanggal__month__gte=month).filter(tanggal__month__lte=year).aggregate(total=Sum('jumlah'))
    id97 = jurnal.objects.filter(kategori="Debet").filter(akun_id__in=[54,55]).filter(tanggal__month__gte=month).filter(tanggal__month__lte=year).aggregate(total=Sum('jumlah'))
    id98 = jurnal.objects.filter(kategori="Kredit").filter(akun_id__in=[54,55]).filter(tanggal__month__gte=month).filter(tanggal__month__lte=year).aggregate(total=Sum('jumlah'))
    id99 = jurnal.objects.filter(kategori="Debet").filter(akun_id__in=[56,74]).filter(tanggal__month__gte=month).filter(tanggal__month__lte=year).aggregate(total=Sum('jumlah'))
    id100 = jurnal.objects.filter(kategori="Kredit").filter(akun_id__in=[56,74]).filter(tanggal__month__gte=month).filter(tanggal__month__lte=year).aggregate(total=Sum('jumlah'))
    id101 = jurnal.objects.filter(kategori="Debet").filter(akun_id__in=[75,76]).filter(tanggal__month__gte=month).filter(tanggal__month__lte=year).aggregate(total=Sum('jumlah'))
    id102 = jurnal.objects.filter(kategori="Kredit").filter(akun_id__in=[75,76]).filter(tanggal__month__gte=month).filter(tanggal__month__lte=year).aggregate(total=Sum('jumlah'))
    mydate= datetime.datetime.now()
    context = {
        'title':title,
        'akuns':akuns,
        'id1':id1,
        'id2':id2,
        'id3':id3,
        'id4':id4,
        'id5':id5,
        'id6':id6,
        'id11':id11,
        'id12':id12,
        'id13':id13,
        'id14':id14,
        'id15':id15,
        'id16':id16,
        'id46':id46,
        'id26':id26,
        'id47':id47,
        'id27':id27,
        'id48':id48,
        'id28':id28,
        'id49':id49,
        'id29':id29,
        'totaldebet1':totaldebet1,
        'totalkredit1':totalkredit1,
        'totaldebet2':totaldebet2,
        'totalkredit2':totalkredit2,
        'totaldebet3':totaldebet3,
        'totalkredit3':totalkredit3,
        'totaldebet4':totaldebet4,
        'totalkredit4':totalkredit4,
        'totaldebet5':totaldebet5,
        'totalkredit5':totalkredit5,
        'totaldebet6':totaldebet6,
        'totalkredit6':totalkredit6,
        'totaldebet7':totaldebet7,
        'totalkredit7':totalkredit7,
        'totaldebet8':totaldebet8,
        'totalkredit8':totalkredit8,
        'totaldebet9':totaldebet9,
        'totalkredit9':totalkredit9,
        'totaldebet10':totaldebet10,
        'totalkredit10':totalkredit10,
        'id51':id51,
        'id52':id52,
        'id53':id53,
        'id54':id54,
        'id55':id55,
        'id56':id56,
        'id57':id57,
        'id58':id58,
        'id59':id59,
        'id60':id60,
        'id61':id61,
        'id62':id62,
        'id63':id63,
        'id64':id64,
        'id65':id65,
        'id66':id66,
        'id67':id67,
        'id68':id68,
        'id69':id69,
        'id70':id70,
        'id71':id71,
        'id72':id72,
        'id73':id73,
        'id74':id74,
        'id75':id75,
        'id76':id76,
        'id77':id77,
        'id78':id78,
        'id79':id79,
        'id80':id80,
        'id81':id81,
        'id82':id82,
        'id83':id83,
        'id84':id84,
        'id85':id85,
        'id86':id86,
        'id87':id87,
        'id88':id88,
        'id89':id89,
        'id90':id90,
        'id91':id91,
        'id92':id92,
        'id93':id93,
        'id94':id94,
        'id95':id95,
        'id96':id96,
        'id97':id97,
        'id98':id98,
        'id99':id99,
        'id100':id100,
        'id101':id101,
        'id102':id102,
        'mydate':mydate,
        'month':month,
        'year':year,
    }
    
    return render(request, 'neraca/filter.html', context)