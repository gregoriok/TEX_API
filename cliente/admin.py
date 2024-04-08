from django.contrib import admin
from cliente.models import Cliente,Endereco


class Clientes(admin.ModelAdmin):
    list_display = ('id','Nome','Documento','Email','Data_nascimento')
    list_display_links = ('id','Nome')
    search_fields = ('Nome',)
    list_per_page = 20


admin.site.register(Cliente, Clientes)


class Enderecos(admin.ModelAdmin):
    list_display = ('id','Codigo_cliente','Cep','Uf','Bairro','Cidade','Logradouro','Numero')
    list_display_links = ('id','Cep')
    search_fields = ('Codigo_cliente',)
    list_per_page = 20


admin.site.register(Endereco, Enderecos)