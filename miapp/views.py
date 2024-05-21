from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models


# Create your views here.
def peliculas(request):
    consultaall = models.Peliculas.objects.all()
    datos = {
        'datos1':consultaall,
    }
    return render(request, '2-quiz-index.html', datos)

def vermas(request, id_pelicula):
    print("aquiiiiiiiii")
    print(type(id_pelicula))
    print((id_pelicula))
    dato = models.Peliculas.objects.get(id=id_pelicula)
    print((dato))

    return render(request,'3-ver-mas.html', {'dato_persona': dato})