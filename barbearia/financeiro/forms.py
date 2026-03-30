from django import forms
from .models import Financeiro

INPUT_CLASS = 'w-full px-4 py-2.5 bg-[#0a0a0a] border border-[#333333] rounded-lg text-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-600 focus:border-gray-500 transition'

class FinanceiroForm(forms.ModelForm):
    class Meta:
        model = Financeiro
        fields = ['tipo', 'descricao', 'valor', 'data_lancamento', 'agendamento']
        widgets = {
            'tipo': forms.Select(attrs={'class': INPUT_CLASS}),
            'descricao': forms.TextInput(attrs={'class': INPUT_CLASS, 'placeholder': 'Descrição do lançamento'}),
            'valor': forms.NumberInput(attrs={'class': INPUT_CLASS, 'placeholder': '0.00', 'step': '0.01'}),
            'data_lancamento': forms.DateTimeInput(attrs={'class': INPUT_CLASS, 'type': 'datetime-local'}),
            'agendamento': forms.Select(attrs={'class': INPUT_CLASS}),
        }