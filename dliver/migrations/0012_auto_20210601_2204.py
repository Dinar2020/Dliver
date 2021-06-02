# Generated by Django 3.1.7 on 2021-06-02 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dliver', '0011_auto_20210601_1428'),
    ]

    operations = [
        migrations.AddField(
            model_name='cadastroatendente',
            name='excluido',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='cadastrofornecedor',
            name='excluido',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='cadastrorestaurante',
            name='excluido',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='cliente',
            name='excluido',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='entregaproduto',
            name='excluido',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='fazerpedido',
            name='excluido',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='formaspagamento',
            name='excluido',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='produto',
            name='excluido',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='registrocupom',
            name='excluido',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
