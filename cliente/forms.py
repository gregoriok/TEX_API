from django import forms
from .models import Cliente, Endereco
from cliente.validators import *
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['Nome', 'Documento', 'Email']

    def clean_Documento(self):
        documento = self.cleaned_data.get('Documento')
        if not validate_Documento(documento):
            raise forms.ValidationError('Número do documento inválido')
        return documento

    def clean_Nome(self):
        nome = self.cleaned_data.get('Nome')
        if not validate_Nome(nome):
            raise forms.ValidationError('O Nome deve conter apenas letras')
        return nome

    def clean_Email(self):
        email = self.cleaned_data.get('Email')
        if not validate_Email(email):
            raise forms.ValidationError('Digite um email válido')
        return email
    
class EnderecoForm(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = ['Cep','Uf','Bairro', 'Cidade', 'Logradouro']