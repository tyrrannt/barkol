from django.urls import path
import authapp.views as authapp_views

app_name = 'authapp'

urlpatterns = [
    path('login/', authapp_views.login, name='login'),
    path('logout/', authapp_views.logout, name='logout'),
    path('register/', authapp_views.register, name='register'),
    path('profile/<int:pk>/', authapp_views.UserProfile.as_view(), name='profile'),
    path('all/', authapp_views.UserAll.as_view(), name='all_user'),
    path('active/<int:pk>/', authapp_views.UserActive.as_view(), name='active_user'),
    path('remove/<int:pk>/', authapp_views.UserRemove.as_view(), name='remove_user'),
    path('edit/<int:pk>/', authapp_views.UserUpdate.as_view(), name='edit_user'),
]
