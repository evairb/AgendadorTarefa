from django.contrib import admin
from django.urls import path
from agenda import views


app_name = 'agenda'

urlpatterns = [
    
    path('lista/', views.ListaTarefas.as_view(), name='tarefa'),
    path('detalhe/<pk>', views.DetalhesTarefa.as_view(), name='detalhe'),
    path('cadastrar/', views.Criar.as_view(), name='cadastrar'),
    path('login/', views.Login.as_view(), name='login'),
    path('criarTarefa/', views.CriarTarefa.as_view(), name='criarTarefa'),
    
    
]