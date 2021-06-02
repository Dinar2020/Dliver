from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, View, DetailView
from .models import Venda, Produto, EntregaProduto, Cliente, CadastroFornecedor, FormasPagamento,\
    CadastroAtendente, CadastroRestaurante, FazerPedido, RegistroCupom
from django.contrib import messages
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from .forms import VendaForm, VendaObservacaoForm, VendaClienteForm, ProdutoForm, ProdutoNacionalidadeForm, \
    ProdutoNomeForm, EntregaProdutoClienteForm, EntregaProdutoEntregaConcluidaForm, ClienteForm, ClienteNomeForm, \
    ClienteTelForm, EntregaProdutoForm, FornecedorForm, FornecedorEmpresaFornecidaForm, FormasPagamentoForm, \
    FormasPagamentoNomeForm, FormasPagamentoAppPagamentoForm, AtendenteForm, AtendenteEnderecoForm, AtendenteFotoForm, \
    RegistroCupomForm, RegistroCupomClienteForm, RegistroCupomValidadeForm, CadastroRestauranteForm, \
    CadastroRestauranteObservacaoClienteForm, CadastroRestauranteTelefoneForm, FazerPedidoForm, \
    FazerPedidoLocalDeEntregaForm, FazerPedidoNomeClienteForm
from easy_pdf.views import PDFTemplateResponseMixin
# Create your views here.

######################## VENDA ####################################


class VendaCreateView(CreateView):
    form_class = VendaForm
    template_name = 'cadastrar/venda.html'

    def get_success_url(self):
        messages.success(self.request, 'Venda cadastrada com sucesso!')
        return reverse_lazy('cadastrar_venda')


class VendaListView(ListView):
    model = Venda
    template_name = 'listar/venda.html'
    paginate_by = 5

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


class ProdutoCorrecaoUpdateView(UpdateView):
    model = Produto
    form_class = ProdutoForm
    template_name = 'atualizar/produto.html'

    def get_success_url(self):
        messages.success(self.request, 'Produto atualizado com sucesso!')
        return reverse_lazy('listar_produto')


class ProdutoAtualizarNacionalidadeView(UpdateView):
    model = Produto
    form_class = ProdutoNacionalidadeForm
    template_name = 'atualizar/produto_nacionalidade.html'

    def get_success_url(self):
        messages.success(self.request, 'Nacionalidade do produto atualizada com sucesso!')
        return reverse_lazy('listar_produto')


class ProdutoAtualizarNomeView(UpdateView):
    model = Venda
    form_class = ProdutoNomeForm
    template_name = 'atualizar/produto_nome.html'

    def get_success_url(self):
        messages.success(self.request, 'Nome do Produto atualizado com sucesso!')
        return reverse_lazy('listar_produto')


class ProdutoView(View):
    def desabilitarProduto(self, pk: int):
        Produto.objects.filter(id=pk).update(excluido=True)
        return HttpResponseRedirect(reverse_lazy('listar_produto'))

    def habilitarProduto(self, pk: int):
        Produto.objects.filter(id=pk).update(excluido=False)
        return HttpResponseRedirect(reverse_lazy('listar_produto'))

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



class EntregaProdutoCorrecaoUpdateView(UpdateView):
    model = EntregaProduto
    form_class = EntregaProdutoForm
    template_name = 'atualizar/venda.html'

    def get_success_url(self):
        messages.success(self.request, 'Entrega do produto atualizada com sucesso!')
        return reverse_lazy('listar_entrega_produto')


class EntregaProdutoAtualizarClienteView(UpdateView):
    model = EntregaProduto
    form_class = EntregaProdutoClienteForm
    template_name = 'atualizar/entrega_produto_cliente.html'

    def get_success_url(self):
        messages.success(self.request, 'Cliente da entrega atualizado com sucesso!')
        return reverse_lazy('listar_entrega_produto')


