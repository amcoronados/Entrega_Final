from django import forms



class CarreraFormulario(forms.Form):
    nombre_carrera = forms.CharField(max_length = 40)
    ciudad = forms.CharField(max_length = 40)
    pais = forms.CharField(max_length = 20)
    distancia = forms.FloatField()

class GearFormulario(forms.Form):
    tipo_gear = forms.CharField(max_length = 20)
    modelo_gear = forms.CharField(max_length = 60)
    marca = forms.CharField(max_length = 20)
    precio = forms.FloatField()
