from django.db import models
from django.contrib.auth.models import User
from django.forms import ValidationError
import re

# Create your models here.
class Estoque(models.Model):
    nome_item = models.CharField(max_length=55)
    quantidade = models.PositiveIntegerField()
    def __str__(self):
        return self.nome_item


class Tarefa(models.Model):
    titulo = models.CharField(max_length=120)
    status = models.CharField(
        default='P',
        max_length=10,
        choices = (
            ('Pendente','Pendente',),
            ('Concluida', 'Concluida'),
            ('Andamento','Andamento',)       
        )
    )
    local = models.CharField(max_length=50)
    
    prioridade = models.CharField(
        default='V',
        max_length=5,
        choices = (
            ('Alta', 'Alta'),
            ('Media','Media',),
            ('Baixa','Baixa',),        
        )
    )
    descricao = models.TextField(null=False, blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_alteracao = models.DateTimeField(auto_now=True)
    criado_por = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True, null=True,
        related_name='created_by'
    )

    realizado_por = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True, null=True,
        related_name='updated_by'
    )
    


class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    data_nascimento = models.DateField()
    funcao = models.CharField(max_length=50)
    nivel_acesso = models.CharField(
    default='V',
    max_length=1,
    choices = (
        ('L', 'Auxiliar de limpeza'),
        ('P','Professora',),
        ('D','Diretor',),        
        ('S','Supervisor',),        
    )
)
    
    def __str__(self):
        if self.usuario.first_name and self.usuario.last_name:
            return f'{self.usuario.first_name} {self.usuario.last_name}'
        return f'{self.usuario}' 
    

    def clean(self):
        error_messages = {}
        # if not valida_cpf(self.cpf):
        #     error_messages['cpf'] = 'Digite um CPF valido'

        # if re.search(r'[^0-9]',self.cep) or len(self.cep) < 8:
        #     error_messages['cep'] = 'Digite um cep valido'

        if error_messages:
            raise ValidationError(error_messages)


    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfis'