from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Group, Permission
from django.utils import timezone
from ckeditor.fields import RichTextField
# import RichTextField
# Create your models here.



class MasterOrganisasi(models.Model):
    id_organisasi = models.PositiveIntegerField(primary_key=True)
    kode_organisasi =  models.CharField(max_length=225, default='none')
    urai = models.CharField(max_length=225)

class MasterTahun(models.Model):
    tahun = models.CharField(max_length=4)
    status = models.BooleanField(max_length=1, default=False)

class MasterJabatan(models.Model):
    jabatan = models.CharField(max_length=225)
    status = models.BooleanField(max_length=1, default=False)
class MasterLokasi(models.Model):
    kd_lokasi = models.CharField(max_length=225)
    urai = models.TextField(max_length=225)

class MasterPegawai(models.Model):
    nip = models.PositiveIntegerField(primary_key=True)
    nama = models.CharField(max_length=225)
    golongan = models.CharField(max_length=225)
    no_hp = models.CharField(max_length=225)
    eselon = models.CharField(max_length=225)
    alamat = models.CharField(max_length=225)
    pangakat = models.TextField(max_length=225)
    email = models.TextField(max_length=225)

class MasterPengesah(models.Model):
    no_rek = models.TextField(max_length=225)
    nama_bank = models.TextField(max_length=225)
    status = models.BooleanField(max_length=1, default=False)
    jabatan = models.ForeignKey(MasterPegawai, on_delete=models.RESTRICT)

class MasterKegiatan(models.Model):
    kd_bidang = models.TextField(max_length=225)
    urai_bidang = RichTextField()
    kd_program = models.TextField(max_length=225)
    urai_program = RichTextField()
    kd_kegiatan = models.TextField(max_length=225)
    urai_kegiatan = RichTextField()
    kd_subkegiatan = models.TextField(max_length=225)
    urai_subkegiatan = RichTextField()
    pagu = models.TextField(max_length=225)
    pagu_p = models.TextField(max_length=225)

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        # nama = self.normalize_name(nama)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, nama, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)

class UserNew(AbstractBaseUser, PermissionsMixin):
    id_user = models.AutoField(primary_key=True)
    id_organisasi = models.ForeignKey(MasterOrganisasi, on_delete=models.CASCADE, null=True, blank=True)
    nama = models.CharField(max_length=40)
    email = models.EmailField(_("email address"), unique=True)
    hak_akses = models.CharField(max_length=30, default="pegawai")
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    group = models.ManyToManyField(Group, related_name = 'tri_set', blank = True)
    permissstions = models.ManyToManyField(Permission, related_name = 'aldi_set', blank = True)



    