from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView,View, DetailView
from .models import Venda, Produto, EntregaProduto, Cliente, CadastroFornecedor, FormasPagamento,\
    CadastroAtendente, CadastroRestaurante, FazerPedido, RegistroCupom
from django.contrib import messages
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from .forms import VendaForm, VendaObservacaoForm, VendaClienteForm
from easy_pdf.views import PDFTemplateResponseMixin
# Create your views here.

######################## VENDA ####################################

class VendaCreateView(CreateView):
    form_class = VendaForm
    model = Venda
    template_name = 'cadastrar/venda.html'

    fields = '__all__'

    def get_success_url(self):
        messages.success(self.request, 'Venda cadastrada com sucesso!')
        return reverse_lazy('cadastrar_venda')


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

class VendaCorrecaoUpdateView(UpdateView):
    model = Venda
    form_class = VendaForm
    template_name = 'atualizar/venda.html'

    def get_success_url(self):
        messages.success(self.request, 'Venda atualizada com sucesso!')
        return reverse_lazy('listar_venda')

class VendaAtualizarObservacaoView(UpdateView):
    model = Venda
    form_class = VendaObservacaoForm
    template_name = 'atualizar/venda_observacao.html'

    def get_success_url(self):
        messages.success(self.request, 'Observação da venda atualizada com sucesso!')
        return reverse_lazy('listar_venda')

class VendaAtualizarClienteView(UpdateView):
    model = Venda
    form_class = VendaClienteForm
    template_name = 'atualizar/venda_cliente.html'

    def get_success_url(self):
        messages.success(self.request, 'Cliente da venda atualizada com sucesso!')
        return reverse_lazy('listar_venda')


class VendaView(View):
    def desabilitarVenda(self, pk: int):
        Venda.objects.filter(id=pk).update(excluido=True)
        return HttpResponseRedirect(reverse_lazy('listar_venda'))

    def habilitarVenda(self, pk: int):
        Venda.objects.filter(id=pk).update(excluido=False)
        return HttpResponseRedirect(reverse_lazy('listar_venda'))


class VendaDetailView(DetailView):
    model = Venda
    template_name = 'detalhes/venda.html'


class VendaPDFDetailView(PDFTemplateResponseMixin, DetailView):
    model = Venda
    template_name = 'detalhes/pdf_venda.html'

######################## VENDA ####################################


####################### PRODUTO ###################################

class ProdutoCreateView(CreateView):
    model = Produto
    template_name = 'cadastrar/produto.html'
    fields = '__all__'

    def get_success_url(self):
        messages.success(self.request, 'Produto cadastrado com suceso!')
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
        messages.success(self.request, 'entrega cadastrada com suceso!')
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
        messages.success(self.request, 'Cliente cadastrado com suceso!')
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

####################### FORNECEDOR  ###################################

class CadastroFornecedorCreateView(CreateView):
    model = CadastroFornecedor
    template_name = 'cadastrar/fornecedor.html'
    fields = '__all__'

    def get_success_url(self):
        messages.success(self.request, 'Fornecedor cadastrado com suceso!')
        return reverse_lazy('cadastrar_fornecedor')


class CadastroFornecedorListView(ListView):
    model = CadastroFornecedor
    template_name = 'listar/fornecedor.html'
    paginate_by = 5


class CadastroFornecedorUpdateView(UpdateView):
    model = CadastroFornecedor
    template_name = 'atualizar/fornecedor.html'

    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('listar_fornecedor')

####################### FORNECEDOR ###################################

######################## FormasPagamento ####################################

class FormasPagamentoCreateView(CreateView):
    model = FormasPagamento
    template_name = 'cadastrar/formaspagamento.html'

    fields = '__all__'

    def get_success_url(self):
        messages.success(self.request, 'Formas de pagamento cadastradas com suceso!')
        return reverse_lazy("listar_formaspagamento")


class FormasPagamentoListView(ListView):
    model = FormasPagamento
    template_name = 'listar/formaspagamento.html'
    paginate_by = 5


class FormasPagamentoUpdateView(UpdateView):
    model = FormasPagamento
    template_name = 'atualizar/formaspagamento.html'

    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('listar_formaspagamento')

######################## FormasPagamento ####################################

######################## CadastroAtendente ####################################

class CadastroAtendenteCreateView(CreateView):
    model = CadastroAtendente
    template_name = 'cadastrar/atendente.html'

    fields = '__all__'

    def get_success_url(self):
        messages.success(self.request, 'Atendente cadastrado com suceso!')
        return reverse_lazy("listar_atendente")


class CadastroAtendenteListView(ListView):
    model = CadastroAtendente
    template_name = 'listar/atendente.html'
    paginate_by = 5


class CadastroAtendenteUpdateView(UpdateView):
    model = CadastroAtendente
    template_name = 'atualizar/atendente.html'

    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('listar_atendente')

######################## CadastroAtendente ####################################


######################## RegistroCupom ####################################

class CadastroLocalDeEntregaCreateView(CreateView):
    model = RegistroCupom
    template_name = 'cadastrar/registrocupom.html'

    fields = '__all__'

    def get_success_url(self):
        messages.success(self.request, 'Cupom cadastrado com suceso!')
        return reverse_lazy('listar_registrocupom')


class CadastroLocalDeEntregaListView(ListView):
    model = RegistroCupom
    template_name = 'listar/registrocupom.html'
    paginate_by = 5


class CadastroLocalDeEntregaUpdateView(UpdateView):
    model = RegistroCupom
    template_name = 'atualizar/registrocupom.html'

    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('listar_registrocupom')

######################## RegistroCupom ####################################

######################## CadastroRestaurante ####################################

class CadastroRestauranteCreateView(CreateView):
    model = CadastroRestaurante
    template_name = 'cadastrar/restaurante.html'

    fields = '__all__'

    def get_success_url(self):
        messages.success(self.request, 'Restaurante cadastrado com suceso!')
        return reverse_lazy("listar_restaurante")


class CadastroRestauranteListView(ListView):
    model = CadastroRestaurante
    template_name = 'listar/restaurante.html'
    paginate_by = 5


class CadastroRestauranteUpdateView(UpdateView):
    model = CadastroRestaurante
    template_name = 'atualizar/restaurante.html'

    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('listar_restaurante')

######################## CadastroRestaurante ####################################

######################## FazerPedido ####################################

class FazerPedidoCreateView(CreateView):
    model = FazerPedido
    template_name = 'cadastrar/pedido.html'

    fields = '__all__'

    def get_success_url(self):
        messages.success(self.request, 'Pedido feito com suceso!')
        return reverse_lazy("listar_pedido")


class FazerPedidoListView(ListView):
    model = FazerPedido
    template_name = 'listar/pedido.html'
    paginate_by = 5


class FazerPedidoUpdateView(UpdateView):
    model = FazerPedido
    template_name = 'atualizar/pedido.html'

    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('listar_pedido')

######################## FazerPedido ####################################

