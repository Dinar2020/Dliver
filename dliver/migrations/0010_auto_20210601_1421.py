# Generated by Django 3.1.7 on 2021-06-01 17:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dliver', '0009_auto_20210601_1329'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cadastrofornecedor',
            old_name='nome_empresa',
            new_name='nome',
        ),
        migrations.RenameField(
            model_name='cadastrorestaurante',
            old_name='nome_restaurante',
            new_name='restaurante',
        ),
    ]