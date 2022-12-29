from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('JSData/', views.JSDataKaryawan, name='JSDataKaryawan'),
    
    # ========================= C / R / U / D ================================

    #Tambah Data (C)
    path('TambahData/', views.TambahData, name='TambahData'), 

    #Lihat Data (R)
    path('LihatData/<str:karyawan_id>', views.LihatData, name='LihatData'), 

    #Edit Data (U)
    path('EditData', views.EditData, name='EditData'), 

    #Hapus Data (D)
    path('HapusData/<str:karyawan_id>', views.HapusData, name='HapusData'),


    # ======================== LOGIN / LOGOUT==================================
  
    path('login/', views.Login, name="login"),

    path('login_user', views.LoginUser, name="login_user"),

    path('logout/', views.LogoutUser, name="logout"),

]