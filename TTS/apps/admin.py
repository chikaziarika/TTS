from django.contrib import admin
from apps.models import DataPegawai
# Register your models here.

class AdmDataPegawai(admin.ModelAdmin):
    list_display = ['nama', 'email','jabatan','jeniskelamin','created_at']
    search_fields = ['nama', 'email','jabatan']
    list_filter = ['jeniskelamin']
    list_per_page = 8

admin.site.register(DataPegawai, AdmDataPegawai)