# Generated by Django 3.1.7 on 2021-06-01 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dliver', '0010_auto_20210601_1421'),
    ]

    operations = [
        migrations.RenameField(
            model_name='formaspagamento',
            old_name='nome_restaurante',
            new_name='restaurante',
        ),
    ]
