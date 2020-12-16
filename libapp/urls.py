from django.urls import path
import libapp.views as libapp_views


app_name = 'libapp'

urlpatterns = [
    path('lib/', libapp_views.libs, name='library'),

]
