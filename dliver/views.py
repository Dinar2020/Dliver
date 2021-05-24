from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView
from .models import Venda, Produto, EntregaProduto, Cliente, ClientePegueLeve
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
    fields = '__all__'

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

####################### ENTREGA PRODUTO ###################################

class EntregaProdutoCreateView(CreateView):
    model = EntregaProduto
    template_name = 'cadastrar/entrega_produto.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('cadastrar_entrega_produto')


class EntregaProdutoListView(ListView):
    model = EntregaProduto
    template_name = 'listar/entrega_produto.html'
    paginate_by = 5


class EntregaProdutoUpdateView(UpdateView):
    model = EntregaProduto
    template_name = 'atualizar/entrega_produto.html'

    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('listar_entrega_produto')

####################### ENTREGA PRODUTO ###################################

####################### CLIENTE ###################################

class ClienteCreateView(CreateView):
    model = Cliente
    template_name = 'cadastrar/entrega_cliente.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('cadastrar_cliente')


class ClienteListView(ListView):
    model = Cliente
    template_name = 'listar/cliente.html'
    paginate_by = 5


class  ClienteUpdateView(UpdateView):
    model = Cliente
    template_name = 'atualizar/cliente.html'

    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('listar_cliente')

####################### CLIENTE ###################################

####################### CLIENTE PEGUE-LEVE  ###################################

class ClientePegueLeveCreateView(CreateView):
    model = ClientePegueLeve
    template_name = 'cadastrar/clientepegueleve.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('cadastrar_clientepegueleve')


class ClientePegueLeveListView(ListView):
    model = ClientePegueLeve
    template_name = 'listar/clientepegueleve.html'
    paginate_by = 5


class ClientePegueLeveUpdateView(UpdateView):
    model = ClientePegueLeve
    template_name = 'atualizar/clientepegueleve.html'

    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('listar_clientepegueleve')

####################### CLIENTE PEGUE-LEVE ###################################