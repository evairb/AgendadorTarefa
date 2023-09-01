from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Estoque(models.Model):
    nome_item = models.CharField(max_length=55)
    quantidade = models.PositiveIntegerField()


    def __str__(self):
        return self.nome_item


class Tarefa(models.Model):
    nome = models.CharField(max_length=120)
    status = models.CharField(
        default='P',
        max_length=1,
        choices = (
            ('C', 'Concluida'),
            ('A','Andamento',),
            ('P','Pendente',),        
        )
    )
    prioridade = models.CharField(
        default='V',
        max_length=1,
        choices = (
            ('A', 'Alta'),
            ('M','Media',),
            ('B','Baixa',),        
        )
    )
    
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
    