# Generated by Django 3.1.7 on 2021-04-25 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dliver', '0021_auto_20210425_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venda',
            name='produtos',
            field=models.ManyToManyField(to='dliver.CategoriasRelacao', verbose_name='Produtos Pedidos'),
        ),
    ]