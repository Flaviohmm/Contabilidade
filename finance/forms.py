from django import forms
from .models import Ativo, Passivo

class AtivoForm(forms.ModelForm):
    class Meta:
        model = Ativo
        fields = ['nome', 'valor', 'circulante']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded',
                'placeholder': 'Nome do Ativo',
            }), 
            'valor': forms.NumberInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded',
                'placeholder': 'Valor do Ativo',
            }),
            'circulante': forms.CheckboxInput(attrs={
                'class': 'form-checkbox h-5 w-5 text-indigo-600'
            })
        }

class PassivoForm(forms.ModelForm):
    class Meta:
        model = Passivo
        fields = ['nome', 'valor', 'circulante']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded',
                'placeholder': 'Nome do Passivo',
            }),
            'valor': forms.NumberInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded',
                'placeholder': 'Valor do Passivo',
            }),
            'circulante': forms.CheckboxInput(attrs={
                'class': 'form-checkbox h-5 w-5 text-indigo-600'
            })
        }