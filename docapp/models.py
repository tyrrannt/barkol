from django.db import models
from libapp.models import Category, AccessLevel
from authapp.models import Person


# Create your models here.


class DocumentCategory(Category):

    def __init__(self, *args, **kwargs):
        super(DocumentCategory, self).__init__(*args, **kwargs)


class Document(models.Model):
    category = models.ForeignKey(DocumentCategory, default=0, on_delete=models.SET_DEFAULT,
                                 verbose_name='Категория документа')
    acces_level = models.ForeignKey(AccessLevel, default=0, on_delete=models.SET_DEFAULT,
                                    verbose_name='Категория доступа')
    name = models.CharField(verbose_name='Наименование документа', max_length=128)
    doc_cover = models.ImageField(verbose_name='Титульный лист', upload_to='document_cover', blank=True)
    short_desc = models.CharField(verbose_name='Краткое описание', max_length=60, blank=True)
    description = models.TextField(verbose_name='Описание', blank=True)
    doc_file = models.FileField(verbose_name='Файл документа', upload_to='library', blank=True)
    author = models.ForeignKey(Person, null=True, on_delete=models.SET_NULL, verbose_name='автор поста', default='')

    def __str__(self):
        return f'{self.name} ({self.category.name})'
