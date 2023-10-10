from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views import View
from agenda import models, forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages

import copy


@method_decorator(login_required, name='dispatch')
class ListaTarefas(ListView):
    
    model = models.Tarefa
    template_name = 'agenda/lista_tarefas.html'
    context_object_name = 'tarefas'


@method_decorator(login_required, name='dispatch')
class DetalhesTarefa(DetailView):
    model = models.Tarefa
    template_name = 'agenda/criar_tarefa.html'
    slug_url_kwarg = 'pk'

    def setup(self, *args, **kwargs):
        super().setup(*args, **kwargs)
        tarefa = get_object_or_404(self.model, pk=self.kwargs['pk'])
        
        self.contexto = {
                'tarefaform': forms.TarefasForms(data= self.request.POST or None, instance=tarefa),
            }
        self.tarefaform = self.contexto['tarefaform']

        self.renderizar = render(self.request, self.template_name, self.contexto)
    
    def get(self, *args, **kwargs):
        return self.renderizar
    
    def post(self, *args, **kwargs):
        if not self.tarefaform.is_valid():
            return self.renderizar
        usuario = self.request.user
        tarefa = self.tarefaform.save(commit=False)
        tarefa.atualizado_por = usuario
        tarefa.save()
        return redirect('agenda:tarefa')
    



class BasePerfil(View):
    template_name = 'agenda/cadastrar.html'

    def setup(self, *args, **kwargs):
        super().setup(*args, **kwargs)
        self.perfil = None

        if self.request.user.is_authenticated:
            self.perfil = models.Perfil.objects.filter(
                usuario=self.request.user
            ).first()
            self.contexto = {
                'userform': forms.UserForm(data= self.request.POST or None, usuario=self.request.user, instance=self.request.user),
                'perfilform': forms.PerfilForm(data = self.request.POST or None, instance=self.perfil)
            }
        else:
            self.contexto = {
                'userform': forms.UserForm(data= self.request.POST or None),
                'perfilform': forms.PerfilForm(data = self.request.POST or None)
                
            }
        self.userform = self.contexto['userform']
        self.perfilform = self.contexto['perfilform']

        self.renderizar = render(self.request, self.template_name, self.contexto)


    def get(self, *args, **kwargs):
        return self.renderizar
    

class Criar(BasePerfil):
    def post(self, *args, **kwargs):
        if not self.userform.is_valid() or not self.perfilform.is_valid():
            return self.renderizar
        
        username = self.userform.cleaned_data.get('username')
        password = self.userform.cleaned_data.get('password')
        email = self.userform.cleaned_data.get('email')
        first_name = self.userform.cleaned_data.get('first_name')
        last_name = self.userform.cleaned_data.get('last_name')
        
        if self.request.user.is_authenticated:
            usuario = get_object_or_404(
                User, username=self.request.user.username)
            
            usuario.username = username
            
            if password:
                usuario.set_password(password)

            usuario.email = email
            usuario.first_name = first_name
            usuario.last_name = last_name
            usuario.save()

            
         
        else:
            usuario = self.userform.save(commit=False)
            usuario.set_password(password)
            usuario.save()


            perfil = self.perfilform.save(commit=False)
            perfil.usuario = usuario
            perfil.save()
    

        if password:
            autentica = authenticate(
                self.request, username=usuario, password=password
            )
    
            if autentica:
                login(self.request, user=usuario)
        return self.renderizar
    

class Login(View):
    template_name = "agenda/login.html"
    def get(self, *args, **kwargs):
        return render(self.request, self.template_name)

    def post(self, *args, **kwargs):  
        self.request.COOKIES.clear()
        username = self.request.POST.get('username')
        password = self.request.POST.get('password')
        
        if not username or not password:
            messages.error(
                self.request,
                'Usuario ou senha invalidos'    
            )
            return redirect('perfil:cadastrar')
       
        usuario = authenticate(self.request, username=username, password=password)
        
        if not usuario:
            messages.error(
                self.request,
                'Usuario ou senha invalidos'    
            )
            return redirect('perfil:criar')
            
        login(self.request, user=usuario)
        messages.success(
            self.request,
            'Voce esta logado'    
        )
        return redirect('agenda:tarefa')
        
        
        

class Logout(View):
    def get(self, *args, **kwargs):        
        logout(args[0])
        return redirect('agenda:login')
    

class CriarTarefa(View):
    template_name = 'agenda/criar_tarefa.html'

    def setup(self, *args, **kwargs):
        super().setup(*args, **kwargs)
        
        self.contexto = {
                'tarefaform': forms.TarefasForms(data= self.request.POST or None),
            }
        self.tarefaform = self.contexto['tarefaform']

        self.renderizar = render(self.request, self.template_name, self.contexto)


    def get(self, *args, **kwargs):
        return self.renderizar
    
    
    def post(self, *args, **kwargs):
        if not self.tarefaform.is_valid():
            return self.renderizar
        usuario = self.request.user
        tarefa = self.tarefaform.save(commit=False)
        tarefa.criado_por = usuario
        tarefa.save()
        return redirect('agenda:tarefa')
    



    