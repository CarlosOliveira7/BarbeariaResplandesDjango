from django import forms
from .models import Servico, Agendamento, Barbeiro, Cliente

class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = ['data', 'barbeiro', 'cliente', 'status', 'servicos']
        widgets = {
            'data': forms.DateTimeInput(
                attrs={
                    'type': 'datetime-local',
                    'class': 'w-full px-4 py-2.5 bg-[#0a0a0a] border border-[#333333] rounded-lg text-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-600 focus:border-gray-500 transition'
                }
            ),
            'barbeiro': forms.Select(attrs={
                'class': 'w-full px-4 py-2.5 bg-[#0a0a0a] border border-[#333333] rounded-lg text-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-600 focus:border-gray-500 transition'
            }),
            'cliente': forms.Select(attrs={
                'class': 'w-full px-4 py-2.5 bg-[#0a0a0a] border border-[#333333] rounded-lg text-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-600 focus:border-gray-500 transition'
            }),
            'status': forms.TextInput(attrs={
                'placeholder': 'Ex: Pendente, Confirmado',
                'class': 'w-full px-4 py-2.5 bg-[#0a0a0a] border border-[#333333] rounded-lg text-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-600 focus:border-gray-500 transition'
            }),
            'servicos': forms.SelectMultiple(attrs={
                'class': 'w-full px-4 py-2.5 bg-[#0a0a0a] border border-[#333333] rounded-lg text-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-600 focus:border-gray-500 transition'
            }),
        }