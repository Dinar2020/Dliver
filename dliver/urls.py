from django.contrib import admin
from django.urls import path
from .views import VendaCreateView, VendaListView, VendaUpdateView, ProdutoCreateView,\
    ProdutoUpdateView, ProdutoListView, EntregaProdutoCreateView, EntregaProdutoListView, EntregaProdutoUpdateView,\
    ClienteCreateView, ClienteListView, ClienteUpdateView, ClientePegueLeveCreateView, ClientePegueLeveListView,\
    ClientePegueLeveUpdateView

urlpatterns = [
    path('cadastrar/venda', VendaCreateView.as_view(), name="cadastrar_venda"),
    path('listar/venda', VendaListView.as_view(), name="listar_venda"),
    path('atualizar/venda/<int:pk>', VendaUpdateView.as_view(), name="atualizar_venda"),

    path('cadastrar/produto', ProdutoCreateView.as_view(), name="cadastrar_produto"),
    path('listar/produto', ProdutoListView.as_view(), name="listar_produto"),
    path('atualizar/produto/<int:pk>', ProdutoUpdateView.as_view(), name="atualizar_produto"),

    path('cadastrar/entregaproduto', EntregaProdutoCreateView.as_view(), name="cadastrar_entrega_produto"),
    path('listar/entregaproduto', EntregaProdutoListView.as_view(), name="listar_entrega_produto"),
    path('atualizar/entregaproduto/<int:pk>', EntregaProdutoUpdateView.as_view(), name="atualizar_entrega_produto"),

    path('cadastrar/cliente', ClienteCreateView.as_view(), name="cadastrar_cliente"),
    path('listar/cliente', ClienteListView.as_view(), name="listar_entrega_cliente"),
    path('atualizar/cliente/<int:pk>', ClienteUpdateView.as_view(), name="atualizar_cliente"),

    path('cadastrar/clientepegueleve', ClientePegueLeveCreateView.as_view(), name="cadastrar_clientepegueleve"),
    path('listar/clientepegueleve', ClientePegueLeveListView.as_view(), name="listar_entrega_clientepegueleve"),
    path('atualizar/clientepegueleve/<int:pk>', ClientePegueLeveUpdateView.as_view(), name="atualizar_clientepegueleve"),



]

