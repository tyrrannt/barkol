from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.hashers import make_password
from authapp.models import Person


# Create your models here.


class AccessLevel(models.Model):
    level = models.PositiveIntegerField(verbose_name='Уровень доступа', default=0)
    description = models.TextField(verbose_name='Описание категории', blank=True)

    def __str__(self):
        return self.description


class Category(models.Model):
    """Класс Category является родительским классом для таких классов как MainMenu,

            Основное применение - задает общие характеристики дочерним классам

            Attributes
            ----------
            parent_category : ForeignKey
                внешний ключ на себя, служит для организации подкатегорий объекта
            name : str
                содержит название категории
            description : str
                содержит описание категории
            access : ForeignKey
                внешний ключ на модель AccessLevel, служит для определения категории доступа

            Methods
            -------
            __str__(self)
                используется для представления отдельных записей на сайте администрирования
                (и в любом другом месте, где нужно обратиться к экземпляру модели).
        """

    class Meta:
        abstract = True

    parent_category = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(verbose_name='Название категории', max_length=128, unique=True)
    description = models.TextField(verbose_name='Описание категории', blank=True)
    access = models.ForeignKey(AccessLevel, default=0, on_delete=models.SET_DEFAULT, verbose_name='Категория доступа')
    hash_view = models.CharField(max_length=256, blank=True)

    def __str__(self):
        if self.parent_category:
            return f'{self.parent_category}/{self.name}'
        else:
            return self.name

    def save(self, **kwargs):
        some_salt = 'some_salt'
        self.hash_view = make_password(self.name, some_salt)
        super().save(**kwargs)


class MainMenu(Category):
    sequence_number = models.PositiveIntegerField(verbose_name='порядковый номер', default=0)
    url_address = models.CharField(verbose_name='ссылка на страницу', max_length=128, default='index', null=False)

    def __init__(self, *args, **kwargs):
        super(MainMenu, self).__init__(*args, **kwargs)
