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
    produtos_pedidos = models.ManyToManyField('SolicitacaoProduto', verbose_name='Produtos Pedidos')
    cliente = models.ForeignKey('Cliente', on_delete=models.DO_NOTHING, default=1, verbose_name='Cliente')

    def __str__(self):
        return str(self.pk) + ' | ' + self.nome + ' | ' + str(self.numero_venda)


class Produto(models.Model):
    nome = models.CharField(max_length=255, blank=False, null=False)
    valor = models.DecimalField(max_digits=12, decimal_places=2, null=False, blank=False)
    tamanho = models.CharField(max_length=10, blank=False, null=False)
    fornecedor = models.CharField(max_length=10, blank=False, null=False)
    quantidade = models.CharField(max_length=10, blank=False, null=False)
    nacionalidade_do_produto = models.CharField(max_length=10, blank=False, null=False)
    observacao = models.CharField(max_length=10, blank=False, null=False)


    def __str__(self):
        return self.nome + '| R$: ' + str(self.valor) + '|' + str(self.tamanho)


class FormasPagamento(models.Model):
    nome_restaurante = models.ForeignKey('CadastroRestaurante', on_delete=models.DO_NOTHING, default=1,
                                         verbose_name='Nome do Restaurante')
    pix = models.BooleanField(blank=False, null=False)
    cartaodecredito = models.BooleanField(blank=False, null=False)
    criptomoeda = models.BooleanField(blank=False, null=False)
    aplicativo_pagamento = models.BooleanField(blank=False, null=False)
    pontos_pagamento= models.BooleanField(blank=False, null=False)

    def __str__(self):
        return str(self.pk) + ' | ' + self.nome_restaurante
    # apagar depois de feito a classe Categoria


class CadastroAtendente(models.Model):
    nome = models.CharField(max_length=255, null=False, blank=False, verbose_name='Nome do Atendente')
    sobrenome = models.CharField(max_length=255, null=False, blank=False, verbose_name='Sobrenome do Atendente')
    email_atendente = models.EmailField(blank=False, null=True, verbose_name='E-mail Atendente')
    cpf = models.CharField(max_length=11, blank=False, null=False, verbose_name='CPF do Atendente')
    GENERO_CHOICES = (('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outro'))
    genero = models.CharField(choices=GENERO_CHOICES, max_length=128, verbose_name='Gênero')
    possui_comorbidade = models.BooleanField(default=False)
    observacao = models.TextField(blank=True, null=True, verbose_name="Observação Comorbidade")
    telefone = models.CharField(max_length=12, blank=False, null=False, verbose_name='Telefone')
    data_de_nascimento = forms.DateField()
    endereco = models.CharField(max_length=200, verbose_name='Endereço')
    salvar_foto_perfil = models.FileField(upload_to='foto_atendente/', verbose_name='Foto de Perfil')

    def __str__(self):
        return str(self.pk) + ' | ' + self.nome



class CadastroRestaurante(models.Model):
    nome_restaurante = models.CharField(max_length=255, null=False, blank=False, verbose_name='Nome do Restaurante')
    endereco = models.CharField(max_length=200, verbose_name='Endereço do Restaurante')
    cnpj = models.CharField(max_length=14, blank=False, null=False, verbose_name='CNPJ')
    email_da_empresa = models.EmailField(blank=False, null=True, verbose_name='E-mail da Empresa')
    CATEGORIA_CHOICES = (('B', 'Bebida'), ('H', 'Hamburguer'), ('Pi', 'Pizza') , ('Pa', 'Passaporte'), ('Pas', 'Pastel'))
    ramo = models.CharField(choices=CATEGORIA_CHOICES, max_length=128, verbose_name='Ramo da empresa', default=5)
    telefone = models.CharField(max_length=12, blank=False, null=False, verbose_name='Telefone')
    observacao = models.TextField(blank=True, null=True, verbose_name="Observação Comorbidade")


    def __str__(self):
        return str(self.pk) + ' | ' + self.nome_restaurante


