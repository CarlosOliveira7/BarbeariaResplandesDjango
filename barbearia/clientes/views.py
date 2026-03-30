from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Cliente
from .forms import ClienteForm
from django.contrib.auth.mixins import LoginRequiredMixin


class ClienteListView(LoginRequiredMixin, ListView):
    model = Cliente
    template_name = 'clientes/cliente_list.html' 
    context_object_name = 'clientes' 

class ClienteCreateView(LoginRequiredMixin,CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'clientes/cliente_form.html'
    success_url = reverse_lazy('cliente_list') 

# Editar Cliente
class ClienteUpdateView(LoginRequiredMixin,UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'clientes/cliente_form.html'
    success_url = reverse_lazy('cliente_list')

# Excluir Cliente
class ClienteDeleteView(LoginRequiredMixin,DeleteView):
    model = Cliente
    template_name = 'clientes/cliente_confirm_delete.html'
    success_url = reverse_lazy('cliente_list')
