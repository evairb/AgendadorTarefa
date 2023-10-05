from django.contrib import admin
from agenda import models

# Register your models here.
@admin.register(models.Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    list_display = 'titulo', 'criado_por', 'data_criacao', 'status',
    list_display_links = 'titulo',
    search_fields = 'titulo', 'status'
    list_per_page = 10
    ordering = '-id',
   
admin.site.register(models.Perfil)