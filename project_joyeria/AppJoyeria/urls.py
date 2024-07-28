"""
URL configuration for project_joyeria project.

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
from django.urls import path
from . import views

urlpatterns = [
    path('',views.inicio,name="inicio"),
    path('articulos',views.articulos,name="articulos"),
    path('clientes',views.clientes,name="clientes"),
    path('ventas',views.ventas,name="ventas"),
    path('cargaArt/',views.CargaArt,name="cargaArticulo"),
    path('leerArt/',views.leerArticulos,name="leerArticulos"),
    path('buscarArt/', views.buscarArt, name="buscarArticulos"),
    path('cargaCliente/',views.CargaCliente,name="cargaCliente"),
    path('leerClientes/',views.leerClientes,name="leerClientes"),
    path('cargaVentas/',views.CargaVentas,name="cargaVentas"),
    path('leerVentas/',views.leerVentas,name="leerVentas"),
    
    
]
