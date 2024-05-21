from django.shortcuts import render, redirect
from django.http import HttpResponse


# Create your views here.
def peliculas(request):
    datos = {
        'titulo':'juan',
        'descripsion':'balbalab blablabl'
    }
    return render(request, '2-quiz-index.html', datos)

def vermas(request, id):
    print("aquiiiiiiiii")
    print(type(id))
    print((id))
    return render(request,'3-ver-mas.html')