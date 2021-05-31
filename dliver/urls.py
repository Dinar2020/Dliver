from django.contrib import admin
from django.urls import path
from .views import VendaCreateView, VendaListView, VendaCorrecaoUpdateView, VendaAtualizarObservacaoView,\
    VendaAtualizarClienteView, VendaView, VendaDetailView, VendaPDFDetailView, ProdutoCreateView,\
    ProdutoUpdateView, ProdutoListView, EntregaProdutoCreateView, EntregaProdutoListView, EntregaProdutoUpdateView,\
    ClienteCreateView, ClienteListView, ClienteUpdateView, CadastroFornecedorCreateView, CadastroFornecedorListView, \
    CadastroFornecedorUpdateView, FormasPagamentoCreateView, FormasPagamentoListView, FormasPagamentoUpdateView

urlpatterns = [
    path('cadastrar/venda', VendaCreateView.as_view(), name="cadastrar_venda"),
    path('listar/venda', VendaListView.as_view(), name="listar_venda"),
    path('atualizar/venda/<int:pk>', VendaCorrecaoUpdateView.as_view(), name="corrigir_venda"),
    path('atualizar/venda/observacao/<int:pk>', VendaAtualizarObservacaoView.as_view(),
         name="atualizar_observacao_venda"),
    path('atualizar/venda/cliente/<int:pk>', VendaAtualizarClienteView.as_view(), name="atualizar_cliente_venda"),
    path('ajax/desabilitar/venda/<int:pk>', VendaView.desabilitarVenda, name="ajax_desabilitar_venda"),
    path('ajax/habilitar/venda/<int:pk>', VendaView.habilitarVenda, name="ajax_habilitar_venda"),
    path('detalhes/venda/<int:pk>', VendaDetailView.as_view(), name="detalhes_venda"),
    path('pdf/venda/<int:pk>', VendaPDFDetailView.as_view(), name="pdf_venda"),

    path('cadastrar/produto', ProdutoCreateView.as_view(), name="cadastrar_produto"),
    path('listar/produto', ProdutoListView.as_view(), name="listar_produto"),
    path('atualizar/produto/<int:pk>', ProdutoUpdateView.as_view(), name="atualizar_produto"),

    path('cadastrar/entregaproduto', EntregaProdutoCreateView.as_view(), name="cadastrar_entrega_produto"),
    path('listar/entregaproduto', EntregaProdutoListView.as_view(), name="listar_entrega_produto"),
    path('atualizar/entregaproduto/<int:pk>', EntregaProdutoUpdateView.as_view(), name="atualizar_entrega_produto"),

    path('cadastrar/cliente', ClienteCreateView.as_view(), name="cadastrar_cliente"),
    path('listar/cliente', ClienteListView.as_view(), name="listar_entrega_cliente"),
    path('atualizar/cliente/<int:pk>', ClienteUpdateView.as_view(), name="atualizar_cliente"),

    path('cadastrar/fornecedor', CadastroFornecedorCreateView.as_view(), name="cadastrar_fornecedor"),
    path('listar/fornecedor', CadastroFornecedorListView.as_view(), name="listar_fornecedor"),
    path('atualizar/fornecedor/<int:pk>', CadastroFornecedorUpdateView.as_view(), name="atualizar_fornecedor"),

    path('cadastrar/formaspagamento', FormasPagamentoCreateView.as_view(), name="cadastrar_formaspagamento"),
    path('listar/formaspagamento', FormasPagamentoListView.as_view(), name="listar_formaspagamento"),
    path('atualizar/formaspagamento/<int:pk>', FormasPagamentoUpdateView.as_view(), name="atualizar_formaspagamento"),
]
