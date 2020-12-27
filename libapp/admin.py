from django.contrib import admin
from libapp.models import Document, AccessLevel, MainMenu, BlogCategory, Blog

admin.site.register(Document)
admin.site.register(AccessLevel)
admin.site.register(MainMenu)
admin.site.register(BlogCategory)
admin.site.register(Blog)
