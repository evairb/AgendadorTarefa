# Generated by Django 4.2.4 on 2023-10-04 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0003_rename_nome_tarefa_titulo'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarefa',
            name='descricao',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='tarefa',
            name='local',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
