from django.contrib import admin

from .models import Venda, Cliente, CadastroAtendente, CadastroRestaurante,\
    ClientePegueLeve, Bebida, Hamburguer, Pizza, Passaporte, Pastel, FazerPedido, EntregaProduto,\
    FormasPagamento, CadastroFornecedor, CadastroLocalDeEntrega, RegistroCupom, Produto

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
admin.site.register(Pastel)
admin.site.register(FazerPedido)
admin.site.register(EntregaProduto)
admin.site.register(FormasPagamento)
admin.site.register(CadastroFornecedor)
admin.site.register(CadastroLocalDeEntrega)
admin.site.register(RegistroCupom)
admin.site.register(Produto)




