from rest_framework import serializers
from cliente.models import Cliente,Endereco
from cliente.validators import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    def validate(self, data):
        if not validate_Documento(data['Documento']):
            raise serializers.ValidationError({'Documento':"Número do documento inválido"})
        if not validate_Nome(data['Nome']):
            raise serializers.ValidationError({'nome':"O Nome deve conter apenas letras"})
        if not validate_Email(data['Email']):
            raise serializers.ValidationError({'Email':"Digite um email válido"})
        return data
    
class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = '__all__'

class ListaEnderecosClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = ['id','Cep','Uf','Bairro','Cidade','Logradouro']