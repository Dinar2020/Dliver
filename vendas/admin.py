from django.contrib import admin

from .models import Venda, Produto, Cliente, CadastroAtendente, CadastroLocalDeEntrega, CadastroRestaurante,\
    ClientePegueLeve, Bebida, Hamburgue, Pizza, Passaporte, Pastel, SolicitacaoRetiradaEstoque,EntregaProduto

# Register your models here.

admin.site.register(Venda)
admin.site.register(Produto)
admin.site.register(Cliente)
admin.site.register(CadastroAtendente)
admin.site.register(CadastroLocalDeEntrega)
admin.site.register(CadastroRestaurante)
admin.site.register(ClientePegueLeve)
admin.site.register(Bebida)
admin.site.register(Hamburgue)
admin.site.register(Pizza)
admin.site.register(Passaporte)
admin.site.register(Pastel)
admin.site.register(SolicitacaoRetiradaEstoque)
admin.site.register(EntregaProduto)