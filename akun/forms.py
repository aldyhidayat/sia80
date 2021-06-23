from django.forms import ModelForm
from django import forms
from .models import *

class FormAkun(ModelForm):
    class Meta:
        model = akun
        fields = ['no','nama','jenis']

        widgets = {
            'no' : forms.NumberInput({'class':'form-input-small'}),
            'nama' : forms.TextInput({'class':'form-input'}),
            'jenis' : forms.Select({'class':'form-input'}),
        }