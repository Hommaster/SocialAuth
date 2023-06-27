from django.urls import path, include

from . import views


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('', include('django.contrib.auth.urls'), name='auth_urls'),
    path('register/', views.registrate, name='register'),
    path('edit/', views.edit, name='edit'),
]
