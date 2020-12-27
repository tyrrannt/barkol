from django.db import models
from django.contrib.auth.models import AbstractUser


class Address(models.Model):
    postal_code = models.CharField(verbose_name='индекс', max_length=6, blank=True, null=True, help_text='')
    country = models.CharField(verbose_name='страна', max_length=30, blank=True, null=True, help_text='')
    region = models.CharField(verbose_name='область', max_length=30, blank=True, null=True, help_text='')
    district = models.CharField(verbose_name='район', max_length=30, blank=True, null=True, help_text='')
    microdistrict = models.CharField(verbose_name='микрорайон', max_length=30, blank=True, null=True, help_text='')
    city = models.CharField(verbose_name='город', max_length=30, blank=True, null=True, help_text='')
    street = models.CharField(verbose_name='улица', max_length=60, blank=True, null=True, help_text='')
    house = models.CharField(verbose_name='дом', max_length=6, blank=True, null=True, help_text='')
    apartment = models.CharField(verbose_name='квартира', max_length=3, blank=True, null=True, help_text='')

    def __str__(self):
        return f'{self.postal_code}, {self.country}, {self.region}, {self.city}, {self.street}, {self.house}, {self.apartment}'


class Person(AbstractUser):
    type_of = [
        ('natural_person', 'физическое лицо'),
        ('staff_member', 'штатный сотрудник'),
        ('freelancer', 'внештатный сотрудник')
    ]
    surname = models.CharField(verbose_name='отчество', max_length=40, blank=True, null=True, help_text='')
    avatar = models.ImageField(upload_to='users_avatars', blank=True, help_text='')
    birthday = models.DateField(verbose_name='день рождения', blank=True, null=True, help_text='')
    access_right = models.SmallIntegerField(verbose_name='права доступа', default=0, help_text='')
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, help_text='')
    type_users = models.CharField(verbose_name='тип пользователя', max_length=40, choices=type_of, help_text='')

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.surname}'


class Counteragent(models.Model):
    type_of = [
        ('juridical_person', 'юридическое лицо'),
        ('physical_person', 'физическое лицо'),
        ('separate_subdivision', 'обособленное подразделение'),
        ('government_agency', 'государственный орган'),
    ]
    type_counteragent = models.CharField(verbose_name='тип контрагента', max_length=40, choices=type_of, help_text='')
