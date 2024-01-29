from django.shortcuts import render
from django.http import HttpResponse
from myBlog.models import *

    
# Create your views here.

def ver_carrera(request):
    mis_carreras = Carrera.objects.all()
    info = {"carreras":mis_carreras}
    return render(request, "carrera.html", info)


def ver_gear(request):
    mis_gears = Gear.objects.all()
    info = {"gears":mis_gears}
    return render(request, "gear.html", info)


def inicio(request):
    return render(request, "inicio.html")




"""
def agregar_carrera(request):

    carrera1 = Carrera(nombre_carrera="UTCB", ciudad="Huaraz", pais="Peru", distancia =21.0)       #crear un objeto
    carrera1.save()

    return HttpResponse("Se agregó una carrera")




def agregar_gear(request):

    gear1 = Gear(tipo_gear = "chaleco", modelo_gear = "Montrail", marca = "Columbia", precio=699.9)
    gear1.save()

    return HttpResponse("Se agregó un gear")
"""
