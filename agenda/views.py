from django.shortcuts import render
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from agenda import models




from django.http import HttpResponse



class ListaTarefas(ListView):
    model = models.Tarefa
    template_name = 'system/lista_tarefas.html'
    context_object_name = 'tarefas'