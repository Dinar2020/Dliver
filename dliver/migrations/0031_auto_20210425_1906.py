# Generated by Django 3.1.7 on 2021-04-25 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dliver', '0030_auto_20210425_1818'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entregaproduto',
            name='cliente',
        ),
        migrations.AlterField(
            model_name='cliente',
            name='endere',
            field=models.CharField(max_length=20, null=True, verbose_name='Endereço Completo'),
        ),
    ]