class SolicitacaoProduto(models.Model):
    bebida = models.ForeignKey('Bebida', on_delete=models.DO_NOTHING, blank=True, null=True, )
    hamburguer = models.ForeignKey('Hamburguer', on_delete=models.DO_NOTHING, blank=True, null=True)
    pizza = models.ForeignKey('Pizza', on_delete=models.DO_NOTHING, blank=True, null=True)
    passaporte = models.ForeignKey('Passaporte', on_delete=models.DO_NOTHING, blank=True, null=True)
    pastel = models.ForeignKey('Pastel', on_delete=models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return str(self.pk) + '|' + str(self.bebida) + str(self.hamburguer) + str(self.pizza) + str(self.passaporte) \
               + str(self.pastel)


class EntregaProduto(models.Model):
    numero_entrega = models.IntegerField(blank=False, null=False, verbose_name='Número da entrega', default=False)
    nome_antendente = models.ForeignKey('CadastroAtendente', on_delete=models.DO_NOTHING, default=1,verbose_name='Atendente')
    nome_cliente = models.ForeignKey('Cliente', on_delete=models.DO_NOTHING,default=1)
    produtos_pedidos_vendas = models.ForeignKey('Venda', on_delete=models.DO_NOTHING, default=1,verbose_name='Confirmação de Entrega')
    produtos_entregues = models.BooleanField(blank=False, null=False,default=False)
    pagamento_na_entrega = models.BooleanField(blank=False, null=False, default=False)
    entrega_concluida = models.BooleanField(blank=False, null=False)
    observacao = models.TextField(blank=True, null=True, verbose_name="Observação")

    def __str__(self):
        return str(self.pk) + '-' + self.numero_entrega

# GIVANILDO


class Cliente(models.Model):
    nome = models.CharField(max_length=255, blank=False, null=False, verbose_name='Nome completo')
    cpf = models.CharField(max_length=11, blank=False, null=False, verbose_name='CPF')
    endere = models.CharField(max_length=128, blank=False, null=True, verbose_name='Endereço Completo')
    data_de_nascimento = forms.DateField()
    cidade = models.CharField(max_length=50, blank=False, null=True, verbose_name='Cidade')
    cep = models.CharField(max_length=8, blank=False, null=True, verbose_name='CEP')
    email_Cliente = models.EmailField(blank=False, null=True, verbose_name='E-mail')
    tel = models.CharField(max_length=12, blank=False, null=True, verbose_name='Telefone')
    observacao = models.TextField(blank=True, null=True, verbose_name="Observação")

    def __str__(self):
        return str(self.pk) + '- ' + str(self.nome)


class Bebida(models.Model):
    marca = models.CharField(max_length=255, blank=False, null=False)
    valor = models.DecimalField(max_digits=12, decimal_places=2, null=False, blank=False)
    tamanho = models.CharField(max_length=10, blank=False, null=False)

    def __str__(self):
        return str(self.pk) + ' | ' + str(self.marca) + ' | R$: ' + str(self.valor) + ' | ' + str(self.tamanho)


class Hamburguer(models.Model):
    sabor = models.CharField(max_length=255, blank=False, null=False)
    valor = models.DecimalField(max_digits=12, decimal_places=2, null=False, blank=False)
    tamanho = models.CharField(max_length=10, blank=False, null=False)

    def __str__(self):
        return str(self.pk) + ' | ' + str(self.sabor) + ' | R$: ' + str(self.valor) + ' | ' + str(self.tamanho)


class Pizza(models.Model):
    sabor = models.CharField(max_length=255, blank=False, null=False)
    tamanho = models.CharField(max_length=10, blank=False, null=False)
    valor = models.DecimalField(max_digits=12, decimal_places=2, null=False, blank=False)

    def __str__(self):
        return str(self.pk) + ' | ' + str(self.sabor) + ' | R$: ' + str(self.valor) + ' | ' + str(self.tamanho)


class Passaporte(models.Model):
    sabor = models.CharField(max_length=255, blank=False, null=False)
    tamanho = models.CharField(max_length=10, blank=False, null=False)
    valor = models.DecimalField(max_digits=12, decimal_places=2, null=False, blank=False)

    def __str__(self):
        return str(self.pk) + ' | ' + str(self.sabor) + ' | R$: ' + str(self.valor) + ' | ' + str(self.tamanho)


class Pastel(models.Model):
    sabor = models.CharField(max_length=255, blank=False, null=False)
    tamanho = models.CharField(max_length=10, blank=False, null=False)
    valor = models.DecimalField(max_digits=12, decimal_places=2, null=False, blank=False)

    def __str__(self):
        return str(self.pk) + ' | ' + str(self.sabor) + ' | R$: ' + str(self.valor) + ' | ' + str(self.tamanho)


class ClientePegueLeve(models.Model):
    nome = models.CharField(max_length=255, blank=False, null=False, verbose_name='Nome completo')
    data_de_nascimento = forms.DateField()
    cpf = models.CharField(max_length=11, blank=False, null=False, verbose_name='CPF')
    endere = models.CharField(max_length=20, blank=False, null=True, verbose_name='Endereço completo')
    cidade = models.CharField(max_length=20, blank=False, null=True, verbose_name='Cidade')
    cep = models.CharField(max_length=20, blank=False, null=True, verbose_name='CEP')
    email_Cliente = models.EmailField(blank=False, null=True, verbose_name='E-mail')
    tel = models.CharField(max_length=12, blank=False, null=True, verbose_name='Telefone')
    observacao = models.TextField(blank=True, null=True, verbose_name="Observação")

    def __str__(self):
        return str(self.nome)

class Fornecedor(models.Model):
    nome_empresa = models.CharField(max_length=255, blank=False, null=False, verbose_name='Nome completo')
    endere =  models.CharField(max_length=20, blank=False, null=True, verbose_name='Endereço completo')
    cep = models.CharField(max_length=20, blank=False, null=False, verbose_name='CEP')
    cnpj = models.CharField(max_length=20, blank=False, null=False, verbose_name='CNPJ')
    ramo_atuacao = models.CharField(max_length=255, blank=False, null=False, verbose_name='Ramo de Atuação')
    email_empresa = models.EmailField(blank=False, null=True, verbose_name='E-mail')
    categoria_CHOICE = (('B', 'Bebida'), ('H', 'Hamburguer'), ('Pi', 'Pizza') , ('Pa', 'Passaporte'), ('Pas', 'Pastel'))
    telefone = models.CharField(max_length=12, blank=False, null=True, verbose_name='Telefone')
    Observacao = models.TextField(blank=True, null=True, verbose_name='Observação')

    def __str__(self):
        return str(self.nome_empresa)

class Faq(models.Model):
    nome = models.CharField(max_length=255, blank=False, null=False, verbose_name='Nome completo')
    duvida = models.TextField(blank=True, null=True, verbose_name='Duvida')
    email = models.EmailField(blank=False, null=True, verbose_name='E-mail')

    def __str__(self):
        return str(self.nome)