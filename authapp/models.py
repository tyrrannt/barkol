from django.db import models
from django.contrib.auth.models import AbstractUser
from libapp.models import Division, AccessLevel


class Country(models.Model):
    code = models.CharField(verbose_name='код', max_length=3, blank=True, null=True, help_text='')
    name = models.CharField(verbose_name='страна', max_length=30, blank=True, null=True, help_text='')

    def __str__(self):
        return self.name


class City(models.Model):
    city_id = models.SmallIntegerField(verbose_name='')
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, help_text='')
    city_name = models.CharField(verbose_name='город', max_length=30, blank=True, null=True, help_text='')

    def __str__(self):
        return self.city_name


class Weather(models.Model):
    weather_date = models.DateField(verbose_name='Дата')
    coord_lon = models.FloatField(verbose_name='Долгота')
    coord_lat = models.FloatField(verbose_name='Широта')
    weather_id = models.SmallIntegerField(verbose_name='ID')
    weather_main = models.CharField(verbose_name='Погодные явление', max_length=20, blank=True, null=True, help_text='')
    weather_description = models.CharField(verbose_name='Погодные условия', max_length=40, blank=True, null=True,
                                           help_text='')
    weather_icon = models.CharField(verbose_name='Иконка', max_length=4, blank=True, null=True, help_text='')
    main_temp = models.FloatField(verbose_name='Температура')
    main_feels_like = models.FloatField(verbose_name='Ощущение')
    main_temp_min = models.FloatField(verbose_name='Минимальная температура')
    main_temp_max = models.FloatField(verbose_name='Максимальная температура')
    main_pressure = models.FloatField(verbose_name='Давление')
    main_humidity = models.SmallIntegerField(verbose_name='Влажность')
    visibility = models.SmallIntegerField(verbose_name='Видимость')
    wind_speed = models.SmallIntegerField(verbose_name='Скорость ветра')
    wind_deg = models.SmallIntegerField(verbose_name='Направление ветра')
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, help_text='', verbose_name='Страна')
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, help_text='', verbose_name='Город')

    def __str__(self):
        return f'{self.city} / {self.weather_date}'


class PhoneNumber(models.Model):
    number = models.CharField(verbose_name='Номер телефона', max_length=15)

    def __str__(self):
        return f'{self.number}'


class Address(models.Model):
    postal_code = models.CharField(verbose_name='индекс', max_length=6, blank=True, null=True, help_text='')
    country = models.ForeignKey(Country, verbose_name='страна', on_delete=models.SET_NULL, null=True, help_text='')
    region = models.CharField(verbose_name='область', max_length=30, blank=True, null=True, help_text='')
    district = models.CharField(verbose_name='район', max_length=30, blank=True, null=True, help_text='')
    microdistrict = models.CharField(verbose_name='микрорайон', max_length=30, blank=True, null=True, help_text='')
    city = models.ForeignKey(City, verbose_name='город', on_delete=models.SET_NULL, null=True, help_text='')
    street = models.CharField(verbose_name='улица', max_length=60, blank=True, null=True, help_text='')
    house = models.CharField(verbose_name='дом', max_length=6, blank=True, null=True, help_text='')
    apartment = models.CharField(verbose_name='квартира', max_length=3, blank=True, null=True, help_text='')

    def __str__(self):
        result = ''
        if self.postal_code:
            result += f'{self.postal_code}'
        if self.country:
            result += f', {self.country}'
        if self.region:
            result += f', {self.region}'
        if self.city:
            result += f', г. {self.city}'
        if self.street:
            result += f', ул. {self.street}'
        if self.house:
            result += f', д. {self.house}'
        if self.apartment:
            result += f', кв. {self.apartment}'

        return result


class Job(models.Model):
    code = models.CharField(verbose_name='код должности', max_length=100, help_text='', default='000')
    name = models.CharField(verbose_name='должность', max_length=100, help_text='')


class Work(models.Model):
    job = models.ForeignKey(Job, verbose_name='должность', on_delete=models.SET_NULL, null=True, help_text='')
    divisions = models.ForeignKey(Division, verbose_name='подразделение', on_delete=models.SET_NULL, null=True,
                                  help_text='')


class Person(AbstractUser):
    type_of = [
        ('natural_person', 'физическое лицо'),
        ('staff_member', 'штатный сотрудник'),
        ('freelancer', 'внештатный сотрудник')
    ]
    type_of_gender = [
        ('male', 'мужской'),
        ('female', 'женский')
    ]
    surname = models.CharField(verbose_name='отчество', max_length=40, blank=True, null=True, help_text='')
    avatar = models.ImageField(upload_to='users_avatars', blank=True, help_text='')
    birthday = models.DateField(verbose_name='день рождения', blank=True, null=True, help_text='')
    access_right = models.ManyToManyField(AccessLevel, verbose_name='права доступа', default=0, help_text='')
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, help_text='')
    type_users = models.CharField(verbose_name='тип пользователя', max_length=40, choices=type_of, help_text='')
    phone = models.OneToOneField(PhoneNumber, verbose_name='номер телефона', on_delete=models.SET_NULL, null=True, related_name='cell')
    corp_phone = models.OneToOneField(PhoneNumber, verbose_name='корпоративный номер', on_delete=models.SET_NULL, null=True, related_name='corp')
    works = models.ForeignKey(Work, verbose_name='занятость', on_delete=models.SET_NULL, blank=True, null=True)
    gender = models.CharField(verbose_name='пол', max_length=7, blank=True, choices=type_of_gender, help_text='')

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.surname}'


class Counteragent(models.Model):
    short_name = models.CharField(verbose_name='Наименование', max_length=150, default='', help_text='')
    full_name = models.CharField(verbose_name='Полное наименование', max_length=250, default='', help_text='')
    inn = models.CharField(verbose_name='ИНН', max_length=12, blank=True, null=True, help_text='')
    kpp = models.CharField(verbose_name='КПП', max_length=9, blank=True, null=True, help_text='')
    type_of = [
        ('juridical_person', 'юридическое лицо'),
        ('physical_person', 'физическое лицо'),
        ('separate_subdivision', 'обособленное подразделение'),
        ('government_agency', 'государственный орган'),
    ]
    type_counteragent = models.CharField(verbose_name='Тип контрагента', max_length=40, choices=type_of, help_text='')
    juridical_address = models.ForeignKey(Address, verbose_name='Юридический адрес', on_delete=models.SET_NULL,
                                          null=True, related_name='juridical')
    physical_address = models.ForeignKey(Address, verbose_name='Физический адрес', on_delete=models.SET_NULL, null=True,
                                         related_name='physical')
    email = models.EmailField(verbose_name='Email', null=True)
    phone = models.ForeignKey(PhoneNumber, verbose_name='Номер телефона', on_delete=models.SET_NULL, null=True)
    base_counteragent = models.BooleanField(verbose_name='Основная организация', default=False)
    director = models.ForeignKey(Person, verbose_name='Директор', on_delete=models.SET_NULL, null=True, blank=True,
                                 related_name='direct')
    accountant = models.ForeignKey(Person, verbose_name='Бухгалтер', on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='account')
    contact_person = models.ForeignKey(Person, verbose_name='Контактное лицо', on_delete=models.SET_NULL, null=True,
                                       blank=True, related_name='contact')

    def __str__(self):
        return f'{self.short_name}, {self.inn}/{self.kpp}'
