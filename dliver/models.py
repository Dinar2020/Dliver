from django.db import models



# Create your models here.
# Cadastro Produto;
# Cadastro Fornecedor;
# Entrega Produto;
# Cliente;
# Cliente Pegue Leve.
class Venda(models.Model):
    nome = models.CharField(max_length=255, null=False, blank=False, verbose_name='Nome da Venda')
    valor = models.DecimalField(max_digits=12, decimal_places=2, null=False, blank=False,
                                verbose_name='Valor total da venda')
    data_hora_venda = models.DateTimeField(auto_now_add=False, blank=True, null=False,
                                           verbose_name='Data e Hora da venda')
    numero_venda = models.IntegerField(blank=False, null=False, verbose_name='Número da Venda')
    comprovante_venda = models.FileField(upload_to='comprovante_venda/', verbose_name='Comprovante da Venda')
    venda_concluida = models.BooleanField(blank=False, null=False, default=True)
    qtd_itens = models.IntegerField(blank=True, null=False, default=0, verbose_name='Quantidade de Itens Vendidos')
    descricao_pedido = models.ManyToManyField('FazerPedido', verbose_name='Produtos Pedidos')
    cliente = models.ForeignKey('Cliente', on_delete=models.DO_NOTHING, default=1, verbose_name='Cliente')
    observacao = models.TextField(blank=True, null=True, verbose_name="Observação")
    novo_item = models.IntegerField(blank=False, null=False)
    excluido = models.BooleanField(blank=True, null=False, default=False)

    def __str__(self):
        return str(self.pk) + ' | ' + str(self.nome) + ' | ' + str(self.numero_venda)


class Produto(models.Model):
    nome = models.CharField(max_length=255, blank=False, null=False, verbose_name='Nome')
    valor = models.DecimalField(max_digits=12, decimal_places=2, null=False, blank=False, verbose_name='Valor')
    tamanho = models.CharField(max_length=10, blank=False, null=False, verbose_name='Tamanho')
    fornecedor = models.ForeignKey('CadastroFornecedor', on_delete=models.DO_NOTHING, default=1,
                                   verbose_name='Fornecedor')
    quantidade = models.IntegerField(blank=True, null=False, default=0, verbose_name='Quantidade do produto')
    nacionalidade_do_produto = models.CharField(max_length=10, blank=False, null=False,
                                                verbose_name='Nacionalidade do Produto')
    observacao = models.TextField(blank=True, null=True, verbose_name="Observação")
    excluido = models.BooleanField(blank=True, null=False, default=False)

    def __str__(self):
        return str(self.nome) + '| R$: ' + str(self.valor) + '|' + str(self.tamanho)


class FormasPagamento(models.Model):
    restaurante = models.ForeignKey('CadastroRestaurante', on_delete=models.DO_NOTHING, default=1,
                                    verbose_name='Nome do Restaurante')
    pix = models.CharField(max_length=255, blank=False, null=False, verbose_name='Chave Pix')
    cartoes_de_credito = models.CharField(max_length=255, blank=False, null=False, verbose_name='Cartões de Crédito')
    cartoes_de_debito = models.CharField(max_length=255, blank=False, null=False, verbose_name='Cartões de Débito')
    criptomoeda = models.CharField(max_length=255, blank=False, null=False, verbose_name='Criptomoeda')
    app_pagamento = models.CharField(max_length=255, blank=False, null=False,
                                            verbose_name='Aplicativo de Pagamento')
    app_pontos = models.CharField(max_length=255, blank=False, null=False,
                                  verbose_name='Aplicativo de Pontos')
    excluido = models.BooleanField(blank=True, null=False, default=False)
    # lista = [cartao_de_debito, cartao_de_debito, criptomoeda, aplicativo_pagamento, pontos_pagamento]

    # def get_queryset(self):
    #     queryset = FormasPagamento.objects
    #     for c in range(0, len(self.lista)):
    #         if self.lista[c] is True:
    #             return self.lista
    #         else:
    #             return False
    def __str__(self):
        return str(self.pk) + ' - ' + str(self.nome_restaurante) + ' - ' + str(self.pix) + ' - ' + \
               str(self.cartoes_de_credito) + ' - ' + str(self.cartoes_de_debito) + ' - ' + \
               str(self.criptomoeda) + ' - ' + str(self.app_pagamento) + ' - ' + str(self.app_pontos)

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
    telefone = models.CharField(max_length=15, blank=False, null=False, verbose_name='Telefone')
    data_nascimento = models.DateField(verbose_name='Data de nascimento')
    endereco = models.CharField(max_length=200, verbose_name='Endereço')
    salvar_foto_perfil = models.FileField(upload_to='foto_atendente/', verbose_name='Foto de Perfil')
    excluido = models.BooleanField(blank=True, null=False, default=False)

    def __str__(self):
        return str(self.pk) + ' - ' + str(self.nome)


