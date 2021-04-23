from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView
from .models import Venda, Produto, CadastroBebida, CadastroHamburgue
from django.urls import reverse_lazy
# Create your views here.

class VendaCreateView(CreateView):
    model = Venda
    template_name = 'cadastrar/venda.html'

    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy("listar_venda")


class ProdutoCreateView(CreateView):
    model = Produto
    template_name = 'cadastrar/produto.html'

    # Caso eu queira que sejam cadastrados todos os fields do meu Model você colocará o fields = '__all__'
    # Caso queira especificar, colocar da forma abaixo. Por exemplo, se quiser apenas nome colocar fields = ['nome']
    fields = ['nome', 'valor']

    def get_success_url(self):
        return reverse_lazy('cadastrar_produto')


class VendaListView(ListView):
    model = Venda
    template_name = 'listar/venda.html'
    paginate_by = 3


class VendaUpdateView(UpdateView):
    model = Venda
    template_name = 'atualizar/venda.html'

    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('listar_venda')



class BebidaCreateView(CreateView):
    model = CadastroBebida
    template_name = 'cadastrar/bebida.html'

    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy("listar_bebida")


class BebidaListView(ListView):
    model = CadastroBebida
    template_name = 'listar/bebida.html'
    paginate_by = 3


class BebidaUpdateView(UpdateView):
    model = CadastroBebida
    template_name = 'atualizar/bebida.html'

    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('listar_bebida')




class HamburgueCreateView(CreateView):
    model = CadastroHamburgue
    template_name = 'cadastrar/hamburgue.html'

    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy("listar_humburgue")


class HamburgueListView(ListView):
    model = CadastroHamburgue
    template_name = 'listar/hamburgue.html'
    paginate_by = 3


class HamburgueUpdateView(UpdateView):
    model = CadastroHamburgue
    template_name = 'atualizar/hamburgue.html'

    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('listar_hamburgue')





