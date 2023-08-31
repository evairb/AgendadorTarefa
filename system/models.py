from django.db import models

# Create your models here.
class Estoque(models.Model):
    nome_item = models.CharField(max_length=55)
    quantidade = models.PositiveIntegerField()


    def __str__(self):
        return self.nome_item


class Tarefa(models.Model):
    nome = models.CharField(max_length=120)
    status = models.CharField()