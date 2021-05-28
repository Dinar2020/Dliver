from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView
from .models import Venda, Produto, EntregaProduto, Cliente, ClientePegueLeve, Fornecedor, Faq, CadastroRestaurante,\
    FormasPagamento

from django.urls import reverse_lazy
from django.contrib import messages

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
        messages.success(self.request, 'Produto cadastrado com sucesso!')
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
        messages.success(self.request, 'Produto Atualizado com sucesso!')
        return reverse_lazy('listar_produto')

####################### PRODUTO ###################################

####################### ENTREGA PRODUTO ###################################

class EntregaProdutoCreateView(CreateView):
    model = EntregaProduto
    template_name = 'cadastrar/entrega_produto.html'
    fields = '__all__'

    def get_success_url(self):
        messages.success(self.request, 'Produto cadastrado com sucesso!')
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
        messages.success(self.request, 'Entrega do Produto Atualizado com sucesso!')
        return reverse_lazy('listar_entrega_produto')

####################### ENTREGA PRODUTO ###################################

####################### CLIENTE ###################################

class ClienteCreateView(CreateView):
    model = Cliente
    template_name = 'cadastrar/entrega_cliente.html'
    fields = '__all__'

    def get_success_url(self):
        messages.success(self.request, 'Cliente cadastrado com sucesso!')
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
        messages.success(self.request, 'Cliente atualizado com sucesso!')
        return reverse_lazy('listar_cliente')

####################### CLIENTE ###################################

####################### CLIENTE PEGUE-LEVE  ###################################

class ClientePegueLeveCreateView(CreateView):
    model = ClientePegueLeve
    template_name = 'cadastrar/clientepegueleve.html'
    fields = '__all__'

    def get_success_url(self):
        messages.success(self.request, 'Cliente Atualizado com sucesso!')
        return reverse_lazy('atualizar_clientepegueleve')


class ClientePegueLeveListView(ListView):
    model = ClientePegueLeve
    template_name = 'listar/clientepegueleve.html'
    paginate_by = 5


class ClientePegueLeveUpdateView(UpdateView):
    model = ClientePegueLeve
    template_name = 'atualizar/clientepegueleve.html'

    fields = '__all__'

    def get_success_url(self):
        messages.success(self.request, 'Cliente atualizado com sucesso!')
        return reverse_lazy('listar_clientepegueleve')

####################### CLIENTE PEGUE-LEVE ###################################

####################### FORNECEDOR  ###################################

class FornecedorCreateView(CreateView):
    model = Fornecedor
    template_name = 'cadastrar/fornecedor.html'
    fields = '__all__'

    def get_success_url(self):
        messages.success(self.request, 'Fornecedor cadastrado com sucesso!')
        return reverse_lazy('cadastrar_fornacedor')


class FornecedorListView(ListView):
    model = Fornecedor
    template_name = 'listar/fornecedor.html'
    paginate_by = 5


class FornecedorUpdateView(UpdateView):
    model = Fornecedor
    template_name = 'atualizar/fornecedor.html'

    fields = '__all__'

    def get_success_url(self):
        messages.success(self.request, 'Fornecedor Atualizado com sucesso!')
        return reverse_lazy('listar_fornecedor')

####################### FORNECEDOR ###################################

####################### FAQ  ###################################

class FaqCreateView(CreateView):
    model = Faq
    template_name = 'cadastrar/faq.html'
    fields = '__all__'

    def get_success_url(self):
        messages.success(self.request, 'FAQ cadastrado com sucesso!')
        return reverse_lazy('cadastrar_faq')


class FaqListView(ListView):
    model = Faq
    template_name = 'listar/faq.html'
    paginate_by = 5


class FaqUpdateView(UpdateView):
    model = Faq
    template_name = 'atualizar/faq.html'

    fields = '__all__'

    def get_success_url(self):
        messages.success(self.request, 'FAQ atualizado com sucesso!')
        return reverse_lazy('listar_faq')

####################### FAQ ###################################

######################## CADASTRO RESTAURANTE ####################################

class CadastroRestauranteCreateView(CreateView):
    model = CadastroRestaurante
    template_name = 'cadastrar/cadastrorestaurante.html'

    fields = '__all__'

    def get_success_url(self):
        messages.success(self.request, 'Cadastro do Restaurante realizado com sucesso!')
        return reverse_lazy("listar_cadastrorestaurante")


class CadastroRestauranteListView(ListView):
    model = CadastroRestaurante
    template_name = 'listar/cadastrorestaurante.html'
    paginate_by = 5


class CadastroRestauranteUpdateView(UpdateView):
    model = CadastroRestaurante
    template_name = 'atualizar/cadastrorestaurante.html'

    fields = '__all__'

    def get_success_url(self):
        messages.success(self.request, 'Cadastro do Restaurante atualizado com sucesso!')
        return reverse_lazy('listar_cadastrorestaurante')

######################## CADASTRO RESTAURANTE ####################################

######################## FORMAS DE PAGAMENTO ####################################

class FormasPagamentoCreateView(CreateView):
    model = FormasPagamento
    template_name = 'cadastrar/formaspagamento.html'

    fields = '__all__'

    def get_success_url(self):
        messages.success(self.request, 'Forma de pagamento realizado com sucesso!')
        return reverse_lazy("listar_formaspagamento")


class FormasPagamentoListView(ListView):
    model = CadastroRestaurante
    template_name = 'listar/formaspagamento.html'
    paginate_by = 5


class FormasPagamentoUpdateView(UpdateView):
    model = CadastroRestaurante
    template_name = 'atualizar/formaspagamento.html'

    fields = '__all__'

    def get_success_url(self):
        messages.success(self.request, 'Forma de pagamento atualizado com sucesso!')
        return reverse_lazy('listar_formaspagamento')

######################## FORMAS DE PAGAMENTO ####################################