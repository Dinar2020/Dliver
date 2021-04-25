from django.db import models
from django import forms


# Create your models here.
print("teste)")


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
    produtos_pedidos = models.ManyToManyField('SolicitacaoRetiradaEstoque', verbose_name='Produtos Pedidos')
    cliente = models.ForeignKey('Cliente', on_delete=models.DO_NOTHING, default=1, verbose_name='Cliente')

    def __str__(self):
        return str(self.pk) + ' - ' + self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=255, blank=False, null=False)
    valor = models.DecimalField(max_digits=6, decimal_places=2, blank=False, null=False)

    def __str__(self):
        return self.nome + '. R$: ' + str(self.valor)
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
        return self.nome


class CadastroLocalDeEntrega(models.Model):
    FAVORITAR_CHOICES = (('C', 'Casa'), ('T', 'Trabalho'))
    favoritar = models.CharField(choices=FAVORITAR_CHOICES, max_length=128, verbose_name='Favoritar como')
    endereco = models.CharField(max_length=200, verbose_name='Endereço')
    complemento = models.CharField(max_length=100, null=False, blank=False, verbose_name='Complemento')
    cep = models.CharField(max_length=50, null=False, blank=False, verbose_name='CEP')
    bairro = models.CharField(max_length=50, null=False, blank=False, verbose_name='Bairro')
    municipio = models.CharField(max_length=50, null=False, blank=False, verbose_name='Município')
    UF_CHOICES = (('Acre', 'AC'), ('Alagoas', 'AL'), ('Amapá', 'AP'), ('Amazonas', 'AM'), ('Bahia', 'BA'),
                  ('Ceará', 'CE'), ('Distrito Federa', 'DF'), ('Espírito Santo', 'ES'), ('Goiás', 'GO'),
                  ('Maranhão', 'MA'), ('Mato Grosso', 'MT'), ('Mato Grosso do Sul', 'MS'), ('Minas Gerais', 'MG'),
                  ('Pará', 'PA'), ('Paraíba', 'PB'), ('Paraná', 'PR'), ('Pernambuco', 'PE'), ('Piauí', ' PI'),
                  ('Rio de Janeiro', 'RJ'), ('Rio Grande do Norte', 'RN'), ('Rio Grande do Sul', 'RS'),
                  ('Rondônia', 'RO'), ('Roraima', 'RR'), ('Santa Catarina', 'SC'), ('São Paulo', 'SP'),
                  ('Sergipe', ' SE'), ('Tocantins', 'TO'))
    uf = models.CharField(choices=UF_CHOICES, max_length=128, verbose_name='UF')

    def __str__(self):
        return self.favoritar


class CadastroRestaurante(models.Model):
    nome_restaurante = models.CharField(max_length=255, null=False, blank=False, verbose_name='Nome do Restaurante')
    endereco = models.CharField(max_length=200, verbose_name='Endereço do Restaurante')
    cnpj = models.CharField(max_length=14, blank=False, null=False, verbose_name='CNPJ')
    email_da_empresa = models.EmailField(blank=False, null=True, verbose_name='E-mail da Empresa')
    CATEGORIA_CHOICES = (('B', 'Bebida'),('H','Hamburgue'),('Pi','Pizza') ,('Pa','Passaporte'),('Pas','Pastel'))
    ramo= models.CharField(choices=CATEGORIA_CHOICES,max_length=128, verbose_name='Ramo da empresa',default=5)

    # categoria = models.ManyToManyField('CategoriasRelacao') USAR EM REGISTRO DE PEDIDOS OU VENDAS
    # categorizar_como = (('B', 'Bebida'), ('T', 'Trabalho'))
    # lista_categorias = ['Bebida', 'Hamburgue', 'Pizza', 'Passaporte', 'Pastel']
    # categoria_venda = models.ManyToManyField('Bebida','Hamburgue','Pizza','Passaporte','Pastel'])
    #     return str(self.pk) + ' - ' + self.nome_restaurante

    def __str__(self):
        return str(self.pk) + ' - ' + self.nome_restaurante


