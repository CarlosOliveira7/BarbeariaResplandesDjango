from django import forms
from .models import Barbeiro


class BarbeiroForm(forms.ModelForm):
    class Meta:
        model = Barbeiro
        fields = ['nome', 'email']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'w-full px-4 py-2.5 bg-[#0a0a0a] border border-[#333333] rounded-lg text-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-600 focus:border-gray-500 transition'}),
            'email': forms.EmailInput(attrs={'class': 'w-full px-4 py-2.5 bg-[#0a0a0a] border border-[#333333] rounded-lg text-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-600 focus:border-gray-500 transition'}),
        }