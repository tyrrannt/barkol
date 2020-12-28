from django.db import models
from libapp.models import Category, AccessLevel


# Create your models here.

class BlogCategory(Category):

    def __init__(self, *args, **kwargs):
        super(BlogCategory, self).__init__(*args, **kwargs)

    def __str__(self):
        return self.name


class Blog(models.Model):
    category = models.ForeignKey(BlogCategory, default=0, on_delete=models.SET_DEFAULT, verbose_name='Категория блога')
    acces_level = models.ForeignKey(AccessLevel, default=0, on_delete=models.SET_DEFAULT, )
    name = models.CharField(verbose_name='Наименование документа', max_length=128)
    cover = models.ImageField(verbose_name='Титульный лист', upload_to='document_cover', blank=True)
    short_desc = models.CharField(verbose_name='Краткое описание', max_length=60, blank=True)
    description = models.TextField(verbose_name='Описание', blank=True)
    doc_file = models.FileField(verbose_name='Файл документа', upload_to='library', blank=True)
    time_publication = models.DateTimeField(verbose_name='дата публикации статьи', auto_now_add=True)

    def __str__(self):
        return f'({self.category.name}) {self.name} {self.time_publication}'
