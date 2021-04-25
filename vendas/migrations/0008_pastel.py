# Generated by Django 3.1.7 on 2021-04-24 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0007_passaporte'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pastel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sabor', models.CharField(max_length=255)),
                ('quantidade', models.IntegerField()),
                ('valor', models.DecimalField(decimal_places=2, max_digits=12)),
            ],
        ),
    ]
