# Generated by Django 3.1.7 on 2021-04-25 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0015_auto_20210424_2315'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cadastrorestaurante',
            name='categoria_venda',
        ),
    ]