class EntregaProdutoAtualizarEntregaConcluidaView(UpdateView):
    model = EntregaProduto
    form_class = EntregaProdutoEntregaConcluidaForm
    template_name = 'atualizar/entrega_produto_entrega_concluida.html'

    def get_success_url(self):
        messages.success(self.request, 'Status da entrega atualizado com sucesso!')
        return reverse_lazy('listar_entrega_produto')


class EntregaProdutoView(View):
    def desabilitarEntregaProduto(self, pk: int):
        EntregaProduto.objects.filter(id=pk).update(excluido=True)
        return HttpResponseRedirect(reverse_lazy('listar_entrega_produto'))

    def habilitarEntregaProduto(self, pk: int):
        EntregaProduto.objects.filter(id=pk).update(excluido=False)
        return HttpResponseRedirect(reverse_lazy('listar_entrega_produto'))

####################### CLIENTE ###################################
class ClienteCreateView(CreateView):
    model = Cliente
    template_name = 'cadastrar/cliente.html'
    fields = '__all__'

    def get_success_url(self):
        messages.success(self.request, 'Cliente cadastrado com suceso!')
        return reverse_lazy('cadastrar_cliente')


class ClienteListView(ListView):
    model = Cliente
    template_name = 'listar/cliente.html'
    paginate_by = 5


