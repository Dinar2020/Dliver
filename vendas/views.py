from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView
from .models import Venda, Produto, Bebida, Hamburgue, Pizza, Passaporte, Pastel, Cliente, ClientePegueLeve
from django.urls import reverse_lazy
# Create your views here.

#################  CLASSE CADASTRO VENDA:   ####################

class VendaCreateView(CreateView):
    model = Venda
    template_name = 'cadastrar/venda.html'

    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy("listar_venda")


class VendaListView(ListView):
    model = Venda
    template_name = 'listar/venda.html'
    paginate_by = 3


class VendaUpdateView(UpdateView):
    model = Venda
    template_name = 'atualizar/venda.html'

    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('listar_venda')

#################  CLASSE CADASTRO VENDA:   ####################


#################  CLASSE CADASTRO CLIENTE:   ####################

class ClienteCreateView(CreateView):
    model = Cliente
    template_name = 'cadastrar/cliente.html'

    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy("listar_cliente")


class ClienteListView(ListView):
    model = Cliente
    template_name = 'listar/cliente.html'
    paginate_by = 3


class ClienteUpdateView(UpdateView):
    model = Cliente
    template_name = 'atualizar/cliente.html'

    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('listar_cliente')


#################  CLASSE CADASTRO CLIENTE:   ####################


#################  CLASSE CADASTRO PRODUTO:   ####################

class ProdutoCreateView(CreateView):
    model = Produto
    template_name = 'cadastrar/produto.html'

    # Caso eu queira que sejam cadastrados todos os fields do meu Model você colocará o fields = '__all__'
    # Caso queira especificar, colocar da forma abaixo. Por exemplo, se quiser apenas nome colocar fields = ['nome']
    fields = ['nome', 'valor']

    def get_success_url(self):
        return reverse_lazy('cadastrar_produto')

#################  CLASSE CADASTRO PRODUTO:   ####################


#################  CLASSE CADASTRO BEBIDA:   ####################

class BebidaCreateView(CreateView):
    model = Bebida
    template_name = 'cadastrar/bebida.html'

    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy("listar_bebida")


class BebidaListView(ListView):
    model = Bebida
    template_name = 'listar/bebida.html'
    paginate_by = 3


class BebidaUpdateView(UpdateView):
    model = Bebida
    template_name = 'atualizar/bebida.html'

    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('listar_bebida')

#################  CLASSE CADASTRO BEBIDA   ####################


#################  CLASSE CADASTRO HAMBURGUER   ####################

class HamburgueCreateView(CreateView):
    model = Hamburgue
    template_name = 'cadastrar/hamburgue.html'

    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy("listar_humburgue")


class HamburgueListView(ListView):
    model = Hamburgue
    template_name = 'listar/hamburgue.html'
    paginate_by = 3


class HamburgueUpdateView(UpdateView):
    model = Hamburgue
    template_name = 'atualizar/hamburgue.html'

    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('listar_hamburgue')

#################  CLASSE CADASTRO HAMBURGUER   ####################

#################  CLASSE CADASTRO PIZZA:   ####################

class PizzaCreateView(CreateView):
    model = Pizza
    template_name = 'cadastrar/pizza.html'

    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy("listar_pizza")


class PizzaListView(ListView):
    model = Pizza
    template_name = 'listar/pizza.html'
    paginate_by = 3


class PizzaUpdateView(UpdateView):
    model = Pizza
    template_name = 'atualizar/pizza.html'

    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('listar_pizza')

#################  CLASSE CADASTRO PIZZA   ####################

#################  CLASSE CADASTRO PASSAPORTE   ####################


class PassaporteCreateView(CreateView):
    model = Passaporte
    template_name = 'cadastrar/passaporte.html'

    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy("listar_passaporte")


class PassaporteListView(ListView):
    model = Passaporte
    template_name = 'listar/passaporte.html'
    paginate_by = 3


class PassaporteUpdateView(UpdateView):
    model = Passaporte
    template_name = 'atualizar/passaporte.html'

    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('listar_passaporte')


#################  CLASSE CADASTRO PASSAPORTE   ####################

#################  CLASSE CADASTRO PASTEL ####################

class PastelCreateView(CreateView):
    model = Pastel
    template_name = 'cadastrar/pastel.html'

    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy("listar_pastel")


class PastelListView(ListView):
    model = Pastel
    template_name = 'listar/pastel.html'
    paginate_by = 3


class PastelUpdateView(UpdateView):
    model = Pastel
    template_name = 'atualizar/pastel.html'

    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('listar_pastel')

#################  CLASSE CADASTRO PASTEL   ####################


#################  CLASSE CADASTRO CLIENTE   ####################


class ClienteCreateView(CreateView):
    model = Cliente
    template_name = 'cadastrar/cliente.html'

    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy("listar_cliente")


class ClienteListView(ListView):
    model = Cliente
    template_name = 'listar/cliente.html'
    paginate_by = 3


class ClienteUpdateView(UpdateView):
    model = Cliente
    template_name = 'atualizar/cliente.html'

    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('listar_cliente')

#################  CLASSE CADASTRO CLIENTE   ####################

#################  CLASSE CADASTRO CLIENTE PEQGUE LEVE   ####################


class ClientePegueLeveCreateView(CreateView):
    model = ClientePegueLeve
    template_name = 'cadastrar/pegueleve.html'

    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy("listar_pegueleve")


class ClientePegueLeveListView(ListView):
    model = ClientePegueLeve
    template_name = 'listar/pegueleve.html'
    paginate_by = 3


class ClientePegueLeveUpdateView(UpdateView):
    model = ClientePegueLeve
    template_name = 'atualizar/pegueleve.html'

    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('listar_pegueleve')

#################  CLASSE CADASTRO CLIENTE PEGUE LEVE   ####################
