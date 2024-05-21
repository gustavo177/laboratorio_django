from django.urls import path
from . import views
urlpatterns = [
    path("",views.peliculas, name='principal'),
    path("ver/<int:id_pelicula>/",views.vermas, name='ver')
]