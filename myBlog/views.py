from django.shortcuts import render
from django.http import HttpResponse
from myBlog.models import *
from myBlog.forms import *
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

##Visualizar

def ver_about(request):
    return render(request, "About.html")

#Read
@login_required
def ver_carrera(request):
    mis_carreras = Carrera.objects.all()
    info = {"carreras":mis_carreras}
    return render(request, "carrera.html", info)

@login_required
def ver_gear(request):
    mis_gears = Gear.objects.all()
    info = {"gears":mis_gears}
    return render(request, "gear.html", info)

def inicio(request):
    return render(request, "inicio.html")

## Create
def agregar_carrera(request):
    nuevo_carreraformulario=CarreraFormulario()
    if request.method == "POST":
        nuevo_carreraformulario=CarreraFormulario(request.POST)
        if nuevo_carreraformulario.is_valid():
            info_carrera=nuevo_carreraformulario.cleaned_data
            carrera_nueva = Carrera(nombre_carrera=info_carrera["nombre_carrera"], ciudad=info_carrera["ciudad"], pais=info_carrera["pais"], distancia=info_carrera["distancia"])
            carrera_nueva.save()
            return render(request, "inicio.html")
    return render(request, "formu_carrera.html", {"mi_formu_carrera":nuevo_carreraformulario})

def agregar_gear(request):
    nuevo_gearformulario=GearFormulario()
    if request.method == "POST":
        nuevo_gearformulario=GearFormulario(request.POST)
        if nuevo_gearformulario.is_valid():
            info_gear=nuevo_gearformulario.cleaned_data
            gear_nuevo = Gear(tipo_gear=info_gear["tipo_gear"], modelo_gear=info_gear["modelo_gear"], marca=info_gear["marca"], precio=info_gear["precio"])
            gear_nuevo.save()
            return render(request, "inicio.html")
    return render(request, "formu_gear.html", {"mi_formu_gear":nuevo_gearformulario})

def buscar_carrera(request):
    return render(request, "buscar_carrera_ciudad.html")

def resultado_buscar_carrera(request):
    if request.method == "GET":
        ciudad_buscada = request.GET["ciudad"]
        resultados_carrera = Carrera.objects.filter(ciudad__icontains = ciudad_buscada)
        return render(request, "buscar_carrera_ciudad.html", {"carreras":resultados_carrera})
    else:
        return render (request,"buscar_carrera_ciudad.html" )

#Update
def actualizar_carrera(request, carrera_nombre):
    nuevo_carreraformulario=CarreraFormulario()
    carrera_escogida = Carrera.objects.get(nombre_carrera=carrera_nombre)
    if request.method == "POST":
        nuevo_carreraformulario=CarreraFormulario(request.POST)
        if nuevo_carreraformulario.is_valid():
            info_carrera=nuevo_carreraformulario.cleaned_data
            carrera_escogida.nombre = info_carrera["nombre_carrera"]
            carrera_escogida.nombre = info_carrera["ciudad"]
            carrera_escogida.nombre = info_carrera["pais"]
            carrera_escogida.nombre = info_carrera["distancia"]  
            carrera_escogida.save()
            return render(request, "inicio.html")
    return render(request, "update_carrera.html", {"mi_formu_carrera":nuevo_carreraformulario})

#Delete
def eliminar_carrera(request, carrera_nombre):
    nuevo_carreraformulario=CarreraFormulario()
    carrera_escogida = Carrera.objects.get(nombre_carrera=carrera_nombre)
    carrera_escogida.delete()
    return render(request, "carrera.html")

#Vistas de register/login/logout

def inicio_sesion(request):
    formulario = AuthenticationForm()
    if request.method == "POST":
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            usuario=info["username"]
            contra= info["password"]
            usuario_actual=authenticate(username=usuario, password=contra)
            if usuario_actual is not None:
                login(request, usuario_actual)
                return render(request, "inicio.html", {"mensaje":f"Bienvenido/a {usuario}"})   
        else:
            return render(request, "inicio.html", {"mensaje":"Error, datos incorrectos"})
    formulario = AuthenticationForm()    
    return render(request, "inicio_sesion.html", {"formu":formulario})

def registro(request):
    formulario = UserCreationForm()
    if request.method=="POST":
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid():
            info=formulario.cleaned_data
            usuario=info["username"]
            formulario.save()
            return render(request, "inicio.html", {"mensaje":f"Bienvenido/a {usuario}"})
    else:
        formulario=UserCreationForm()
    return render(request, "registrar_usuario.html", {"formu":formulario})

def cerrar_sesion(request):
    logout(request)
    return render(request, "cerrar_sesion.html")


