from django.shortcuts import render
from .models import Barbeiro
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import BarbeiroForm
from django.contrib.auth.mixins import LoginRequiredMixin

class BarbeiroListView(LoginRequiredMixin,ListView):
    model = Barbeiro
    template_name = 'barbeiros/barbeiro_list.html'
    context_object_name = 'barbeiros'

class BarbeiroCreateView(LoginRequiredMixin,CreateView):
    model = Barbeiro
    form_class = BarbeiroForm
    template_name = 'barbeiros/barbeiro_form.html'
    success_url = reverse_lazy('barbeiro_list') 

# Editar Barbeiro
class BarbeiroUpdateView(LoginRequiredMixin,UpdateView):
    model = Barbeiro
    form_class = BarbeiroForm
    template_name = 'barbeiros/barbeiro_form.html'
    success_url = reverse_lazy('barbeiro_list')

# Excluir Barbeiro
class BarbeiroDeleteView(LoginRequiredMixin,DeleteView):
    model = Barbeiro
    template_name = 'barbeiros/barbeiro_confirm_delete.html'
    success_url = reverse_lazy('barbeiro_list')

