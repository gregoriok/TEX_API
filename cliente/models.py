from django.db import models

class Cliente(models.Model):
    Nome = models.CharField(max_length=30)
    Documento = models.CharField(max_length=11,unique= True)
    Email = models.CharField(max_length=30)
    Data_nascimento = models.DateField

def __str__(self):
    return self.nome


class Endereco(models.Model):
    Codigo_cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE)
    Cep = models.CharField(max_length=8)
    Uf = models.CharField(max_length=2)
    Bairro = models.CharField(max_length=30)
    Cidade = models.CharField(max_length=30)
    Logradouro = models.CharField(max_length=30)
    Numero = models.IntegerField


def __str__(self):
    return f"{self.Logradouro}, {self.Cidade}, {self.Uf} {self.Cep}"