class ClienteCorrecaoUpdateView(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'atualizar/cliente.html'

    def get_success_url(self):
        messages.success(self.request, 'Cliente atualizado com sucesso!')
        return reverse_lazy('listar_cliente')


class ClienteAtualizarNomeView(UpdateView):
    model = Cliente
    form_class = ClienteNomeForm
    template_name = 'atualizar/cliente_nome.html'

    def get_success_url(self):
        messages.success(self.request, 'Nome do cliente atualizado com sucesso!')
        return reverse_lazy('listar_cliente')


class ClienteAtualizarTelefoneView(UpdateView):
    model = Cliente
    form_class = ClienteTelForm
    template_name = 'atualizar/cliente_tel.html'

    def get_success_url(self):
        messages.success(self.request, 'Telefone do cliente atualizado com sucesso!')
        return reverse_lazy('listar_cliente')


class ClienteView(View):
    def desabilitarCliente(self, pk: int):
        Cliente.objects.filter(id=pk).update(excluido=True)
        return HttpResponseRedirect(reverse_lazy('listar_cliente'))

    def habilitarCliente(self, pk: int):
        Cliente.objects.filter(id=pk).update(excluido=False)
        return HttpResponseRedirect(reverse_lazy('listar_cliente'))
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


class CadastroFornecedorCorrecaoUpdateView(UpdateView):
    model = CadastroFornecedor
    form_class = FornecedorForm
    template_name = 'atualizar/fornecedor.html'

    def get_success_url(self):
        messages.success(self.request, 'Cadastro de fornecedor atualizado com sucesso!')
        return reverse_lazy('listar_fornecedor')


class CadastroFornecedorAtualizarNomeView(UpdateView):
    model = CadastroFornecedor
    form_class = VendaObservacaoForm
    template_name = 'atualizar/fornecedor_nome.html'

    def get_success_url(self):
        messages.success(self.request, 'Observação da venda atualizada com sucesso!')
        return reverse_lazy('listar_fornecedor')


class CadastroFornecedorAtualizarEmpresaFornecidaView(UpdateView):
    model = Venda
    form_class = FornecedorEmpresaFornecidaForm
    template_name = 'atualizar/fornecedor_empresa_fornecida.html'

    def get_success_url(self):
        messages.success(self.request, 'Empresa fornecida atualizada com sucesso!')
        return reverse_lazy('listar_fornecedor')


class CadastroFornecedorView(View):
    def desabilitarCadastroFornecedor(self, pk: int):
        CadastroFornecedor.objects.filter(id=pk).update(excluido=True)
        return HttpResponseRedirect(reverse_lazy('listar_fornecedor'))

    def habilitarCadastroFornecedor(self, pk: int):
        CadastroFornecedor.objects.filter(id=pk).update(excluido=False)
        return HttpResponseRedirect(reverse_lazy('listar_fornecedor'))

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


class FormasPagamentoCorrecaoUpdateView(UpdateView):
    model = FormasPagamento
    form_class = FormasPagamentoForm
    template_name = 'atualizar/formaspagamento.html'

    def get_success_url(self):
        messages.success(self.request, 'Formas de pagamento atualizadas com sucesso!')
        return reverse_lazy('listar_formaspagamento')


class FormasPagamentoAtualizarNomeView(UpdateView):
    model = FormasPagamento
    form_class = FormasPagamentoNomeForm
    template_name = 'atualizar/formaspagamento_nome.html'

    def get_success_url(self):
        messages.success(self.request, 'Nome do restaurante atualizado com sucesso!')
        return reverse_lazy('listar_venda')


class FormasPagamentoAtualizarAppPagamentoView(UpdateView):
    model = FormasPagamento
    form_class = FormasPagamentoAppPagamentoForm
    template_name = 'atualizar/formaspagamento_app_pagamento.html'

    def get_success_url(self):
        messages.success(self.request, 'Cliente da venda atualizada com sucesso!')
        return reverse_lazy('listar_formaspagamento')


class FormasPagamentoView(View):
    def desabilitarFormasPagamento(self, pk: int):
        FormasPagamento.objects.filter(id=pk).update(excluido=True)
        return HttpResponseRedirect(reverse_lazy('listar_formaspagamento'))

    def habilitarFormasPagamento(self, pk: int):
        FormasPagamento.objects.filter(id=pk).update(excluido=False)
        return HttpResponseRedirect(reverse_lazy('listar_formaspagamento'))

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


class CadastroAtendenteCorrecaoUpdateView(UpdateView):
    model = CadastroAtendente
    form_class = AtendenteForm
    template_name = 'atualizar/atendente.html'

    def get_success_url(self):
        messages.success(self.request, 'Atendente atualizado com sucesso!')
        return reverse_lazy('listar_atendente')


class CadastroAtendenteAtualizarEnderecoView(UpdateView):
    model = CadastroAtendente
    form_class = AtendenteEnderecoForm
    template_name = 'atualizar/atendente_endereco.html'

    def get_success_url(self):
        messages.success(self.request, 'Endereço do atendente atualizado com sucesso!')
        return reverse_lazy('listar_atendente')


class CadastroAtendenteAtualizarFotoView(UpdateView):
    model = CadastroAtendente
    form_class = AtendenteFotoForm
    template_name = 'atualizar/atendente_foto.html'

    def get_success_url(self):
        messages.success(self.request, 'Foto do atendente atualizada com sucesso!')
        return reverse_lazy('listar_atendente')


class CadastroAtendenteView(View):
    def desabilitarCadastroAtendente(self, pk: int):
        CadastroAtendente.objects.filter(id=pk).update(excluido=True)
        return HttpResponseRedirect(reverse_lazy('listar_atendente'))

    def habilitarCadastroAtendente(self, pk: int):
        CadastroAtendente.objects.filter(id=pk).update(excluido=False)
        return HttpResponseRedirect(reverse_lazy('listar_atendente'))

######################## CadastroAtendente ####################################


######################## RegistroCupom ####################################

class RegistroCupomCreateView(CreateView):
    model = RegistroCupom
    template_name = 'cadastrar/registrocupom.html'

    fields = '__all__'

    def get_success_url(self):
        messages.success(self.request, 'Cupom cadastrado com suceso!')
        return reverse_lazy('listar_registrocupom')


class RegistroCupomListView(ListView):
    model = RegistroCupom
    template_name = 'listar/registrocupom.html'
    paginate_by = 5


class RegistroCupomCorrecaoUpdateView(UpdateView):
    model = RegistroCupom
    form_class = RegistroCupomForm
    template_name = 'atualizar/venda.html'

    def get_success_url(self):
        messages.success(self.request, 'Registro do cupom atualizado com sucesso!')
        return reverse_lazy('listar_venda')


class RegistroCupomAtualizarClienteView(UpdateView):
    model = RegistroCupom
    form_class = RegistroCupomClienteForm
    template_name = 'atualizar/registrocupom_cliente.html'

    def get_success_url(self):
        messages.success(self.request, 'Cliente registrado no cupom atualizado com sucesso!')
        return reverse_lazy('listar_registrocupom')


class RegistroCupomAtualizarValidadeView(UpdateView):
    model = RegistroCupom
    form_class = RegistroCupomValidadeForm
    template_name = 'atualizar/registrocupom_validade.html'

    def get_success_url(self):
        messages.success(self.request, 'Validade do cupom atualizada com sucesso!')
        return reverse_lazy('listar_resgistrocupom')


class RegistroCupomView(View):
    def desabilitarRegistroCupom(self, pk: int):
        RegistroCupom.objects.filter(id=pk).update(excluido=True)
        return HttpResponseRedirect(reverse_lazy('listar_registrocupom'))

    def habilitarRegistroCupom(self, pk: int):
        RegistroCupom.objects.filter(id=pk).update(excluido=False)
        return HttpResponseRedirect(reverse_lazy('listar_resgistrocupom'))

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


class CadastroRestauranteCorrecaoUpdateView(UpdateView):
    model = Venda
    form_class = CadastroRestauranteForm
    template_name = 'atualizar/restaurante.html'

    def get_success_url(self):
        messages.success(self.request, 'Venda atualizada com sucesso!')
        return reverse_lazy('listar_restaurante')


class CadastroRestauranteAtualizarObservacaoView(UpdateView):
    model = Venda
    form_class = CadastroRestauranteObservacaoClienteForm
    template_name = 'atualizar/restaurante_observacao.html'

    def get_success_url(self):
        messages.success(self.request, 'Observação do restaurante atualizada com sucesso!')
        return reverse_lazy('listar_restaurante')


class CadastroRestauranteAtualizarTelefoneView(UpdateView):
    model = CadastroRestaurante
    form_class = CadastroRestauranteTelefoneForm
    template_name = 'atualizar/restaurante_telefone.html'

    def get_success_url(self):
        messages.success(self.request, 'Telefone do restaurante atualizada com sucesso!')
        return reverse_lazy('listar_restaurante')


class CadastroRestauranteView(View):
    def desabilitarCadastroRestaurante(self, pk: int):
        CadastroAtendente.objects.filter(id=pk).update(excluido=True)
        return HttpResponseRedirect(reverse_lazy('listar_restaurante'))

    def habilitarCadastroRestaurante(self, pk: int):
        CadastroRestaurante.objects.filter(id=pk).update(excluido=False)
        return HttpResponseRedirect(reverse_lazy('listar_restaurante'))

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


class FazerPedidoCorrecaoUpdateView(UpdateView):
    model = FazerPedido
    form_class = FazerPedidoForm
    template_name = 'atualizar/pedido.html'

    def get_success_url(self):
        messages.success(self.request, 'Pedido atualizada com sucesso!')
        return reverse_lazy('listar_pedido')


class FazerPedidoAtualizarLocalDeEntregaView(UpdateView):
    model = FazerPedido
    form_class = FazerPedidoLocalDeEntregaForm
    template_name = 'atualizar/venda_observacao.html'

    def get_success_url(self):
        messages.success(self.request, 'Local de entrega do pedido atualizado com sucesso!')
        return reverse_lazy('listar_pedido')


class FazerPedidoAtualizarNomeClienteView(UpdateView):
    model = FazerPedido
    form_class = FazerPedidoNomeClienteForm
    template_name = 'atualizar/venda_cliente.html'

    def get_success_url(self):
        messages.success(self.request, 'Cliente do pedido atualizado com sucesso!')
        return reverse_lazy('listar_pedido')


class FazerPedidoView(View):
    def desabilitarFazerPedido(self, pk: int):
        FazerPedido.objects.filter(id=pk).update(excluido=True)
        return HttpResponseRedirect(reverse_lazy('listar_pedido'))

    def habilitarFazerPedido(self, pk: int):
        FazerPedido.objects.filter(id=pk).update(excluido=False)
        return HttpResponseRedirect(reverse_lazy('listar_pedido'))

######################## FazerPedido ####################################