class CadastroLocalDeEntrega(models.Model):
    FAVORITAR_CHOICES = (('C', 'Casa'), ('T', 'Trabalho'), ('P', 'Pegue e leve'))
    favoritar = models.CharField(choices=FAVORITAR_CHOICES, max_length=128, verbose_name='Favoritar como')
    endereco = models.CharField(max_length=200, verbose_name='Endereço')
    complemento = models.CharField(max_length=100, null=False, blank=True, verbose_name='Complemento')
    cep = models.CharField(max_length=50, null=False, blank=True, verbose_name='CEP')
    bairro = models.CharField(max_length=50, null=False, blank=True, verbose_name='Bairro')
    municipio = models.CharField(max_length=50, null=False, blank=True, verbose_name='Município')
    UF_CHOICES = (('Acre', 'AC'), ('Alagoas', 'AL'), ('Amapá', 'AP'), ('Amazonas', 'AM'), ('Bahia', 'BA'),
                  ('Ceará', 'CE'), ('Distrito Federa', 'DF'), ('Espírito Santo', 'ES'), ('Goiás', 'GO'),
                  ('Maranhão', 'MA'), ('Mato Grosso', 'MT'), ('Mato Grosso do Sul', 'MS'), ('Minas Gerais', 'MG'),
                  ('Pará', 'PA'), ('Paraíba', 'PB'), ('Paraná', 'PR'), ('Pernambuco', 'PE'), ('Piauí', ' PI'),
                  ('Rio de Janeiro', 'RJ'), ('Rio Grande do Norte', 'RN'), ('Rio Grande do Sul', 'RS'),
                  ('Rondônia', 'RO'), ('Roraima', 'RR'), ('Santa Catarina', 'SC'), ('São Paulo', 'SP'),
                  ('Sergipe', ' SE'), ('Tocantins', 'TO'))
    uf = models.CharField(choices=UF_CHOICES, max_length=128, verbose_name='UF', blank=True)


    def __str__(self):
        return str(self.favoritar)


class CadastroRestaurante(models.Model):
    restaurante = models.CharField(max_length=255, null=False, blank=False, verbose_name='Nome do Restaurante')
    endereco = models.CharField(max_length=200, verbose_name='Endereço do Restaurante')
    cnpj = models.CharField(max_length=14, blank=False, null=False, verbose_name='CNPJ')
    email_da_empresa = models.EmailField(blank=False, null=True, verbose_name='E-mail da Empresa')
    CATEGORIA_CHOICES = (('B', 'Bebida'), ('H', 'Hamburguer'), ('Pi', 'Pizza'), ('Pa', 'Passaporte'), ('Pas', 'Pastel'))
    ramo = models.CharField(choices=CATEGORIA_CHOICES, max_length=128, verbose_name='Ramo da empresa', default=5)
    telefone = models.CharField(max_length=15, blank=False, null=True, verbose_name='Telefone')
    observacao = models.TextField(blank=True, null=True, verbose_name="Observação")
    excluido = models.BooleanField(blank=True, null=False, default=False)
    # categoria = models.ManyToManyField('CategoriasRelacao') USAR EM REGISTRO DE PEDIDOS OU VENDAS
    # categorizar_como = (('B', 'Bebida'), ('T', 'Trabalho'))
    # lista_categorias = ['Bebida', 'Hamburgue', 'Pizza', 'Passaporte', 'Pastel']
    # categoria_venda = models.ManyToManyField('Bebida','Hamburgue','Pizza','Passaporte','Pastel'])
    #     return str(self.pk) + ' - ' + self.nome_restaurante

    def __str__(self):
        return str(self.pk) + ' - ' + str(self.nome_restaurante)


class FazerPedido(models.Model):
    nome_cliente = models.ForeignKey('Cliente', on_delete=models.DO_NOTHING, default=1, verbose_name='Nome do cliente')
    bebida = models.ForeignKey('Bebida', on_delete=models.DO_NOTHING, blank=True, null=True,)
    hamburguer = models.ForeignKey('Hamburguer', on_delete=models.DO_NOTHING, blank=True, null=True)
    pizza = models.ForeignKey('Pizza', on_delete=models.DO_NOTHING, blank=True, null=True)
    passaporte = models.ForeignKey('Passaporte', on_delete=models.DO_NOTHING, blank=True, null=True)
    pastel = models.ForeignKey('Pastel', on_delete=models.DO_NOTHING, blank=True, null=True)
    local_de_entrega = models.ForeignKey('CadastroLocalDeEntrega', on_delete=models.DO_NOTHING,
                                         verbose_name='Local de entrega')
    observacao = models.TextField(blank=True, null=True, verbose_name='Observação')
    excluido = models.BooleanField(blank=True, null=False, default=False)

    def __str__(self):
        return str(self.pk) + ' - ' + str(self.bebida) + str(self.hamburguer) + str(self.pizza) + str(self.passaporte) \
               + str(self.pastel)


