from django.shortcuts import render
from .models import Servico
from .forms import ServicoForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
# Create your views here.

class ServicoCreateView(CreateView):
    model = Servico
    form_class = ServicoForm
    template_name = 'cadastrar_servico.html'
    success_url = reverse_lazy('listar_servicos')

class ServicoListView(ListView):
    model = Servico
    template_name = 'listar_servicos.html'
    context_object_name = 'servicos'