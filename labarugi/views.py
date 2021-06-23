from django.shortcuts import render
from jurnal.models import *
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from django.conf import settings
# Create your views here.
@login_required(login_url=settings.LOGIN_URL)
def dashboard (request):
    title = "Laba Rugi"
    id1 = jurnal.objects.filter(akun_id=101).filter(kategori="Debet").aggregate(total=Sum('jumlah'))
    id2 = jurnal.objects.filter(akun_id=101).filter(kategori="Kredit").aggregate(total=Sum('jumlah'))
    id3 = jurnal.objects.filter(akun_id=102).filter(kategori="Debet").aggregate(total=Sum('jumlah'))
    id4 = jurnal.objects.filter(akun_id=102).filter(kategori="Kredit").aggregate(total=Sum('jumlah'))
    id5 = jurnal.objects.filter(akun_id=104).filter(kategori="Debet").aggregate(total=Sum('jumlah'))
    id6 = jurnal.objects.filter(akun_id=104).filter(kategori="Kredit").aggregate(total=Sum('jumlah'))
    id7 = jurnal.objects.filter(akun_id=105).filter(kategori="Debet").aggregate(total=Sum('jumlah'))
    id8 = jurnal.objects.filter(akun_id=105).filter(kategori="Kredit").aggregate(total=Sum('jumlah'))
    id9 = jurnal.objects.filter(akun_id=106).filter(kategori="Debet").aggregate(total=Sum('jumlah'))
    id10 = jurnal.objects.filter(akun_id=106).filter(kategori="Kredit").aggregate(total=Sum('jumlah'))
    id11 = jurnal.objects.filter(akun_id=107).filter(kategori="Debet").aggregate(total=Sum('jumlah'))
    id12 = jurnal.objects.filter(akun_id=107).filter(kategori="Kredit").aggregate(total=Sum('jumlah'))
    id13 = jurnal.objects.filter(akun_id=108).filter(kategori="Debet").aggregate(total=Sum('jumlah'))
    id14 = jurnal.objects.filter(akun_id=108).filter(kategori="Kredit").aggregate(total=Sum('jumlah'))
    id15 = jurnal.objects.filter(akun_id=109).filter(kategori="Debet").aggregate(total=Sum('jumlah'))
    id16 = jurnal.objects.filter(akun_id=109).filter(kategori="Kredit").aggregate(total=Sum('jumlah'))
    id17 = jurnal.objects.filter(akun_id=110).filter(kategori="Debet").aggregate(total=Sum('jumlah'))
    id18 = jurnal.objects.filter(akun_id=110).filter(kategori="Kredit").aggregate(total=Sum('jumlah'))
    id19 = jurnal.objects.filter(akun_id=111).filter(kategori="Debet").aggregate(total=Sum('jumlah'))
    id20 = jurnal.objects.filter(akun_id=111).filter(kategori="Kredit").aggregate(total=Sum('jumlah'))
    id21 = jurnal.objects.filter(akun_id=112).filter(kategori="Debet").aggregate(total=Sum('jumlah'))
    id22 = jurnal.objects.filter(akun_id=112).filter(kategori="Kredit").aggregate(total=Sum('jumlah'))
    id23 = jurnal.objects.filter(akun_id=113).filter(kategori="Debet").aggregate(total=Sum('jumlah'))
    id24 = jurnal.objects.filter(akun_id=113).filter(kategori="Kredit").aggregate(total=Sum('jumlah'))
    id25 = jurnal.objects.filter(akun_id=114).filter(kategori="Debet").aggregate(total=Sum('jumlah'))
    id26 = jurnal.objects.filter(akun_id=114).filter(kategori="Kredit").aggregate(total=Sum('jumlah'))
    id27 = jurnal.objects.filter(akun_id=115).filter(kategori="Debet").aggregate(total=Sum('jumlah'))
    id28 = jurnal.objects.filter(akun_id=115).filter(kategori="Kredit").aggregate(total=Sum('jumlah'))
    id29 = jurnal.objects.filter(akun_id=116).filter(kategori="Debet").aggregate(total=Sum('jumlah'))
    id30 = jurnal.objects.filter(akun_id=116).filter(kategori="Kredit").aggregate(total=Sum('jumlah'))
    id31 = jurnal.objects.filter(akun_id=117).filter(kategori="Debet").aggregate(total=Sum('jumlah'))
    id32 = jurnal.objects.filter(akun_id=117).filter(kategori="Kredit").aggregate(total=Sum('jumlah'))
    id33 = jurnal.objects.filter(akun_id=118).filter(kategori="Debet").aggregate(total=Sum('jumlah'))
    id34 = jurnal.objects.filter(akun_id=118).filter(kategori="Kredit").aggregate(total=Sum('jumlah'))
    id35 = jurnal.objects.filter(akun_id=119).filter(kategori="Debet").aggregate(total=Sum('jumlah'))
    id36 = jurnal.objects.filter(akun_id=119).filter(kategori="Kredit").aggregate(total=Sum('jumlah'))
    id37 = jurnal.objects.filter(akun_id=120).filter(kategori="Debet").aggregate(total=Sum('jumlah'))
    id38 = jurnal.objects.filter(akun_id=120).filter(kategori="Kredit").aggregate(total=Sum('jumlah'))
    id39 = jurnal.objects.filter(akun_id=121).filter(kategori="Debet").aggregate(total=Sum('jumlah'))
    id40 = jurnal.objects.filter(akun_id=121).filter(kategori="Kredit").aggregate(total=Sum('jumlah'))
    id41 = jurnal.objects.filter(akun_id=122).filter(kategori="Debet").aggregate(total=Sum('jumlah'))
    id42 = jurnal.objects.filter(akun_id=122).filter(kategori="Kredit").aggregate(total=Sum('jumlah'))
    id43 = jurnal.objects.filter(akun_id=123).filter(kategori="Debet").aggregate(total=Sum('jumlah'))
    id44 = jurnal.objects.filter(akun_id=123).filter(kategori="Kredit").aggregate(total=Sum('jumlah'))
    id45 = jurnal.objects.filter(akun_id=124).filter(kategori="Debet").aggregate(total=Sum('jumlah'))
    id46 = jurnal.objects.filter(akun_id=124).filter(kategori="Kredit").aggregate(total=Sum('jumlah'))
    id47 = jurnal.objects.filter(akun_id=125).filter(kategori="Debet").aggregate(total=Sum('jumlah'))
    id48 = jurnal.objects.filter(akun_id=125).filter(kategori="Kredit").aggregate(total=Sum('jumlah'))
    id49 = jurnal.objects.filter(akun_id=126).filter(kategori="Debet").aggregate(total=Sum('jumlah'))
    id50 = jurnal.objects.filter(akun_id=126).filter(kategori="Kredit").aggregate(total=Sum('jumlah'))
    id51 = jurnal.objects.filter(akun_id=127).filter(kategori="Debet").aggregate(total=Sum('jumlah'))
    id52 = jurnal.objects.filter(akun_id=127).filter(kategori="Kredit").aggregate(total=Sum('jumlah'))
    id53 = jurnal.objects.filter(akun_id=128).filter(kategori="Debet").aggregate(total=Sum('jumlah'))
    id54 = jurnal.objects.filter(akun_id=128).filter(kategori="Kredit").aggregate(total=Sum('jumlah'))
    id55 = jurnal.objects.filter(akun_id=129).filter(kategori="Debet").aggregate(total=Sum('jumlah'))
    id56 = jurnal.objects.filter(akun_id=129).filter(kategori="Kredit").aggregate(total=Sum('jumlah'))
    id57 = jurnal.objects.filter(akun_id=130).filter(kategori="Debet").aggregate(total=Sum('jumlah'))
    id58 = jurnal.objects.filter(akun_id=130).filter(kategori="Kredit").aggregate(total=Sum('jumlah'))
    id59 = jurnal.objects.filter(akun_id=131).filter(kategori="Debet").aggregate(total=Sum('jumlah'))
    id60 = jurnal.objects.filter(akun_id=131).filter(kategori="Kredit").aggregate(total=Sum('jumlah'))
    id61 = jurnal.objects.filter(akun_id=132).filter(kategori="Debet").aggregate(total=Sum('jumlah'))
    id62 = jurnal.objects.filter(akun_id=132).filter(kategori="Kredit").aggregate(total=Sum('jumlah'))
    id63 = jurnal.objects.filter(akun_id=133).filter(kategori="Debet").aggregate(total=Sum('jumlah'))
    id64 = jurnal.objects.filter(akun_id=133).filter(kategori="Kredit").aggregate(total=Sum('jumlah'))
    id65 = jurnal.objects.filter(akun_id=134).filter(kategori="Debet").aggregate(total=Sum('jumlah'))
    id66 = jurnal.objects.filter(akun_id=134).filter(kategori="Kredit").aggregate(total=Sum('jumlah'))
    id67 = jurnal.objects.filter(akun_id=135).filter(kategori="Debet").aggregate(total=Sum('jumlah'))
    id68 = jurnal.objects.filter(akun_id=135).filter(kategori="Kredit").aggregate(total=Sum('jumlah'))
    id69 = jurnal.objects.filter(akun_id=136).filter(kategori="Debet").aggregate(total=Sum('jumlah'))
    id70 = jurnal.objects.filter(akun_id=136).filter(kategori="Kredit").aggregate(total=Sum('jumlah'))
    id71 = jurnal.objects.filter(akun_id=137).filter(kategori="Debet").aggregate(total=Sum('jumlah'))
    id72 = jurnal.objects.filter(akun_id=137).filter(kategori="Kredit").aggregate(total=Sum('jumlah'))
    id73 = jurnal.objects.filter(akun_id=138).filter(kategori="Debet").aggregate(total=Sum('jumlah'))
    id74 = jurnal.objects.filter(akun_id=138).filter(kategori="Kredit").aggregate(total=Sum('jumlah'))
    id75 = jurnal.objects.filter(akun_id=139).filter(kategori="Debet").aggregate(total=Sum('jumlah'))
    id76 = jurnal.objects.filter(akun_id=139).filter(kategori="Kredit").aggregate(total=Sum('jumlah'))
    totaldebet1 = jurnal.objects.filter(kategori="Debet").filter(akun__jenis_id=17).aggregate(total=Sum('jumlah'))
    totalkredit1 = jurnal.objects.filter(kategori="Kredit").filter(akun__jenis_id=17).aggregate(total=Sum('jumlah'))
    totaldebet2 = jurnal.objects.filter(kategori="Debet").filter(akun__jenis_id=18).aggregate(total=Sum('jumlah'))
    totalkredit2 = jurnal.objects.filter(kategori="Kredit").filter(akun__jenis_id=18).aggregate(total=Sum('jumlah'))
    totaldebet3 = jurnal.objects.filter(kategori="Debet").filter(akun__jenis_id=20).aggregate(total=Sum('jumlah'))
    totalkredit3 = jurnal.objects.filter(kategori="Kredit").filter(akun__jenis_id=20).aggregate(total=Sum('jumlah'))
    totaldebet4 = jurnal.objects.filter(kategori="Debet").filter(akun__jenis_id=21).aggregate(total=Sum('jumlah'))
    totalkredit4 = jurnal.objects.filter(kategori="Kredit").filter(akun__jenis_id=21).aggregate(total=Sum('jumlah'))
    totaldebet5 = jurnal.objects.filter(kategori="Debet").filter(akun__jenis_id=22).aggregate(total=Sum('jumlah'))
    totalkredit5 = jurnal.objects.filter(kategori="Kredit").filter(akun__jenis_id=22).aggregate(total=Sum('jumlah'))
    totaldebet6 = jurnal.objects.filter(kategori="Debet").filter(akun__jenis_id=23).aggregate(total=Sum('jumlah'))
    totalkredit6 = jurnal.objects.filter(kategori="Kredit").filter(akun__jenis_id=23).aggregate(total=Sum('jumlah'))
    totaldebet7 = jurnal.objects.filter(kategori="Debet").filter(akun__jenis_id=24).aggregate(total=Sum('jumlah'))
    totalkredit7 = jurnal.objects.filter(kategori="Kredit").filter(akun__jenis_id=24).aggregate(total=Sum('jumlah'))
    
    context = {
        'title':title,
        'id1':id1,
        'id2':id2,
        'id3':id3,
        'id4':id4,
        'id5':id5,
        'id6':id6,
        'id7':id7,
        'id8':id8,
        'id9':id9,
        'id10':id10,
        'id11':id11,
        'id12':id12,
        'id13':id13,
        'id14':id14,
        'id15':id15,
        'id16':id16,
        'id17':id17,
        'id18':id18,
        'id19':id19,
        'id20':id20,
        'id21':id21,
        'id22':id22,
        'id23':id23,
        'id24':id24,
        'id25':id25,
        'id26':id26,
        'id27':id27,
        'id28':id28,
        'id29':id29,
        'id30':id30,
        'id31':id31,
        'id32':id32,
        'id33':id33,
        'id34':id34,
        'id35':id35,
        'id36':id36,
        'id37':id37,
        'id38':id38,
        'id39':id39,
        'id40':id40,
        'id41':id41,
        'id42':id42,
        'id43':id43,
        'id44':id44,
        'id45':id45,
        'id46':id46,
        'id47':id47,
        'id48':id48,
        'id49':id49,
        'id50':id50,
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
    }
    return render(request,'labarugi/dashboard.html', context)