class CadastroFornecedor(models.Model):
    nome = models.CharField(max_length=255, null=False, blank=False, verbose_name='Nome do Fornecedor')
    endereco = models.CharField(max_length=200, verbose_name='Endereço do Restaurante')
    cep = models.CharField(max_length=50, null=False, blank=False, verbose_name='CEP')
    cnpj = models.CharField(max_length=14, blank=False, null=False, verbose_name='CNPJ')
    ramo_atuacao = models.CharField(max_length=128, verbose_name='Ramo de Atuação')
    email_do_fornecedor = models.EmailField(blank=False, null=True, verbose_name='E-mail do Fornecedor')
    empresa_fornecida = models.ForeignKey('CadastroRestaurante', on_delete=models.DO_NOTHING,
                                          verbose_name='Empresa Fornecida')
    telefone = models.CharField(max_length=15, blank=False, null=False, verbose_name='Telefone')
    observacao = models.TextField(blank=True, null=True, verbose_name="Observação")
    excluido = models.BooleanField(blank=True, null=False, default=False)

    def __str__(self):
        return str(self.nome_empresa)


class EntregaProduto(models.Model):
    numero_entrega = models.IntegerField(blank=False, null=False, verbose_name='Número da entrega', default=False)
    nome_antendente = models.ForeignKey('CadastroAtendente', on_delete=models.DO_NOTHING, default=1,
                                        verbose_name='Atendente')
    nome_cliente = models.ForeignKey('Cliente', on_delete=models.DO_NOTHING, default=1)
    # ('Cliente', on_delete=models.DO_NOTHING, default=1, verbose_name='Cliente')
    # endereco_cliente = models.ForeignKey('Cliente', on_delete=models.DO_NOTHING, default=1)
    descricao_pedido = models.ForeignKey('FazerPedido', on_delete=models.DO_NOTHING, default=1)
    PAGAMENTO_CHOICES = (('ENTREGA', 'ENTREGA'), ('APP', 'APP'))
    momento_pagamento = models.CharField(choices=PAGAMENTO_CHOICES, max_length=128, verbose_name='Local de pagamento', blank=True)
    entrega_concluida = models.BooleanField(blank=True, null=False, default=False)
    observacao = models.TextField(blank=True, null=True, verbose_name="Observação")
    excluido = models.BooleanField(blank=True, null=False, default=False)

    def __str__(self):
        return str(self.pk) + '-' + str(self.numero_entrega)


# GIVANILDO


class Cliente(models.Model):
    nome = models.CharField(max_length=255, blank=False, null=False, verbose_name='Nome completo')
    cpf = models.CharField(max_length=11, blank=False, null=False, verbose_name='CPF')
    endere = models.CharField(max_length=128, blank=False, null=True, verbose_name='Endereço Completo')
    data_nascimento = models.DateField(verbose_name='Data de nascimento')
    cidade = models.CharField(max_length=50, blank=False, null=True, verbose_name='Cidade')
    cep = models.CharField(max_length=8, blank=False, null=True, verbose_name='CEP')
    email_cliente = models.EmailField(blank=False, null=True, verbose_name='E-mail')
    tel = models.CharField(max_length=15, blank=False, null=True, verbose_name='Telefone')
    observacao = models.TextField(blank=True, null=True, verbose_name="Observação")
    excluido = models.BooleanField(blank=True, null=False, default=False)

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
    tamanho = models.CharField(max_length=10, blank=False, null=False)
    valor = models.DecimalField(max_digits=12, decimal_places=2, null=False, blank=False)

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
    data_nascimento = models.DateField(verbose_name='Data de nascimento')
    cpf = models.CharField(max_length=11, blank=False, null=False, verbose_name='CPF')
    endere = models.CharField(max_length=20, blank=False, null=True, verbose_name='Endereço completo')
    cidade = models.CharField(max_length=20, blank=False, null=True, verbose_name='Cidade')
    cep = models.CharField(max_length=20, blank=False, null=True, verbose_name='CEP')
    email_Cliente = models.EmailField(blank=False, null=True, verbose_name='E-mail')
    tel = models.CharField(max_length=15, blank=False, null=True, verbose_name='Telefone')
    observacao = models.TextField(blank=True, null=True, verbose_name="Observação")

    def __str__(self):
        return str(self.nome)


class RegistroCupom(models.Model):
    titulo_cupom = models.CharField(max_length=255, blank=False, null=False, verbose_name='Título do Cupom')
    codigo_promocional = models.CharField(max_length=255, blank=False, null=False, verbose_name='Código Promocional')
    # CATEGORIA_CHOICES = (('A','A'),('A','A'))
    # categoria_cupons = models.ForeignObject(Produto,on_delete=models.DO_NOTHING())
    categoria_produto_cupons = models.CharField(max_length=255, blank=False, null=False,
                                                verbose_name='Categoria de Cupom')
    nome_empresa_cupom = models.ForeignKey('CadastroRestaurante', on_delete=models.DO_NOTHING, default=1,
                                           verbose_name='Cupom da Empresa')
    cliente = models.ForeignKey('Cliente', on_delete=models.DO_NOTHING, default=1)
    validade_cupom = models.DateField(verbose_name='Validade do Cupom')
    parceiro_cupom = models.CharField(max_length=255, blank=False, null=False, verbose_name='Nome do Parceiro')
    link_cupom = models.URLField(verbose_name='Link')
    observacao = models.TextField(blank=True, null=True, verbose_name="Observação")
    excluido = models.BooleanField(blank=True, null=False, default=False)