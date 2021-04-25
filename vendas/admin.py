from django.contrib import admin

from .models import Venda, Produto, Cliente, CadastroAtendente, CadastroLocalDeEntrega

# Register your models here.

admin.site.register(Venda)
admin.site.register(Produto)
admin.site.register(Cliente)
admin.site.register(CadastroAtendente)
admin.site.register(CadastroLocalDeEntrega)