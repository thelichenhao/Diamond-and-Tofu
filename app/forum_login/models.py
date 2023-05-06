from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import CustomUserManager
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Address(models.Model):
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)
    country = models.CharField(max_length=50)
    def __str__(self):
        return self.address1 + " " + self.address2 + " " + self.city + " " + self.state + " " + self.zipcode + " " + self.country


class CustomUser(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(_("email address"), unique=True)
    name = models.CharField(max_length=100, default="Anonymous")
    tofu_credit = models.IntegerField(default=0)
    gender = models.CharField(max_length=50, default="I do not wish to provide this information")
    description = models.TextField(max_length=500, blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.name