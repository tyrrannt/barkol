from django.db import models

# Create your models here.


class Access_document(models.Model):
    level = models.PositiveIntegerField(
        verbose_name='Уровень доступа',
        default=0
    )
    description = models.TextField(
        verbose_name='Описание категории',
        blank=True
    )

    def __str__(self):
        return self.description


class Category(models.Model):
    name = models.CharField(
        verbose_name='Название категории',
        max_length=128,
        unique=True
    )
    description = models.TextField(
        verbose_name='Описание категории',
        blank=True
    )
    access = models.CharField(
        verbose_name='Категория доступа',
        max_length=10,
        unique=True
    )

    def __str__(self):
        return self.name


class Document(models.Model):
    category = models.ForeignKey(
        Category,
        default=0,
        on_delete=models.SET_DEFAULT,
    )
    acces_level = models.ForeignKey(
        Access_document,
        default=0,
        on_delete=models.SET_DEFAULT,
    )
    name = models.CharField(
        verbose_name='Наименование документа',
        max_length=128
    )
    doc_cover = models.ImageField(
        verbose_name='Титульный лист',
        upload_to='document_cover',
        blank=True
    )
    short_desc = models.CharField(
        verbose_name='Краткое описание',
        max_length=60,
        blank=True
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=True
    )
    doc_file = models.FileField(
        verbose_name='Файл документа',
        upload_to='library',
        blank=True
    )

    def __str__(self):
        return f'{self.name} ({self.category.name})'
