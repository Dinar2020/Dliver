from django.db import models
from django import forms


# Create your models here.


class Venda(models.Model):
    nome = models.CharField(max_length=255, null=False, blank=False, verbose_name='Nome da Venda')
    valor = models.DecimalField(max_digits=12, decimal_places=2, null=False, blank=False,
                                verbose_name='Valor total da venda')
    data_hora_venda = models.DateTimeField(auto_now_add=True, blank=True, null=False)
    numero_venda = models.IntegerField(blank=False, null=False, verbose_name='Número da Venda')
    observacao = models.TextField(blank=True, null=True, verbose_name="Observação")
    comprovante_venda = models.FileField(upload_to='comprovante_venda/', verbose_name='Comprovante de Venda')
    venda_concluida = models.BooleanField(blank=False, null=False)
    qtd_itens = models.IntegerField(blank=True, null=False, default=0, verbose_name='Quantidade de Itens Vendidos')
    produtos = models.ManyToManyField('Produto')
    cliente = models.ForeignKey('Cliente', on_delete=models.DO_NOTHING, default=1, verbose_name='Cliente')

    def __str__(self):
        return str(self.pk) + ' - ' + self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=255, blank=False, null=False)
    valor = models.DecimalField(max_digits=6, decimal_places=2, blank=False, null=False)

    def __str__(self):
        return self.nome + '. R$: ' + str(self.valor)


class Cliente(models.Model):
    nome = models.CharField(max_length=255, blank=False, null=False, verbose_name='Nome completo')
    cpf = models.CharField(max_length=11, blank=False, null=False, verbose_name='CPF')
    email_cliente = models.EmailField(blank=True, null=True, verbose_name='E-mail')

    def __str__(self):
        return self.nome


class CadastroAtendente(models.Model):
    nome = models.CharField(max_length=255, null=False, blank=False, verbose_name='Nome do Atendente')
    sobrenome = models.CharField(max_length=255, null=False, blank=False, verbose_name='Sobrenome do Atendente')
    email_atendente = models.EmailField(blank=False, null=True, verbose_name='E-mail Atendente')
    cpf = models.CharField(max_length=11, blank=False, null=False, verbose_name='CPF do Atendente')
    escolha_de_genero = (('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outro'))
    genero = models.CharField(choices=escolha_de_genero, max_length=128 , verbose_name='Gênero')
    possui_comorbidade = models.BooleanField(default=False)
    observacao = models.TextField(blank=True, null=True, verbose_name="Observação Comorbidade")
    telefone = models.CharField(max_length=12, blank=False, null=False, verbose_name='Telefone')
    data_de_nascimento = forms.DateField()
    endereco = models.CharField(max_length=200 , verbose_name='Endereço')
    salvar_foto_perfil = models.FileField(upload_to='foto_atendente/', verbose_name='Foto de Perfil')

    def __str__(self):
        return self.nome
