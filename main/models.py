from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Group, Permission
from django.utils import timezone
# Create your models here.



class MasterOrganisasi(models.Model):
    id_organisasi = models.PositiveIntegerField(primary_key=True)
    tahun = models.CharField(max_length=4)
    urai = models.CharField(max_length=100)

    
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


class spt(models.Model):
    id_spt = models.PositiveIntegerField(primary_key=True)
    nip = models.CharField(max_length=20)
    nama = models.CharField(max_length=100)
    alamat = models.CharField(max_length=100)
    golonga = models.CharField(max_length=100)
    alamat = models.CharField(max_length=100)
    no_hp = models.CharField(max_length=100)
    eselon = models.CharField(max_length=100)
    pangkat = models.CharField(max_length=100)
    tgl_terbit = models.DateTimeField(default=timezone.now)

class konfirmasi(models.Model):
    id_konfirmasi = models.PositiveIntegerField(primary_key=True)
    id_spt = models.ForeignKey(spt, on_delete=models.CASCADE, null=True, blank=True)
    id_user = models.ForeignKey(UserNew, on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=30)
    ket = models.CharField(max_length=100)
    waktu = mmodels.DateTimeField(default=timezone.now)


class sppd(models.Model):
    id_sppd = models.PositiveIntegerField(primary_key=True)
    id_spt = models.ForeignKey(spt, on_delete=models.CASCADE, null=True, blank=True)
    id_user = models.ForeignKey(UserNew, on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=30)
    ket = models.CharField(max_length=100)
    waktu = mmodels.DateTimeField(default=timezone.now)

    