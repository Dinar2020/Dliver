from django.contrib import admin

from .models import Venda, Produto, Cliente, CadastroBebida, CadastroHamburgue

# Register your models here.

admin.site.register(Venda)
admin.site.register(Produto)
admin.site.register(Cliente)
admin.site.register(CadastroBebida)
admin.site.register(CadastroHamburgue)