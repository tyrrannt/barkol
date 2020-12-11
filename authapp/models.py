from django.db import models
from django.contrib.auth.models import AbstractUser


class CorpUser(AbstractUser):
    surname = models.CharField(verbose_name='отчество', max_length=40, blank=True, null=True)
    email = models.EmailField(verbose_name='электронная почта', blank=True)
    avatar = models.ImageField(upload_to='users_avatars', blank=True)
    birthday = models.DateField(verbose_name='день рождения', blank=True, null=True)
    access_right = models.SmallIntegerField(verbose_name='права доступа', default=0)
