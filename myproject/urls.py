"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from myBlog.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("about/", ver_about, name="About"),
    #url para los modelos creados
    path("carrera/", ver_carrera, name="carrera"),
    path("gear/", ver_gear, name = "gear"),
    path("", inicio, name = "inicio"),
    #url para crear nuevos datos
    path("nueva_carrera/", agregar_carrera, name="nueva carrera"),
    path("nuevo_gear/", agregar_gear, name="nuevo gear"),
    #url para buscar datos
    path("buscarCarreraCiudad/", buscar_carrera),
    path("resultadosCarrera/", resultado_buscar_carrera),
    #url para actualizar carrera
    path("actualizarCarrera/<carrera_nombre>", actualizar_carrera, name="actualizar carrera"),
    #url borrar carrera
    path("eliminarCarrera/<carrera_nombre>", eliminar_carrera, name="Eliminar carrera"),
    #url registro/inicio de sesion
    path("signup/", registro, name="Registrar Usuario"),
    path("login/", inicio_sesion, name="Iniciar Sesion"),
    path("logout/", cerrar_sesion, name = "Cerrar Sesion"),
]
