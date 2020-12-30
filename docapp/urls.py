from django.urls import path
import docapp.views as docapp_views

app_name = 'docapp'

urlpatterns = [
    path('', docapp_views.index, name='index'),
]
