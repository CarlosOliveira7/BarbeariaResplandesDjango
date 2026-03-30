from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Agendamento
from .forms import AgendamentoForm

class AgendamentoListView(LoginRequiredMixin, ListView):
    model = Agendamento
    template_name = 'agendamentos/agendamento_list.html'
    context_object_name = 'agendamentos'

class AgendamentoCreateView(LoginRequiredMixin, CreateView):
    model = Agendamento
    form_class = AgendamentoForm        # ← form_class, não fields
    template_name = 'agendamentos/agendamento_form.html'
    success_url = reverse_lazy('agendamento_list')

class AgendamentoUpdateView(LoginRequiredMixin, UpdateView):
    model = Agendamento
    form_class = AgendamentoForm        # ← form_class, não fields
    template_name = 'agendamentos/agendamento_form.html'
    success_url = reverse_lazy('agendamento_list')

class AgendamentoDeleteView(LoginRequiredMixin, DeleteView):
    model = Agendamento
    template_name = 'agendamentos/agendamento_confirm_delete.html'
    success_url = reverse_lazy('agendamento_list')