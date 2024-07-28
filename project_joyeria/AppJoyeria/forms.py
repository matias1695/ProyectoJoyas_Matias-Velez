from django import forms   

class Articuloformulario(forms.Form):
    idArt=forms.CharField(max_length=5)#A****
    nomArt=forms.CharField(max_length=30)
    precioArt=forms.FloatField()
    material=forms.CharField(max_length=10)
    
class BucarArtForm(forms.Form):
    idArt=forms.CharField()
    nomArt=forms.CharField()
    material=forms.CharField()
    
class ClienteForm(forms.Form):
    idCliente=forms.CharField(max_length=5)#C****
    nombre=forms.CharField(max_length=10)
    apellido=forms.CharField(max_length=10)
    mail=forms.EmailField()

class BuscarClienteForm(forms.Form):
    nombre=forms.CharField()
    apellido=forms.CharField()
    
class VentaForm(forms.Form):
    idVenta=forms.CharField()
    fecha=forms.DateField()
    idCliente=forms.CharField()
    idArt=forms.CharField()
    cant=forms.IntegerField()
    montoVta=forms.FloatField()
    tipoPago=forms.CharField()
    
class BuscarVenta(forms.Form):
    fecha=forms.DateField()
    tipoPago=forms.CharField()
