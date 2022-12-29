from django.shortcuts import render
from apps.models import DataPegawai
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required 
from django.views.decorators.cache import cache_control # Destroy the section after logout

# Create your views here.
@login_required(login_url="/login/")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def home(request):
    DataKaryawan = DataPegawai.objects.all()
    return render(request, 'apps/home.html',{"karyawan":DataKaryawan})

def JSDataKaryawan(request):
    karyawan = DataPegawai.objects.all()
    data = [datakaryawan.get_data() for datakaryawan in karyawan ]
    response = {'data': data}
    return JsonResponse(response)


#Tambah Data (C)
def TambahData(request):
    if request.method =="POST":
        if request.POST.get('nama') and request.POST.get('email') and request.POST.get('jabatan') and request.POST.get('gaji') and request.POST.get('jeniskelamin') or request.POST.get('note'):
            karyawan = DataPegawai()
            karyawan.nama = request.POST.get('nama')
            karyawan.email = request.POST.get('email')
            karyawan.jabatan = request.POST.get('jabatan')
            karyawan.gaji = request.POST.get('gaji')
            karyawan.jeniskelamin = request.POST.get('jeniskelamin')
            karyawan.note = request.POST.get('note')
            karyawan.save()
            messages.success(request, "Data Berhasil ditambahkan!")
            return HttpResponseRedirect("/")
    else:
            return render(request, 'apps/TambahData.html')

#Lihat Data (R)
def LihatData(request, karyawan_id):
    karyawan = DataPegawai.objects.get (id=karyawan_id)
    if karyawan != None:
        return render(request, "apps/LihatData.html", {'karyawan':karyawan})

#Edit Data (U)
def EditData(request):
    if request.method == "POST":
        karyawan = DataPegawai.objects.get(id = request.POST.get('id'))
        if karyawan != None:
            karyawan.nama = request.POST.get('nama')
            karyawan.email = request.POST.get('email')
            karyawan.jabatan = request.POST.get('jabatan')
            karyawan.gaji = request.POST.get('gaji')
            karyawan.jeniskelamin = request.POST.get('jeniskelamin')
            karyawan.note = request.POST.get('note')
            karyawan.save()
            messages.success(request, "Data Berhasil dirubah!")
            return HttpResponseRedirect("/")

#Hapus Data (D)
def HapusData(request, karyawan_id):
    karyawan = DataPegawai.objects.get(id=karyawan_id)
    karyawan.delete()
    messages.success(request, "Data Berhasil dihapus!")
    return HttpResponseRedirect("/")


# Login Function
def Login(request):
    if request.user == None or request.user == "" or request.user.username == "":
        return render(request, "apps/login.html")
    else:
        return HttpResponseRedirect('/')
 
# Login User
def LoginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        if user != None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            messages.error(request, "Silahkan Isi Kembali data anda dengan benar.")
            return HttpResponseRedirect('/')

# logout Functin
def LogoutUser (request):
    logout(request)
    request.user = None
    return HttpResponseRedirect('/')


