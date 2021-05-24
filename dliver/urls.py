from django.contrib import admin
from django.urls import path
from .views import VendaCreateView, VendaListView, VendaUpdateView, ProdutoCreateView, ProdutoUpdateView, ProdutoListView

urlpatterns = [
    path('cadastrar/venda', VendaCreateView.as_view(), name="cadastrar_venda"),
    path('listar/venda', VendaListView.as_view(), name="listar_venda"),
    path('atualizar/venda/<int:pk>', VendaUpdateView.as_view(), name="atualizar_venda"),

    path('cadastrar/produto', ProdutoCreateView.as_view(), name="cadastrar_produto"),
    path('listar/produto', ProdutoListView.as_view(), name="listar_produto"),
    path('atualizar/produto/<int:pk>', ProdutoUpdateView.as_view(), name="atualizar_produto"),

    path('cadastrar/entregaproduto', ProdutoCreateView.as_view(), name="cadastrar_entrega_produto"),
    path('listar/entregaproduto', ProdutoListView.as_view(), name="listar_entrega_produto"),
    path('atualizar/entregaproduto/<int:pk>', ProdutoUpdateView.as_view(), name="atualizar_entrega_produto"),





]

