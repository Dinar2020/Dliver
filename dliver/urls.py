from django.contrib import admin
from django.urls import path
from .views import VendaCreateView, VendaListView, VendaCorrecaoUpdateView, VendaAtualizarObservacaoView, \
    VendaAtualizarClienteView, VendaView, VendaDetailView, VendaPDFDetailView, ProdutoCreateView, \
    ProdutoListView, EntregaProdutoCreateView, EntregaProdutoListView, \
    ClienteCreateView, ClienteListView, CadastroFornecedorCreateView, CadastroFornecedorListView, \
    FormasPagamentoCreateView, FormasPagamentoListView, CadastroAtendenteCreateView, CadastroAtendenteListView, \
    RegistroCupomCreateView, RegistroCupomListView, CadastroRestauranteCreateView, CadastroRestauranteListView, \
    FazerPedidoCreateView, FazerPedidoListView, ProdutoCorrecaoUpdateView, ProdutoAtualizarNomeView, \
    ProdutoAtualizarNacionalidadeView, ProdutoView, EntregaProdutoCorrecaoUpdateView, \
    EntregaProdutoAtualizarClienteView, EntregaProdutoAtualizarEntregaConcluidaView, EntregaProdutoView, \
    ClienteCorrecaoUpdateView, ClienteAtualizarNomeView, ClienteAtualizarTelefoneView, ClienteView, \
    CadastroFornecedorCorrecaoUpdateView, CadastroFornecedorAtualizarNomeView, \
    CadastroFornecedorAtualizarEmpresaFornecidaView, CadastroFornecedorView, FormasPagamentoAtualizarAppPagamentoView, \
    FormasPagamentoAtualizarNomeView, FormasPagamentoView, CadastroAtendenteCorrecaoUpdateView, \
    CadastroAtendenteAtualizarEnderecoView, CadastroAtendenteAtualizarFotoView, CadastroAtendenteView, \
    RegistroCupomCorrecaoUpdateView, RegistroCupomAtualizarClienteView, RegistroCupomAtualizarValidadeView, \
    RegistroCupomView, CadastroRestauranteCorrecaoUpdateView, CadastroRestauranteAtualizarObservacaoView, \
    CadastroRestauranteAtualizarTelefoneView, CadastroRestauranteView, FazerPedidoCorrecaoUpdateView, \
    FazerPedidoAtualizarLocalDeEntregaView, FazerPedidoAtualizarNomeClienteView, FazerPedidoView

