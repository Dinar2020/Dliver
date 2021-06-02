from django import forms
from .models import *

# VENDA
class VendaForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = '__all__'


class VendaObservacaoForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = ['observacao']


class VendaClienteForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = ['cliente']

# VENDA


# PRODUTO
class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'


class ProdutoNacionalidadeForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nacionalidade_do_produto']


class ProdutoNomeForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome']

#PRODUTO

# ENTREGA

class EntregaProdutoForm(forms.ModelForm):
    class Meta:
        model = EntregaProduto
        fields = '__all__'


class EntregaProdutoClienteForm(forms.ModelForm):
    class Meta:
        model = EntregaProduto
        fields = ['nome_cliente']


class EntregaProdutoEntregaConcluidaForm(forms.ModelForm):
    class Meta:
        model = EntregaProduto
        fields = ['entrega_concluida']

# ENTREGA

#CLIENTE


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'


class ClienteNomeForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome']


class ClienteTelForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['tel']

#CLIENTE

# FORNECEDOR

class FornecedorForm(forms.ModelForm):
    class Meta:
        model = CadastroFornecedor
        fields = '__all__'


class FornecedorEmpresaFornecidaForm(forms.ModelForm):
    class Meta:
        model = CadastroFornecedor
        fields = ['empresa_fornecida']


class FornecedorNomeForm(forms.ModelForm):
    class Meta:
        model = CadastroFornecedor
        fields = ['nome']



# FORNECEDOR

# FORMASPAGAMENTO

class FormasPagamentoForm(forms.ModelForm):
    class Meta:
        model = FormasPagamento
        fields = '__all__'


class FormasPagamentoAppPagamentoForm(forms.ModelForm):
    class Meta:
        model = FormasPagamento
        fields = ['app_pagamento']


class FormasPagamentoNomeForm(forms.ModelForm):
    class Meta:
        model = FormasPagamento
        fields = ['restaurante']

# FORMASPAGAMENTO

# CADASTROATENDENTE

class AtendenteForm(forms.ModelForm):
    class Meta:
        model = CadastroAtendente
        fields = '__all__'


class AtendenteEnderecoForm(forms.ModelForm):
    class Meta:
        model = CadastroAtendente
        fields = ['endereco']


class AtendenteFotoForm(forms.ModelForm):
    class Meta:
        model = CadastroAtendente
        fields = ['salvar_foto_perfil']


# CADASTROATENDENTE

# REGISTROCUPOM

class RegistroCupomForm(forms.ModelForm):
    class Meta:
        model = RegistroCupom
        fields = '__all__'


class RegistroCupomClienteForm(forms.ModelForm):
    class Meta:
        model = RegistroCupom
        fields = ['cliente']


class RegistroCupomValidadeForm(forms.ModelForm):
    class Meta:
        model = RegistroCupom
        fields = ['validade_cupom']

# REGISTROCUPOM

# CADASTRORESTAURANTE

class CadastroRestauranteForm(forms.ModelForm):
    class Meta:
        model = CadastroRestaurante
        fields = '__all__'


class CadastroRestauranteObservacaoClienteForm(forms.ModelForm):
    class Meta:
        model = CadastroRestaurante
        fields = ['observacao']


class CadastroRestauranteTelefoneForm(forms.ModelForm):
    class Meta:
        model = CadastroRestaurante
        fields = ['telefone']


# CADASTRORESTAURANTE

# FAZERPEDIDO

class FazerPedidoForm(forms.ModelForm):
    class Meta:
        model = FazerPedido
        fields = '__all__'


class FazerPedidoLocalDeEntregaForm(forms.ModelForm):
    class Meta:
        model = FazerPedido
        fields = ['local_de_entrega']


class FazerPedidoNomeClienteForm(forms.ModelForm):
    class Meta:
        model = FazerPedido
        fields = ['nome_cliente']


# FAZERPEDIDO