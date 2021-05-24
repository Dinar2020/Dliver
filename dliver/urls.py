from django.contrib import admin
from django.urls import path
from .views import VendaCreateView, VendaListView, VendaUpdateView, ProdutoCreateView, ProdutoUpdateView, ProdutoListView

urlpatterns = [
    path('cadastrar/venda', VendaCreateView.as_view(), name="cadastrar_venda"),
    path('listar/venda', VendaListView.as_view(), name="listar_venda"),
    path('atualizar/venda/<int:pk>', VendaUpdateView.as_view(), name="atualizar_venda"),

    path('cadastrar/produto', ProdutoCreateView.as_view(), name="cadastrar_produto"),
    path('listar/produto', ProdutoListView.as_view(), name="listar_produto"),
    path('atualizar/produto', ProdutoUpdateView.as_view(), name="atualizar_produto"),

]