class SolicitacaoRetiradaEstoque(models.Model):
    bebida = models.ForeignKey('Bebida', on_delete=models.DO_NOTHING, blank=True, null=True)
    hamburgue = models.ForeignKey('Hamburgue', on_delete=models.DO_NOTHING, blank=True, null=True)
    pizza = models.ForeignKey('Pizza', on_delete=models.DO_NOTHING, blank=True, null=True)
    passaporte = models.ForeignKey('Passaporte', on_delete=models.DO_NOTHING, blank=True, null=True)
    pastel = models.ForeignKey('Pastel', on_delete=models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return str(self.pk) + '-' + str(self.bebida) or str(self.hamburgue) or str(self.pizza) or str(self.passaporte)\
               or str(self.pastel)

# class Cardapio(models.Model):
# GIVANILDO


class Cliente(models.Model):
    nome = models.CharField(max_length=255, blank=False, null=False, verbose_name='Nome completo')
    cpf = models.CharField(max_length=11, blank=False, null=False, verbose_name='CPF')
    endere = models.CharField(max_length=20, blank=False, null=True, verbose_name='Endereço completo')
    cidade = models.CharField(max_length=20, blank=False, null=True, verbose_name='Cidade')
    cep = models.CharField(max_length=20, blank=False, null=True, verbose_name='CEP')
    email_Cliente = models.EmailField(blank=False, null=True, verbose_name='E-mail')
    tel = models.CharField(max_length=12, blank=False, null=True, verbose_name='Telefone')

    def __str__(self):
        return self.nome


class Bebida(models.Model):
    marca = models.CharField(max_length=255, blank=False, null=False)
    valor = models.DecimalField(max_digits=12, decimal_places=2, null=False, blank=False)
    tamanho = models.CharField(max_length=10, blank=False, null=False)

    def __str__(self):
        return str(self.pk) + ' - ' + str(self.marca) + '  R$: ' + str(self.valor) + '  ' + str(self.tamanho)


class Hamburgue(models.Model):
    sabor = models.CharField(max_length=255, blank=False, null=False)
    valor = models.DecimalField(max_digits=12, decimal_places=2, null=False, blank=False)
    tamanho = models.CharField(max_length=10, blank=False, null=False)

    def __str__(self):
        return str(self.pk) + ' - ' + str(self.sabor) + '  R$: ' + str(self.valor) + '  ' + str(self.tamanho)


class Pizza(models.Model):
    sabor = models.CharField(max_length=255, blank=False, null=False)
    tamanho = models.CharField(max_length=10, blank=False, null=False)
    valor = models.DecimalField(max_digits=12, decimal_places=2, null=False, blank=False)

    def __str__(self):
        return str(self.pk) + ' - ' + str(self.sabor) + '  R$: ' + str(self.valor) + '  ' + str(self.tamanho)


class Passaporte(models.Model):
    sabor = models.CharField(max_length=255, blank=False, null=False)
    tamanho = models.CharField(max_length=10, blank=False, null=False)
    valor = models.DecimalField(max_digits=12, decimal_places=2, null=False, blank=False)

    def __str__(self):
        return str(self.pk) + ' - ' + str(self.sabor) + '  R$: ' + str(self.valor) + '  ' + str(self.tamanho)


class Pastel(models.Model):
    sabor = models.CharField(max_length=255, blank=False, null=False)
    tamanho = models.CharField(max_length=10, blank=False, null=False)
    valor = models.DecimalField(max_digits=12, decimal_places=2, null=False, blank=False)

    def __str__(self):
        return str(self.pk) + ' - ' + str(self.sabor) + '  R$: ' + str(self.valor) + '  ' + str(self.tamanho)


class ClientePegueLeve(models.Model):
    nome = models.CharField(max_length=255, blank=False, null=False, verbose_name='Nome completo')
    cpf = models.CharField(max_length=11, blank=False, null=False, verbose_name='CPF')
    endere = models.CharField(max_length=20, blank=False, null=True, verbose_name='Endereço completo')
    cidade = models.CharField(max_length=20, blank=False, null=True, verbose_name='Cidade')
    cep = models.CharField(max_length=20, blank=False, null=True, verbose_name='CEP')
    email_Cliente = models.EmailField(blank=False, null=True, verbose_name='E-mail')
    tel = models.CharField(max_length=12, blank=False, null=True, verbose_name='Telefone')

    def __str__(self):
        return self.nome
