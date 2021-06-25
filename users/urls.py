"""Django URL patterns for first"""
from django.urls import path, include
from . import views

app_name = 'users'
urlpatterns = [
    #URL аутентификации
    path('', include('django.contrib.auth.urls')),
    #Страница регистрации
    path('register/', views.register, name='register'),

]
