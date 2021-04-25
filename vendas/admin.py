from django.contrib import admin

from .models import Venda, Produto, Cliente, Bebida, Hamburgue, Pizza, Passaporte, Pastel, ClientePegueLeve

# Register your models here.

admin.site.register(Venda)
admin.site.register(Produto)
admin.site.register(Cliente)
admin.site.register(ClientePegueLeve)
admin.site.register(Bebida)
admin.site.register(Hamburgue)
admin.site.register(Pizza)
admin.site.register(Passaporte)
admin.site.register(Pastel)