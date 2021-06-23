from django.forms import ModelForm
from django import forms
from .models import *

class FormJurnal(ModelForm):
    class Meta:
        model = jurnal
        fields = ['akun', 'tanggal', 'keterangan', 'jumlah', 'kategori']
        
        widgets = {
            'akun' : forms.Select({'class':'form-input'}),
            'kategori' : forms.Select({'class':'form-input-small'}),
            'keterangan': forms.TextInput({'class':'form-input'}),
            'jumlah': forms.NumberInput({'class':'form-input'}),
            'tanggal': forms.SelectDateWidget({'class':'form-input-small'})
        }
