# Generated by Django 3.1.7 on 2021-04-25 20:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dliver', '0025_entregaproduto'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SolicitacaoRetiradaEstoque',
            new_name='ListaProdutosPedidos',
        ),
        migrations.RenameField(
            model_name='entregaproduto',
            old_name='atendente',
            new_name='antendente',
        ),
        migrations.RenameField(
            model_name='entregaproduto',
            old_name='entrega_concluida',
            new_name='produtos_entregues',
        ),
        migrations.RemoveField(
            model_name='entregaproduto',
            name='bebida',
        ),
        migrations.RemoveField(
            model_name='entregaproduto',
            name='hamburgue',
        ),
        migrations.RemoveField(
            model_name='entregaproduto',
            name='numero_entrega',
        ),
        migrations.RemoveField(
            model_name='entregaproduto',
            name='passaporte',
        ),
        migrations.RemoveField(
            model_name='entregaproduto',
            name='pastel',
        ),
        migrations.RemoveField(
            model_name='entregaproduto',
            name='pizza',
        ),
        migrations.AddField(
            model_name='entregaproduto',
            name='produtos_pedidos_vendas',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='dliver.venda', verbose_name='Produtos Entregues'),
        ),
    ]
