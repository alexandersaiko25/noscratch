"""Django URL patterns for first"""
from django.urls import path
from . import views


app_name = 'first'

urlpatterns = [
    #Главная страница
    path('', views.index, name='index'),
    #Страница, показывает все темы
    path('topics/', views.topics, name='topics'),
    #Страница показывает одну тему
    path('topics/<int:topic_id>/', views.topic, name="topic"),
    #Страница для добавления новой темы
    path('new_topic/', views.new_topic, name='new_topic'),
    #Страница для добавления новой записи
    path('new_entry/<int:topic_id>/', views.new_entry, name="new_entry"),
    #Страница для редактирования записи
    path('edit_entry/<int:entry_id>/', views.edit_entry, name="edit_entry"),

]
