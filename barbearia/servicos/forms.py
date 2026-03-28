from django import forms
from .models import Servico


class ServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = ['nome', 'preco']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2.5 bg-[#0a0a0a] border border-[#333333] rounded-lg text-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-600 focus:border-gray-500 transition'
            }),
            'preco': forms.NumberInput(attrs={
                'step': '0.01',
                'class': 'w-full px-4 py-2.5 bg-[#0a0a0a] border border-[#333333] rounded-lg text-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-600 focus:border-gray-500 transition'
            }),
        }