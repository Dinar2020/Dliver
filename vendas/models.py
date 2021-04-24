from django.db import models

# Create your models here.


class Venda(models.Model):
    nome = models.CharField(max_length=255, null=False, blank=False, verbose_name='Nome da Venda')
    valor = models.DecimalField(max_digits=12, decimal_places=2, null=False, blank=False,
                                verbose_name='Valor total da venda')
    data_venda = models.DateField(auto_now_add=True, blank=True, null=False)
    hora_venda = models.TimeField(auto_now_add=True, blank=True, null=False)
    data_hora_venda = models.DateTimeField(auto_now_add=True, blank=True, null=False)
    numero_venda = models.IntegerField(blank=False, null=False, verbose_name='Número da Venda')
    observacao = models.TextField(blank=True, null=True, verbose_name="Observação")
    comprovante_venda = models.FileField(upload_to='comprovante_venda/', verbose_name='Comprovante de Venda')
    exemplo_upload = models.FileField(upload_to='outro_diretorio/', null=True, blank=True)
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

class Bebida(models.Model):
    marca = models.CharField(max_length=255, blank=False, null=False)
    valor = models.DecimalField(max_digits=12, decimal_places=2, null=False, blank=False)
    quant_litro = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return str(self.pk) + ' - ' + self.marca



class Hamburgue(models.Model):
    sabor = models.CharField(max_length=255, blank=False, null=False)
    valor = models.DecimalField(max_digits=12, decimal_places=2, null=False, blank=False)
    quantidade = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return str(self.pk) + ' - ' + self.sabor


class Pizza(models.Model):
    sabor = models.CharField(max_length=255, blank=False, null=False)
    quantidade = models.IntegerField(blank=False, null=False)
    valor = models.DecimalField(max_digits=12, decimal_places=2, null=False, blank=False)


    def __str__(self):
        return str(self.pk) + ' - ' + self.sabor

class Passaporte(models.Model):
    sabor = models.CharField(max_length=255, blank=False, null=False)
    quantidade = models.IntegerField(blank=False, null=False)
    valor = models.DecimalField(max_digits=12, decimal_places=2, null=False, blank=False)


    def __str__(self):
        return str(self.pk) + ' - ' + self.sabor

class Pastel(models.Model):
    sabor = models.CharField(max_length=255, blank=False, null=False)
    quantidade = models.IntegerField(blank=False, null=False)
    valor = models.DecimalField(max_digits=12, decimal_places=2, null=False, blank=False)


    def __str__(self):
        return str(self.pk) + ' - ' + self.sabor
