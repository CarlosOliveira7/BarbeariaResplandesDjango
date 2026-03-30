from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Financeiro
from .forms import FinanceiroForm

class FinanceiroListView(LoginRequiredMixin, ListView):
    model = Financeiro
    template_name = 'financeiro/financeiro_list.html'
    context_object_name = 'lancamentos'

class FinanceiroCreateView(LoginRequiredMixin, CreateView):
    model = Financeiro
    form_class = FinanceiroForm
    template_name = 'financeiro/financeiro_form.html'
    success_url = reverse_lazy('financeiro_list')

class FinanceiroUpdateView(LoginRequiredMixin, UpdateView):
    model = Financeiro
    form_class = FinanceiroForm
    template_name = 'financeiro/financeiro_form.html'
    success_url = reverse_lazy('financeiro_list')

class FinanceiroDeleteView(LoginRequiredMixin, DeleteView):
    model = Financeiro
    template_name = 'financeiro/financeiro_confirm_delete.html'
    success_url = reverse_lazy('financeiro_list')