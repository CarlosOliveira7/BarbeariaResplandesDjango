from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.db.models import Sum 

from clientes.models import Cliente
from barbeiros.models import Barbeiro
from agendamentos.models import Agendamento
from servicos.models import Servico
from financeiro.models import Financeiro 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

@login_required
def dashboard(request):
    soma_receitas = Financeiro.objects.filter(tipo='receita').aggregate(Sum('valor'))['valor__sum']
    soma_despesas = Financeiro.objects.filter(tipo='despesa').aggregate(Sum('valor'))['valor__sum']

    total_receitas = soma_receitas if soma_receitas else 0
    total_despesas = soma_despesas if soma_despesas else 0

    context = {
        'total_clientes': Cliente.objects.count(),
        'total_barbeiros': Barbeiro.objects.count(),
        'total_agendamentos': Agendamento.objects.count(),
        'total_servicos': Servico.objects.count(),
        'agendamentos_recentes': Agendamento.objects.order_by('-data')[:5],
        
        'total_receitas': total_receitas,
        'total_despesas': total_despesas,
    }
    
    return render(request, 'dashboard.html', context)



def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('agendamento_list')
    else:
        form = UserCreationForm()
    return render(request, 'auth/registro.html', {'form': form})