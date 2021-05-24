from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView
from .models import Venda, Produto
from django.urls import reverse_lazy

# Create your views here.

######################## VENDA ####################################

class VendaCreateView(CreateView):
    model = Venda
    template_name = 'cadastrar/venda.html'

    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy("listar_venda")


class VendaListView(ListView):
    model = Venda
    template_name = 'listar/venda.html'
    paginate_by = 5


class VendaUpdateView(UpdateView):
    model = Venda
    template_name = 'atualizar/venda.html'

    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('listar_venda')

######################## VENDA ####################################


####################### PRODUTO ###################################

class ProdutoCreateView(CreateView):
    model = Produto
    template_name = 'cadastrar/produto.html'
    # Caso eu queira que sejam cadastrados todos os fields do meu Model você colocará o fields = '__all__'
    # Caso queira especificar, colocar da forma abaixo. Por exemplo, se quiser apenas nome colocar fields = ['nome']
    fields = ['nome', 'valor']

    def get_success_url(self):
        return reverse_lazy('cadastrar_produto')


class ProdutoListView(ListView):
    model = Produto
    template_name = 'listar/produto.html'
    paginate_by = 5


class ProdutoUpdateView(UpdateView):
    model = Produto
    template_name = 'atualizar/produto.html'

    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('listar_produto')

####################### PRODUTO ###################################