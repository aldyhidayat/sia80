
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm
from django import forms
class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(label='',widget=forms.TextInput(
        attrs={'class': 'form-login',  'placeholder': 'Username', 'id': 'hello'}))
    password = forms.CharField(label='',widget=forms.PasswordInput(
        attrs={
            'class': 'form-login',
            'placeholder': 'Password',
            'id': 'hi',
        }
))
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(authentication_form=UserLoginForm), name='login'),
    path('logout', LogoutView.as_view(next_page='login'), name='logout'),
    path('', include('beranda.urls', namespace='beranda')),
    path('laba-rugi/',include('labarugi.urls', namespace='labarugi')),
    path('jurnal/', include('jurnal.urls', namespace='jurnal')),
    path('neraca/', include('neraca.urls', namespace='neraca')),
    path('akun/', include('akun.urls', namespace='akun')),
    
]