@login_required(login_url=settings.LOGIN_URL)
def filterbulan (request):
    month=request.POST.get('bulan')
    bulan2=request.POST.get('bulan2')
    if not month:
        month = "1"
    if not bulan2:
        bulan2 = "12"
    title = "Laba Rugi"
    id1 = jurnal.objects.filter(akun_id=101).filter(kategori="Debet").filter(tanggal__month__gte=month).filter(tanggal__month__lte=bulan2).aggregate(total=Sum('jumlah'))
    id2 = jurnal.objects.filter(akun_id=101).filter(kategori="Kredit").filter(tanggal__month__gte=month).filter(tanggal__month__lte=bulan2).aggregate(total=Sum('jumlah'))
    id3 = jurnal.objects.filter(akun_id=102).filter(kategori="Debet").filter(tanggal__month__gte=month).filter(tanggal__month__lte=bulan2).aggregate(total=Sum('jumlah'))
    id4 = jurnal.objects.filter(akun_id=102).filter(kategori="Kredit").filter(tanggal__month__gte=month).filter(tanggal__month__lte=bulan2).aggregate(total=Sum('jumlah'))
    id5 = jurnal.objects.filter(akun_id=104).filter(kategori="Debet").filter(tanggal__month__gte=month).filter(tanggal__month__lte=bulan2).aggregate(total=Sum('jumlah'))
    id6 = jurnal.objects.filter(akun_id=104).filter(kategori="Kredit").filter(tanggal__month__gte=month).filter(tanggal__month__lte=bulan2).aggregate(total=Sum('jumlah'))
    id7 = jurnal.objects.filter(akun_id=105).filter(kategori="Debet").filter(tanggal__month__gte=month).filter(tanggal__month__lte=bulan2).aggregate(total=Sum('jumlah'))
    id8 = jurnal.objects.filter(akun_id=105).filter(kategori="Kredit").filter(tanggal__month__gte=month).filter(tanggal__month__lte=bulan2).aggregate(total=Sum('jumlah'))
    id9 = jurnal.objects.filter(akun_id=106).filter(kategori="Debet").filter(tanggal__month__gte=month).filter(tanggal__month__lte=bulan2).aggregate(total=Sum('jumlah'))
    id10 = jurnal.objects.filter(akun_id=106).filter(kategori="Kredit").filter(tanggal__month__gte=month).filter(tanggal__month__lte=bulan2).aggregate(total=Sum('jumlah'))
    id11 = jurnal.objects.filter(akun_id=107).filter(kategori="Debet").filter(tanggal__month__gte=month).filter(tanggal__month__lte=bulan2).aggregate(total=Sum('jumlah'))
    id12 = jurnal.objects.filter(akun_id=107).filter(kategori="Kredit").filter(tanggal__month__gte=month).filter(tanggal__month__lte=bulan2).aggregate(total=Sum('jumlah'))
    id13 = jurnal.objects.filter(akun_id=108).filter(kategori="Debet").filter(tanggal__month__gte=month).filter(tanggal__month__lte=bulan2).aggregate(total=Sum('jumlah'))
    id14 = jurnal.objects.filter(akun_id=108).filter(kategori="Kredit").filter(tanggal__month__gte=month).filter(tanggal__month__lte=bulan2).aggregate(total=Sum('jumlah'))
    id15 = jurnal.objects.filter(akun_id=109).filter(kategori="Debet").filter(tanggal__month__gte=month).filter(tanggal__month__lte=bulan2).aggregate(total=Sum('jumlah'))
    id16 = jurnal.objects.filter(akun_id=109).filter(kategori="Kredit").filter(tanggal__month__gte=month).filter(tanggal__month__lte=bulan2).aggregate(total=Sum('jumlah'))
    id17 = jurnal.objects.filter(akun_id=110).filter(kategori="Debet").filter(tanggal__month__gte=month).filter(tanggal__month__lte=bulan2).aggregate(total=Sum('jumlah'))
    id18 = jurnal.objects.filter(akun_id=110).filter(kategori="Kredit").filter(tanggal__month__gte=month).filter(tanggal__month__lte=bulan2).aggregate(total=Sum('jumlah'))
    id19 = jurnal.objects.filter(akun_id=111).filter(kategori="Debet").filter(tanggal__month__gte=month).filter(tanggal__month__lte=bulan2).aggregate(total=Sum('jumlah'))
    id20 = jurnal.objects.filter(akun_id=111).filter(kategori="Kredit").filter(tanggal__month__gte=month).filter(tanggal__month__lte=bulan2).aggregate(total=Sum('jumlah'))
    id21 = jurnal.objects.filter(akun_id=112).filter(kategori="Debet").filter(tanggal__month__gte=month).filter(tanggal__month__lte=bulan2).aggregate(total=Sum('jumlah'))
    id22 = jurnal.objects.filter(akun_id=112).filter(kategori="Kredit").filter(tanggal__month__gte=month).filter(tanggal__month__lte=bulan2).aggregate(total=Sum('jumlah'))
    id23 = jurnal.objects.filter(akun_id=113).filter(kategori="Debet").filter(tanggal__month__gte=month).filter(tanggal__month__lte=bulan2).aggregate(total=Sum('jumlah'))
    id24 = jurnal.objects.filter(akun_id=113).filter(kategori="Kredit").filter(tanggal__month__gte=month).filter(tanggal__month__lte=bulan2).aggregate(total=Sum('jumlah'))
    id25 = jurnal.objects.filter(akun_id=114).filter(kategori="Debet").filter(tanggal__month__gte=month).filter(tanggal__month__lte=bulan2).aggregate(total=Sum('jumlah'))
    id26 = jurnal.objects.filter(akun_id=114).filter(kategori="Kredit").filter(tanggal__month__gte=month).filter(tanggal__month__lte=bulan2).aggregate(total=Sum('jumlah'))
    id27 = jurnal.objects.filter(akun_id=115).filter(kategori="Debet").filter(tanggal__month__gte=month).filter(tanggal__month__lte=bulan2).aggregate(total=Sum('jumlah'))
    id28 = jurnal.objects.filter(akun_id=115).filter(kategori="Kredit").filter(tanggal__month__gte=month).filter(tanggal__month__lte=bulan2).aggregate(total=Sum('jumlah'))
    id29 = jurnal.objects.filter(akun_id=116).filter(kategori="Debet").filter(tanggal__month__gte=month).filter(tanggal__month__lte=bulan2).aggregate(total=Sum('jumlah'))
    id30 = jurnal.objects.filter(akun_id=116).filter(kategori="Kredit").filter(tanggal__month__gte=month).filter(tanggal__month__lte=bulan2).aggregate(total=Sum('jumlah'))
    id31 = jurnal.objects.filter(akun_id=117).filter(kategori="Debet").filter(tanggal__month__gte=month).filter(tanggal__month__lte=bulan2).aggregate(total=Sum('jumlah'))
    id32 = jurnal.objects.filter(akun_id=117).filter(kategori="Kredit").filter(tanggal__month__gte=month).filter(tanggal__month__lte=bulan2).aggregate(total=Sum('jumlah'))
    id33 = jurnal.objects.filter(akun_id=118).filter(kategori="Debet").filter(tanggal__month__gte=month).filter(tanggal__month__lte=bulan2).aggregate(total=Sum('jumlah'))
    id34 = jurnal.objects.filter(akun_id=118).filter(kategori="Kredit").filter(tanggal__month__gte=month).filter(tanggal__month__lte=bulan2).aggregate(total=Sum('jumlah'))
    id35 = jurnal.objects.filter(akun_id=119).filter(kategori="Debet").filter(tanggal__month__gte=month).filter(tanggal__month__lte=bulan2).aggregate(total=Sum('jumlah'))
    id36 = jurnal.objects.filter(akun_id=119).filter(kategori="Kredit").filter(tanggal__month__gte=month).filter(tanggal__month__lte=bulan2).aggregate(total=Sum('jumlah'))
    id37 = jurnal.objects.filter(akun_id=120).filter(kategori="Debet").filter(tanggal__month__gte=month).filter(tanggal__month__lte=bulan2).aggregate(total=Sum('jumlah'))
    id38 = jurnal.objects.filter(akun_id=120).filter(kategori="Kredit").filter(tanggal__month__gte=month).filter(tanggal__month__lte=bulan2).aggregate(total=Sum('jumlah'))
    id39 = jurnal.objects.filter(akun_id=121).filter(kategori="Debet").filter(tanggal__month__gte=month).filter(tanggal__month__lte=bulan2).aggregate(total=Sum('jumlah'))
    id40 = jurnal.objects.filter(akun_id=121).filter(kategori="Kredit").filter(tanggal__month__gte=month).filter(tanggal__month__lte=bulan2).aggregate(total=Sum('jumlah'))
    id41 = jurnal.objects.filter(akun_id=122).filter(kategori="Debet").filter(tanggal__month__gte=month).filter(tanggal__month__lte=bulan2).aggregate(total=Sum('jumlah'))
    id42 = jurnal.objects.filter(akun_id=122).filter(kategori="Kredit").filter(tanggal__month__gte=month).filter(tanggal__month__lte=bulan2).aggregate(total=Sum('jumlah'))
    id43 = jurnal.objects.filter(akun_id=123).filter(kategori="Debet").filter(tanggal__month__gte=month).filter(tanggal__month__lte=bulan2).aggregate(total=Sum('jumlah'))
    id44 = jurnal.objects.filter(akun_id=123).filter(kategori="Kredit").filter(tanggal__month__gte=month).filter(tanggal__month__lte=bulan2).aggregate(total=Sum('jumlah'))
    id45 = jurnal.objects.filter(akun_id=124).filter(kategori="Debet").filter(tanggal__month__gte=month).filter(tanggal__month__lte=bulan2).aggregate(total=Sum('jumlah'))
    id46 = jurnal.objects.filter(akun_id=124).filter(kategori="Kredit").filter(tanggal__month__gte=month).filter(tanggal__month__lte=bulan2).aggregate(total=Sum('jumlah'))
    id47 = jurnal.objects.filter(akun_id=125).filter(kategori="Debet").filter(tanggal__month__gte=month).filter(tanggal__month__lte=bulan2).aggregate(total=Sum('jumlah'))
    id48 = jurnal.objects.filter(akun_id=125).filter(kategori="Kredit").filter(tanggal__month__gte=month).filter(tanggal__month__lte=bulan2).aggregate(total=Sum('jumlah'))
    id49 = jurnal.objects.filter(akun_id=126).filter(kategori="Debet").filter(tanggal__month__gte=month).filter(tanggal__month__lte=bulan2).aggregate(total=Sum('jumlah'))
    id50 = jurnal.objects.filter(akun_id=126).filter(kategori="Kredit").filter(tanggal__month__gte=month).filter(tanggal__month__lte=bulan2).aggregate(total=Sum('jumlah'))
    id51 = jurnal.objects.filter(akun_id=127).filter(kategori="Debet").filter(tanggal__month__gte=month).filter(tanggal__month__lte=bulan2).aggregate(total=Sum('jumlah'))
    id52 = jurnal.objects.filter(akun_id=127).filter(kategori="Kredit").filter(tanggal__month__gte=month).filter(tanggal__month__lte=bulan2).aggregate(total=Sum('jumlah'))
    id53 = jurnal.objects.filter(akun_id=128).filter(kategori="Debet").filter(tanggal__month__gte=month).filter(tanggal__month__lte=bulan2).aggregate(total=Sum('jumlah'))
    id54 = jurnal.objects.filter(akun_id=128).filter(kategori="Kredit").filter(tanggal__month__gte=month).filter(tanggal__month__lte=bulan2).aggregate(total=Sum('jumlah'))
    id55 = jurnal.objects.filter(akun_id=129).filter(kategori="Debet").filter(tanggal__month__gte=month).filter(tanggal__month__lte=bulan2).aggregate(total=Sum('jumlah'))
    id56 = jurnal.objects.filter(akun_id=129).filter(kategori="Kredit").filter(tanggal__month__gte=month).filter(tanggal__month__lte=bulan2).aggregate(total=Sum('jumlah'))
    id57 = jurnal.objects.filter(akun_id=130).filter(kategori="Debet").filter(tanggal__month__gte=month).filter(tanggal__month__lte=bulan2).aggregate(total=Sum('jumlah'))
    id58 = jurnal.objects.filter(akun_id=130).filter(kategori="Kredit").filter(tanggal__month__gte=month).filter(tanggal__month__lte=bulan2).aggregate(total=Sum('jumlah'))
    id59 = jurnal.objects.filter(akun_id=131).filter(kategori="Debet").filter(tanggal__month__gte=month).filter(tanggal__month__lte=bulan2).aggregate(total=Sum('jumlah'))
    id60 = jurnal.objects.filter(akun_id=131).filter(kategori="Kredit").filter(tanggal__month__gte=month).filter(tanggal__month__lte=bulan2).aggregate(total=Sum('jumlah'))
    id61 = jurnal.objects.filter(akun_id=132).filter(kategori="Debet").filter(tanggal__month__gte=month).filter(tanggal__month__lte=bulan2).aggregate(total=Sum('jumlah'))
    id62 = jurnal.objects.filter(akun_id=132).filter(kategori="Kredit").filter(tanggal__month__gte=month).filter(tanggal__month__lte=bulan2).aggregate(total=Sum('jumlah'))
    id63 = jurnal.objects.filter(akun_id=133).filter(kategori="Debet").filter(tanggal__month__gte=month).filter(tanggal__month__lte=bulan2).aggregate(total=Sum('jumlah'))
    id64 = jurnal.objects.filter(akun_id=133).filter(kategori="Kredit").filter(tanggal__month__gte=month).filter(tanggal__month__lte=bulan2).aggregate(total=Sum('jumlah'))
    id65 = jurnal.objects.filter(akun_id=134).filter(kategori="Debet").filter(tanggal__month__gte=month).filter(tanggal__month__lte=bulan2).aggregate(total=Sum('jumlah'))
    id66 = jurnal.objects.filter(akun_id=134).filter(kategori="Kredit").filter(tanggal__month__gte=month).filter(tanggal__month__lte=bulan2).aggregate(total=Sum('jumlah'))
    id67 = jurnal.objects.filter(akun_id=135).filter(kategori="Debet").filter(tanggal__month__gte=month).filter(tanggal__month__lte=bulan2).aggregate(total=Sum('jumlah'))
    id68 = jurnal.objects.filter(akun_id=135).filter(kategori="Kredit").filter(tanggal__month__gte=month).filter(tanggal__month__lte=bulan2).aggregate(total=Sum('jumlah'))
    id69 = jurnal.objects.filter(akun_id=136).filter(kategori="Debet").filter(tanggal__month__gte=month).filter(tanggal__month__lte=bulan2).aggregate(total=Sum('jumlah'))
    id70 = jurnal.objects.filter(akun_id=136).filter(kategori="Kredit").filter(tanggal__month__gte=month).filter(tanggal__month__lte=bulan2).aggregate(total=Sum('jumlah'))
    id71 = jurnal.objects.filter(akun_id=137).filter(kategori="Debet").filter(tanggal__month__gte=month).filter(tanggal__month__lte=bulan2).aggregate(total=Sum('jumlah'))
    id72 = jurnal.objects.filter(akun_id=137).filter(kategori="Kredit").filter(tanggal__month__gte=month).filter(tanggal__month__lte=bulan2).aggregate(total=Sum('jumlah'))
    id73 = jurnal.objects.filter(akun_id=138).filter(kategori="Debet").filter(tanggal__month__gte=month).filter(tanggal__month__lte=bulan2).aggregate(total=Sum('jumlah'))
    id74 = jurnal.objects.filter(akun_id=138).filter(kategori="Kredit").filter(tanggal__month__gte=month).filter(tanggal__month__lte=bulan2).aggregate(total=Sum('jumlah'))
    id75 = jurnal.objects.filter(akun_id=139).filter(kategori="Debet").filter(tanggal__month__gte=month).filter(tanggal__month__lte=bulan2).aggregate(total=Sum('jumlah'))
    id76 = jurnal.objects.filter(akun_id=139).filter(kategori="Kredit").filter(tanggal__month__gte=month).filter(tanggal__month__lte=bulan2).aggregate(total=Sum('jumlah'))
    totaldebet1 = jurnal.objects.filter(kategori="Debet").filter(akun__jenis_id=17).filter(tanggal__month__gte=month).filter(tanggal__month__lte=bulan2).aggregate(total=Sum('jumlah'))
    totalkredit1 = jurnal.objects.filter(kategori="Kredit").filter(akun__jenis_id=17).filter(tanggal__month__gte=month).filter(tanggal__month__lte=bulan2).aggregate(total=Sum('jumlah'))
    totaldebet2 = jurnal.objects.filter(kategori="Debet").filter(akun__jenis_id=18).filter(tanggal__month__gte=month).filter(tanggal__month__lte=bulan2).aggregate(total=Sum('jumlah'))
    totalkredit2 = jurnal.objects.filter(kategori="Kredit").filter(akun__jenis_id=18).filter(tanggal__month__gte=month).filter(tanggal__month__lte=bulan2).aggregate(total=Sum('jumlah'))
    totaldebet3 = jurnal.objects.filter(kategori="Debet").filter(akun__jenis_id=20).filter(tanggal__month__gte=month).filter(tanggal__month__lte=bulan2).aggregate(total=Sum('jumlah'))
    totalkredit3 = jurnal.objects.filter(kategori="Kredit").filter(akun__jenis_id=20).filter(tanggal__month__gte=month).filter(tanggal__month__lte=bulan2).aggregate(total=Sum('jumlah'))
    totaldebet4 = jurnal.objects.filter(kategori="Debet").filter(akun__jenis_id=21).filter(tanggal__month__gte=month).filter(tanggal__month__lte=bulan2).aggregate(total=Sum('jumlah'))
    totalkredit4 = jurnal.objects.filter(kategori="Kredit").filter(akun__jenis_id=21).filter(tanggal__month__gte=month).filter(tanggal__month__lte=bulan2).aggregate(total=Sum('jumlah'))
    totaldebet5 = jurnal.objects.filter(kategori="Debet").filter(akun__jenis_id=22).filter(tanggal__month__gte=month).filter(tanggal__month__lte=bulan2).aggregate(total=Sum('jumlah'))
    totalkredit5 = jurnal.objects.filter(kategori="Kredit").filter(akun__jenis_id=22).filter(tanggal__month__gte=month).filter(tanggal__month__lte=bulan2).aggregate(total=Sum('jumlah'))
    totaldebet6 = jurnal.objects.filter(kategori="Debet").filter(akun__jenis_id=23).filter(tanggal__month__gte=month).filter(tanggal__month__lte=bulan2).aggregate(total=Sum('jumlah'))
    totalkredit6 = jurnal.objects.filter(kategori="Kredit").filter(akun__jenis_id=23).filter(tanggal__month__gte=month).filter(tanggal__month__lte=bulan2).aggregate(total=Sum('jumlah'))
    totaldebet7 = jurnal.objects.filter(kategori="Debet").filter(akun__jenis_id=24).filter(tanggal__month__gte=month).filter(tanggal__month__lte=bulan2).aggregate(total=Sum('jumlah'))
    totalkredit7 = jurnal.objects.filter(kategori="Kredit").filter(akun__jenis_id=24).filter(tanggal__month__gte=month).filter(tanggal__month__lte=bulan2).aggregate(total=Sum('jumlah'))
    
    context = {
        'title':title,
        'id1':id1,
        'id2':id2,
        'id3':id3,
        'id4':id4,
        'id5':id5,
        'id6':id6,
        'id7':id7,
        'id8':id8,
        'id9':id9,
        'id10':id10,
        'id11':id11,
        'id12':id12,
        'id13':id13,
        'id14':id14,
        'id15':id15,
        'id16':id16,
        'id17':id17,
        'id18':id18,
        'id19':id19,
        'id20':id20,
        'id21':id21,
        'id22':id22,
        'id23':id23,
        'id24':id24,
        'id25':id25,
        'id26':id26,
        'id27':id27,
        'id28':id28,
        'id29':id29,
        'id30':id30,
        'id31':id31,
        'id32':id32,
        'id33':id33,
        'id34':id34,
        'id35':id35,
        'id36':id36,
        'id37':id37,
        'id38':id38,
        'id39':id39,
        'id40':id40,
        'id41':id41,
        'id42':id42,
        'id43':id43,
        'id44':id44,
        'id45':id45,
        'id46':id46,
        'id47':id47,
        'id48':id48,
        'id49':id49,
        'id50':id50,
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
        'month':month,
        'bulan2':bulan2,
    }
    return render(request,'labarugi/filterbulan.html', context)