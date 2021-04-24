from django.contrib import admin
from django.urls import path
from .views import VendaCreateView, ProdutoCreateView, VendaListView, VendaUpdateView, BebidaCreateView, BebidaListView, BebidaUpdateView, HamburgueCreateView, HamburgueListView, HamburgueUpdateView, PizzaCreateView, PizzaListView, PizzaUpdateView, PassaporteCreateView, PassaporteUpdateView, PassaporteListView, PastelCreateView, PastelListView, PastelUpdateView

urlpatterns = [
    path('cadastrar/venda', VendaCreateView.as_view(), name="cadastrar_venda"),
    path('listar/venda', VendaListView.as_view(), name="listar_venda"),
    path('atualizar/venda/<int:pk>', VendaUpdateView.as_view(), name="atualizar_venda"),


    path('cadastrar/produto', ProdutoCreateView.as_view(), name="cadastrar_produto"),


    path('cadastrar/bebida', BebidaCreateView.as_view(), name="cadastrar_bebida"),
    path('listar/bebida', BebidaListView.as_view(), name="listar_bebida"),
    path('atualizar/venda/<int:pk>', BebidaUpdateView.as_view(), name="atualizar_bebida"),


    path('cadastrar/hamburgue', HamburgueCreateView.as_view(), name="cadastrar_hamburgue"),
    path('listar/hamburgue', HamburgueListView.as_view(), name="listar_hamburgue"),
    path('atualizar/venda/<int:pk>', HamburgueUpdateView.as_view(), name="atualizar_hamburgue"),


    path('cadastrar/pizza', PizzaCreateView.as_view(), name="cadastrar_pizza"),
    path('listar/pizza', PizzaListView.as_view(), name="listar_pizza"),
    path('atualizar/venda/<int:pk>', PizzaUpdateView.as_view(), name="atualizar_pizza"),


    path('cadastrar/passaporte', PassaporteCreateView.as_view(), name="cadastrar_pizza"),
    path('listar/passaporte', PassaporteListView.as_view(), name="listar_pizza"),
    path('atualizar/venda/<int:pk>', PassaporteUpdateView.as_view(), name="atualizar_pizza"),

    path('cadastrar/pastel', PastelCreateView.as_view(), name="cadastrar_pastel"),
    path('listar/pastel', PastelListView.as_view(), name="listar_pastel"),
    path('atualizar/venda/<int:pk>', PastelUpdateView.as_view(), name="atualizar_pastel"),

]

