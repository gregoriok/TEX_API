from django import forms
from .models import Cliente, Endereco

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['id','Nome', 'Documento', 'Email']

class EnderecoForm(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = ['Cep','Uf','Bairro', 'Cidade', 'Logradouro']