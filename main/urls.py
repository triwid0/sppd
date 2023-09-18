from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls.static import static

app_name = 'SPPD'
urlpatterns = [
    path('', views.loginUser, name='login'),
    path('adduser/', views.addUser, name='adduser'),
    path('master_jabatan/tambah/', views.tambah, name='tambah'),
    path('master_jabatan/hapus/<int:idedit>', views.hapus, name='hapus'),
    # path('form_edit/', views.form_edit, name='formEdit'),
    path('master_jabatan/edit/<int:idedit>', views.editData, name='editData'),

    # path('data/', views.read, name='read'),

    path('dash/', views.dash, name='dash'),
    path('laporan/', views.laporan, name='laporan'),
    path('master/', views.master, name='master'),
    path('spt/', views.spt, name='spt'),
    path('sppd/', views.sppd, name='sppd'),
    path('master_jabatan/', views.jabatan, name='jabatan'),
    path('master_kegiatan/', views.kegiatan, name='kegiatan'),
    path('master_lokasi/', views.lokasi, name='lokasi'),
    path('master_organisasi/', views.organisasi, name='organisasi'),
    path('master_pegawai/', views.pegawai, name='pegawai'),
    path('master_pengesah/', views.pengesah, name='pengesah'),
    path('master_ssh/', views.ssh, name='ssh'),
    path('master_tahun/', views.tahun, name='tahun'),
]