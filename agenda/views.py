from django.shortcuts import render
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views import View
from agenda import models




from django.http import HttpResponse



class ListaTarefas(ListView):
    model = models.Tarefa
    template_name = 'agenda/lista_tarefas.html'
    context_object_name = 'tarefas'

class DetalhesTarefa(DetailView):
    model = models.Tarefa
    template_name = 'agenda/detalhe.html'
    context_object_name = 'tarefa'
    slug_url_kwarg = 'pk'