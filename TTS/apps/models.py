from django.db import models

# Create your models here.
class DataPegawai(models.Model):
    JK = (
        ('Pria' , 'Pria'),
        ('Wanita','Wanita'), 
        )
    id = models.IntegerField(primary_key=True)
    nama = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    jabatan = models.CharField(max_length=100)
    gaji = models.CharField(max_length=100)
    jeniskelamin = models.CharField(max_length=100, null=True, choices=JK)
    note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nama

    def get_data(self):
        return {
            'id': self.id,
            'nama': self.nama,
            'email': self.email,
            'jabatan': self.jabatan,
            'gaji': self.gaji,
            'jeniskelamin': self.jeniskelamin,
        }