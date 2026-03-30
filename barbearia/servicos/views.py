from django.shortcuts import render
from .models import Servico
from .forms import ServicoForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


class ServicoCreateView(LoginRequiredMixin,CreateView):
    model = Servico
    form_class = ServicoForm
    template_name = 'servicos/servico_form.html'
    success_url = reverse_lazy('listar_servicos')


class ServicoListView(LoginRequiredMixin,ListView):
    model = Servico
    template_name = 'servicos/listar_servicos.html'
    context_object_name = 'servicos'


class ServicoUpdateView(LoginRequiredMixin,UpdateView):
    model = Servico
    form_class = ServicoForm
    template_name = 'servicos/servico_form.html'
    success_url = reverse_lazy('listar_servicos')


class ServicoDeleteView(LoginRequiredMixin,DeleteView):
    model = Servico
    template_name = 'servicos/servico_confirm_delete.html'
    success_url = reverse_lazy('listar_servicos')