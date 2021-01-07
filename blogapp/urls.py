from django.urls import path
import blogapp.views as blogapp_views

app_name = 'blogapp'

urlpatterns = [
    path('', blogapp_views.index, name='index'),
    path('new/', blogapp_views.CreateNewPost.as_view(), name='new_blog'),
]
