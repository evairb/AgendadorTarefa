from django.contrib import admin
from django.urls import path
from agenda import views


app_name = 'agenda'

urlpatterns = [
    path('', views.ListaTarefas.as_view(), name='tarefa'),
    
]