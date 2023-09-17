from django.shortcuts import render, redirect
from .models import UserNew

from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.hashers import make_password

# Create your views here.
def login(request):
    return render(request, 'auth/login.html')

def dash(request):
    return render(request, 'dashboard/index.html')

def laporan(request):
    return render(request, 'laporan/laporan.html')

def master(request):
    return render(request, 'master/master.html')

def spt(request):
    return render(request, 'spt/spt.html')

def sppd(request):
    return render(request, 'sppd/input_sppd.html')

def jabatan(request):
    return render(request, 'master/master_jabatan.html')

def kegiatan(request):
    return render(request, 'master/master_kegiatan.html')

def lokasi(request):
    return render(request, 'master/master_lokasi.html')

def organisasi(request):
    return render(request, 'master/master_organisasi.html')

def pegawai(request):
    return render(request, 'master/master_pegawai.html')

def pengesah(request):
    return render(request, 'master/master_pengesah.html')

def ssh(request):
    return render(request, 'master/master_ssh.html')

def tahun(request):
    return render(request, 'master/master_tahun.html')

def loginUser(request):

    if request.method == 'GET':
        contex = {
            'title' : 'Login'
        }   
        return render(request, 'auth/login.html', contex)
    if request.method == 'POST':

        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('SPPD:dash')
        else:
            return redirect('SPPD:login')


def addUser(request):
    contex = {
        'title' : 'Add User'
    }

    if request.method == "POST":
        nama = request.POST.get('nama')
        email = request.POST.get('email')
        password = request.POST.get('password')

        insert = UserNew()
        insert.email = email
        insert.nama = nama
        insert.set_password(password)
        insert.save()

        return redirect('SPPD:login')

    return render(request, 'auth/addUser.html', contex)
