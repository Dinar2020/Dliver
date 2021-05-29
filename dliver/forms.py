from django import forms
from .models import *


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