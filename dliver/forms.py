from django import forms
from .models import *


class VendaForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = ['nome', 'valor', 'data_hora_venda', 'numero_venda', 'comprovante_venda', 'venda_concluida',
                  'qtd_itens', 'descricao_pedido', 'cliente', 'observacao', 'novo_item', 'excluido']


class VendaObservacaoForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = ['observacao']


class VendaClienteForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = ['cliente']