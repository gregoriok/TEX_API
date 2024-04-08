"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from cliente.views import *
from rest_framework import routers

from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register('clientes',ClientesViewSet, basename='Clientes')
router.register('Enderecos',EnderecosViewSet, basename='Enderecos')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clientes/<int:cliente_id>/enderecos/', enderecos_cliente , name='enderecos_cliente'),
    path('lista_clientes/', clientes_view, name='clientes'),
    path('adicionar_cliente/', adicionar_cliente, name='adicionar_cliente'),
    path('editar_cliente/<int:cliente_id>/', editar_cliente, name='editar_cliente'),
    path('adicionar_endereco/<int:cliente_id>/', adicionar_endereco, name='adicionar_endereco'),
    path('clientes/<int:cliente_id>/excluir/', excluir_cliente, name='excluir_cliente'),
    path('preencher_endereco/', preencher_endereco, name='preencher_endereco'),
    path('excluir_endereco/<int:endereco_id>/', excluir_endereco, name='excluir_endereco'),
    path('',include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)