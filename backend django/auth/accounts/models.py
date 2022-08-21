from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import RegexValidator
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, is_staff=False, is_active=True, is_admin=False):
        if not email:
            raise ValueError('users must have a email number')
        if not password:
            raise ValueError('user must have a password')

        user_obj = self.model(
            email=email
        )
        user_obj.set_password(password)
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
            is_staff=True,


        )
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
            is_staff=True,
            is_admin=True,


        )
        return user



class User(AbstractBaseUser):
    email = models.EmailField(max_length=60,unique=True)
    name        = models.CharField(max_length = 20, blank = True, null = True)
    first_login = models.BooleanField(default=False)
    active      = models.BooleanField(default=True)
    staff       = models.BooleanField(default=False)
    admin       = models.BooleanField(default=False)
    timestamp   = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        if self.name:
            return self.name
        return self.email

    def get_short_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):

        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active

class EmailOTP(models.Model):
    email = models.EmailField(max_length=60,unique=True)
    otp         = models.CharField(max_length = 9, blank = True, null= True)
    count       = models.IntegerField(default = 0, help_text = 'Number of otp sent')
    validated  = models.BooleanField(default=False,help_text="if it is true that means user have validate otp")


    def __str__(self):
        return str(self.email) + ' is sent ' + str(self.otp)
