from rest_framework import viewsets
from cliente.models import Cliente, Endereco
from cliente.serializer import ClienteSerializer, EnderecoSerializer
from django.shortcuts import redirect, render, get_object_or_404
from cliente.forms import ClienteForm, EnderecoForm
from django.http import JsonResponse
from cliente.api import preencher_endereco_por_cep
import logging


class ClientesViewSet(viewsets.ModelViewSet):
    """Exibindo todos os clientes"""
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class EnderecosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os Enderecos"""
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer
    
def clientes_view(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes.html', {'clientes': clientes})

def adicionar_cliente(request):
    cliente = None
    botao_texto = 'Adicionar Cliente'
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            clientes = Cliente.objects.all()
            return render(request, 'clientes.html', {'clientes': clientes})
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'adicionar_cliente.html', {'form': form, 'botao_texto': botao_texto})

def editar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            clientes = Cliente.objects.all()
            return render(request, 'clientes.html', {'clientes': clientes})
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'editar_cliente.html', {'form': form, 'cliente': cliente})


def excluir_cliente(request, cliente_id):
    cliente = Cliente.objects.get(pk=cliente_id)
    cliente.delete()
    clientes = Cliente.objects.all()
    return render(request, 'clientes.html', {'clientes': clientes})

def enderecos_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    enderecos = Endereco.objects.filter(Codigo_cliente_id=cliente_id)

    return render(request, 'enderecos_cliente.html', {'cliente': cliente, 'enderecos': enderecos})

# FUNÇÕES RELACIONADAS AO ENDEREÇO

def adicionar_endereco(request, cliente_id):
    cliente = Cliente.objects.get(pk=cliente_id)
    if request.method == 'POST':
        form = EnderecoForm(request.POST)
        if form.is_valid():
            endereco = form.save(commit=False)
            endereco.Codigo_cliente = cliente
            endereco.save()
            return redirect('enderecos_cliente', cliente_id=cliente_id)
        else:
        #  logging.error(f'Erro ao validar o formulário de endereço para o cliente com ID {cliente_id}')
        #  for field_name, errors in form.errors.items():
        #         for error in errors:
        #             logging.error(f"{field_name}: {error}")
         clientes = Cliente.objects.all()
         return render(request, 'clientes.html', {'clientes': clientes})   
    else:
        form = EnderecoForm()
    return render(request, 'adicionar_endereco.html', {'form': form, 'cliente': cliente})

def preencher_endereco(request):
    if request.method == 'POST':
        cep = request.POST.get('cep')
        logradouro, cidade, uf = preencher_endereco_por_cep(cep)
        return JsonResponse({'logradouro': logradouro, 'cidade': cidade, 'uf': uf})
    return JsonResponse({}, status=400)

def excluir_endereco(request, endereco_id):
    endereco = get_object_or_404(Endereco, pk=endereco_id)
    cliente_id = endereco.Codigo_cliente.id
    endereco.delete()
    return redirect('enderecos_cliente', cliente_id=cliente_id)