from django.shortcuts import render
from .models import *
from AppJoyeria.forms import *
from django.db.models import Q #para realizar consultas mas complejas
#from django.http import HttpResponse
# Create your views here.
def inicio(request):
    return render(request,"AppJoyeria/inicio.html")

def articulos(request):
    return render(request,"AppJoyeria/articulos.html")

def clientes(request):
    return render(request, "AppJoyeria/clientes.html")

def ventas(request):
    return render(request, "AppJoyeria/ventas.html")

def CargaArt(request):

    if request.method == "POST":

            miFormulario = Articuloformulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)

            if miFormulario.is_valid():
                informacion = miFormulario.cleaned_data
                articulo = Articulo(idArt=informacion["idArt"], nomArt=informacion["nomArt"],precioArt=informacion["precioArt"],material=informacion["material"])
                articulo.save()
                return render(request, "AppJoyeria/inicio.html")
    else:
            miFormulario = Articuloformulario()

    return render(request, "AppJoyeria/cargaArt.html", {"miFormulario": miFormulario})

def leerArticulos(request):

    articulos = Articulo.objects.all() #trae todos los Articulos

    contexto= {"articulos":articulos} 

    return render(request, "AppJoyeria/leerArticulos.html",contexto)

def buscarArt(request):
    if request.method == "POST":
        mi_formulario = BucarArtForm(request.POST)  # Aquí me llega la información del HTML

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            
            # Utilizo Q para combinar los filtros de búsqueda
            query = Q()
            if informacion["idArt"]:
                query &= Q(idArt__icontains=informacion["idArt"])
            if informacion["nomArt"]:
                query &= Q(nomArt__icontains=informacion["nomArt"])
            if informacion["material"]:
                query &= Q(material__icontains=informacion["material"])

            articulos = Articulo.objects.filter(query)

            return render(request, "AppJoyeria/leerArticulos.html", {"articulos": articulos})
    else:
        mi_formulario = BucarArtForm()

    return render(request, "AppJoyeria/buscarArt.html", {"mi_formulario": mi_formulario})

def CargaCliente(request):

    if request.method == "POST":

            miFormulario = ClienteForm(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)

            if miFormulario.is_valid():
                informacion = miFormulario.cleaned_data
                clientes = Cliente(idCliente=informacion["idCliente"], nombre=informacion["nombre"],apellido=informacion["apellido"],mail=informacion["mail"])
                clientes.save()
                return render(request, "AppJoyeria/inicio.html")
    else:
            miFormulario = ClienteForm()

    return render(request, "AppJoyeria/cargaCliente.html", {"miFormulario": miFormulario})

def leerClientes(request):

    clientes = Cliente.objects.all() #trae todos los Clientes

    contexto= {"clientes":clientes} 

    return render(request, "AppJoyeria/leerClientes.html",contexto)

def CargaVentas(request):

    if request.method == "POST":

            miFormulario = VentaForm(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)

            if miFormulario.is_valid():
                informacion = miFormulario.cleaned_data
                ventas = Venta(idVenta=informacion["idVenta"], fecha=informacion["fecha"],idCliente=informacion["idCliente"],idArt=informacion["idArt"],cant=informacion["cant"],montoVta=informacion["montoVta"],tipoPago=informacion["tipoPago"])
                ventas.save()
                return render(request, "AppJoyeria/inicio.html")
    else:
            miFormulario = VentaForm()

    return render(request, "AppJoyeria/cargaVentas.html", {"miFormulario": miFormulario})

def leerVentas(request):

    ventas = Venta.objects.all() #trae todos las ventas

    contexto= {"ventas":ventas} 

    return render(request, "AppJoyeria/leerVentas.html",contexto)

