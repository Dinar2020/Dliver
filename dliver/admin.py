from django.contrib import admin

from .models import Venda, Cliente, CadastroAtendente, CadastroRestaurante,\
    ClientePegueLeve, Bebida, Hamburguer, Pizza, Passaporte, Pastel, SolicitacaoProduto, EntregaProduto,\
    FormasPagamento, Fornecedor, Produto

# Register your models here.

admin.site.register(Venda)
admin.site.register(Cliente)
admin.site.register(CadastroAtendente)
admin.site.register(CadastroRestaurante)
admin.site.register(ClientePegueLeve)
admin.site.register(Bebida)
admin.site.register(Hamburguer)
admin.site.register(Pizza)
admin.site.register(Passaporte)
admin.site.register(Produto)
admin.site.register(Pastel)
admin.site.register(SolicitacaoProduto)
admin.site.register(EntregaProduto)
admin.site.register(FormasPagamento)
admin.site.register(Fornecedor)