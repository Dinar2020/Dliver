# Generated by Django 3.1.7 on 2021-04-26 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0032_auto_20210425_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='cidade',
            field=models.CharField(max_length=50, null=True, verbose_name='Cidade'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='endere',
            field=models.CharField(max_length=128, null=True, verbose_name='Endereço Completo'),
        ),
    ]