urlpatterns = [
    # venda
    path('cadastrar/venda', VendaCreateView.as_view(),
         name="cadastrar_venda"),
    path('listar/venda', VendaListView.as_view(),
         name="listar_venda"),
    path('atualizar/venda/<int:pk>', VendaCorrecaoUpdateView.as_view(),
         name="corrigir_venda"),
    path('atualizar/venda/observacao/<int:pk>', VendaAtualizarObservacaoView.as_view(),
         name="atualizar_observacao_venda"),
    path('atualizar/venda/cliente/<int:pk>', VendaAtualizarClienteView.as_view(),
         name="atualizar_cliente_venda"),
    path('ajax/desabilitar/venda/<int:pk>', VendaView.desabilitarVenda,
         name="ajax_desabilitar_venda"),
    path('ajax/habilitar/venda/<int:pk>', VendaView.habilitarVenda,
         name="ajax_habilitar_venda"),
    path('detalhes/venda/<int:pk>', VendaDetailView.as_view(),
         name="detalhes_venda"),
    path('pdf/venda/<int:pk>', VendaPDFDetailView.as_view(),
         name="pdf_venda"),

    # produto
    path('cadastrar/produto', ProdutoCreateView.as_view(),
         name="cadastrar_produto"),
    path('listar/produto', ProdutoListView.as_view(),
         name="listar_produto"),
    path('atualizar/produto/<int:pk>', ProdutoCorrecaoUpdateView.as_view(),
         name="corrigir_produto"),
    path('atualizar/produto/nacionalidade/<int:pk>', ProdutoAtualizarNacionalidadeView.as_view(),
         name="atualizar_produto-nacionalidade"),
    path('atualizar/produto/nome/<int:pk>', ProdutoAtualizarNomeView.as_view(),
         name="atualizar_produto_nome"),
    path('ajax/desabilitar/produto/<int:pk>', ProdutoView.desabilitarProduto,
         name="ajax_desabilitar_produto"),
    path('ajax/habilitar/produto/<int:pk>', ProdutoView.habilitarProduto,
         name="ajax_habilitar_produto"),

    # AJEITA LISTAR /....... html


    # entregaproduto
    path('cadastrar/entregaproduto', EntregaProdutoCreateView.as_view(),
         name="cadastrar_entrega_produto"),
    path('listar/entregaproduto', EntregaProdutoListView.as_view(),
         name="listar_entrega_produto"),
    path('atualizar/entregaproduto/<int:pk>', EntregaProdutoCorrecaoUpdateView.as_view(),
         name="corrigir_entrega_produto"),
    path('atualizar/entregaproduto/cliente/<int:pk>', EntregaProdutoAtualizarClienteView.as_view(),
         name="atualizar_cliente_entrega_produto"),
    path('atualizar/entregaproduto/status/<int:pk>', EntregaProdutoAtualizarEntregaConcluidaView.as_view(),
         name="atualizar_status_entrega_produto"),
    path('ajax/desabilitar/entregaproduto/<int:pk>', EntregaProdutoView.desabilitarEntregaProduto,
         name="ajax_desabilitar_entrega_produto"),
    path('ajax/habilitar/entregaproduto/<int:pk>', EntregaProdutoView.habilitarEntregaProduto,
         name="ajax_habilitar_entrega_produto"),


    # cliente
    path('cadastrar/cliente', ClienteCreateView.as_view(),
         name="cadastrar_cliente"),
    path('listar/cliente', ClienteListView.as_view(),
         name="listar_cliente"),
    path('atualizar/cliente/<int:pk>', ClienteCorrecaoUpdateView.as_view(),
         name="corrigir_cliente"),
    path('atualizar/cliente/nome/<int:pk>', ClienteAtualizarNomeView.as_view(),
         name="atualizar_nome_cliente"),
    path('atualizar/cliente/telefone/<int:pk>', ClienteAtualizarTelefoneView.as_view(),
         name="atualizar_telefone_cliente"),
    path('ajax/desabilitar/cliente/<int:pk>', ClienteView.desabilitarCliente,
         name="ajax_desabilitar_cliente"),
    path('ajax/habilitarcliente/<int:pk>', ClienteView.habilitarCliente,
         name="ajax_habilitar_cliente"),



    # fornecedor
    path('cadastrar/fornecedor', CadastroFornecedorCreateView.as_view(),
         name="cadastrar_fornecedor"),
    path('listar/fornecedor', CadastroFornecedorListView.as_view(),
         name="listar_fornecedor"),
    path('atualizar/fornecedor/<int:pk>', CadastroFornecedorCorrecaoUpdateView.as_view(),
         name="corrigir_fornecedor"),
    path('atualizar/fornecedor/nome/<int:pk>', CadastroFornecedorAtualizarNomeView.as_view(),
         name="atualizar_nome_fornecedor"),
    path('atualizar/produto/empresa_fornecida/<int:pk>', CadastroFornecedorAtualizarEmpresaFornecidaView.as_view(),
         name="atualizar_empresa_fornecida_fornecedor"),
    path('ajax/desabilitar/fornecedor/<int:pk>', CadastroFornecedorView.desabilitarCadastroFornecedor,
         name="ajax_desabilitar_fornecedor"),
    path('ajax/habilitar/fornecedor/<int:pk>', CadastroFornecedorView.habilitarCadastroFornecedor,
         name="ajax_habilitar_fornecedor"),



    # formaspagamento
    path('cadastrar/formaspagamento', FormasPagamentoCreateView.as_view(),
         name="cadastrar_formaspagamento"),
    path('listar/formaspagamento', FormasPagamentoListView.as_view(),
         name="listar_formaspagamento"),
    path('atualizar/formaspagamento/<int:pk>', ProdutoCorrecaoUpdateView.as_view(),
         name="corrigir_formaspagamento"),
    path('atualizar/formaspagamento/app_pagamento/<int:pk>', FormasPagamentoAtualizarAppPagamentoView.as_view(),
         name="atualizar_app_pagamento_formaspagamento"),
    path('atualizar/formaspagamento/nome/<int:pk>', FormasPagamentoAtualizarNomeView.as_view(),
         name="atualizar_nome_formaspagamento"),
    path('ajax/desabilitar/formaspagamento/<int:pk>', FormasPagamentoView.desabilitarFormasPagamento,
         name="ajax_desabilitar_formaspagamento"),
    path('ajax/habilitar/formaspagamento/<int:pk>', FormasPagamentoView.habilitarFormasPagamento,
         name="ajax_habilitar_formaspagamento"),

    # FAZER APÓS A PROVA DAQUI PRA BAIXO

    # atendente
    path('cadastrar/atendente', CadastroAtendenteCreateView.as_view(),
         name="cadastrar_atendente"),
    path('listar/atendente', CadastroAtendenteListView.as_view(),
         name="listar_atendente"),
    path('atualizar/atendente/<int:pk>', CadastroAtendenteCorrecaoUpdateView.as_view(),
         name="corrigir_atendente"),
    path('atualizar/atendente/endereco/<int:pk>', CadastroAtendenteAtualizarEnderecoView.as_view(),
         name="atualizar_endereco-atendente"),
    path('atualizar/produto/foto/<int:pk>', CadastroAtendenteAtualizarFotoView.as_view(),
         name="atualizar_foto_atendente"),
    path('ajax/desabilitar/atendente/<int:pk>', CadastroAtendenteView.desabilitarCadastroAtendente,
         name="ajax_desabilitar_atendente"),
    path('ajax/habilitar/atendente/<int:pk>', CadastroAtendenteView.habilitarCadastroAtendente,
         name="ajax_habilitar_atendente"),



    # registrocupom
    path('cadastrar/registrocupom', RegistroCupomCreateView.as_view(),
         name="cadastrar_registrocupom"),
    path('listar/registrocupom', RegistroCupomListView.as_view(),
         name="listar_registrocupom"),
    path('atualizar/registrocupom/<int:pk>', RegistroCupomCorrecaoUpdateView.as_view(), name="corrigir_registrocupom"),
    path('atualizar/registrocupom/cliente/<int:pk>', RegistroCupomAtualizarClienteView.as_view(),
         name="atualizar_cliente-registrocupom"),
    path('atualizar/registrocupom/validade/<int:pk>', RegistroCupomAtualizarValidadeView.as_view(),
         name="atualizar_validade_registrocupom"),
    path('ajax/desabilitar/registrocupom/<int:pk>', RegistroCupomView.desabilitarRegistroCupom,
         name="ajax_desabilitar_registrocupom"),
    path('ajax/habilitar/registrocupom/<int:pk>', RegistroCupomView.habilitarRegistroCupom,
         name="ajax_habilitar_registrocupom"),



    # cadastrorestaurante
    path('cadastrar/restaurante', CadastroRestauranteCreateView.as_view(),
         name="cadastrar_restaurante"),
    path('listar/restaurante', CadastroRestauranteListView.as_view(),
         name="listar_restaurante"),
    path('atualizar/restaurante/<int:pk>', CadastroRestauranteCorrecaoUpdateView.as_view(),
         name="corrigir_restaurante"),
    path('atualizar/restaurante/observacao/<int:pk>', CadastroRestauranteAtualizarObservacaoView.as_view(),
         name="atualizar_observacao_restaurante"),
    path('atualizar/produto/telefone/<int:pk>', CadastroRestauranteAtualizarTelefoneView.as_view(),
         name="atualizar_telefone_restaurante"),
    path('ajax/desabilitar/restaurante/<int:pk>', CadastroRestauranteView.desabilitarCadastroRestaurante,
         name="ajax_desabilitar_restaurante"),
    path('ajax/habilitar/restaurante/<int:pk>', CadastroRestauranteView.habilitarCadastroRestaurante,
         name="ajax_habilitar_restaurante"),



    # pedido
    path('cadastrar/pedido', FazerPedidoCreateView.as_view(),
         name="cadastrar_pedido"),
    path('listar/pedido', FazerPedidoListView.as_view(),
         name="listar_pedido"),
    path('atualizar/pedido/<int:pk>', FazerPedidoCorrecaoUpdateView.as_view(),
         name="corrigir_pedido"),
    path('atualizar/pedido/local_de_entrega/<int:pk>', FazerPedidoAtualizarLocalDeEntregaView.as_view(),
         name="atualizar_local_de_entrega_pedido"),
    path('atualizar/produto/cliente/<int:pk>', FazerPedidoAtualizarNomeClienteView.as_view(),
         name="atualizar_cliente_pedido"),
    path('ajax/desabilitar/pedido/<int:pk>', FazerPedidoView.desabilitarFazerPedido,
         name="ajax_desabilitar_pedido"),
    path('ajax/habilitar/pedido/<int:pk>', FazerPedidoView.habilitarFazerPedido,
         name="ajax_habilitar_pedido"),
]
