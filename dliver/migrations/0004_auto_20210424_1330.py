# Generated by Django 3.1.7 on 2021-04-24 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dliver', '0003_auto_20210423_1351'),
    ]

    operations = [
        migrations.CreateModel(
            name='CadastroAtendente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome do Atendente')),
                ('sobrenome', models.CharField(max_length=255, verbose_name='Sobrenome do Atendente')),
                ('email_atendente', models.EmailField(blank=True, max_length=254, null=True, verbose_name='E-mail Atendente')),
                ('cpf', models.CharField(max_length=11, verbose_name='CPF do Atendente')),
                ('genero', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('U', 'Unisex/Parody')], max_length=128)),
                ('possui_comorbidade', models.BooleanField(default=True)),
                ('observacao', models.TextField(blank=True, null=True, verbose_name='Observação')),
                ('telefone', models.CharField(max_length=12, verbose_name='Telefone')),
                ('endereco', models.CharField(max_length=200, verbose_name='Endereço')),
                ('salvar_foto_perfil', models.FileField(upload_to='foto_atendente/', verbose_name='Foto de Perfil')),
            ],
        ),
        migrations.RemoveField(
            model_name='venda',
            name='data_venda',
        ),
        migrations.RemoveField(
            model_name='venda',
            name='exemplo_upload',
        ),
        migrations.RemoveField(
            model_name='venda',
            name='hora_venda',
        ),
    ]