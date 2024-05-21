from django.urls import path
from . import views
urlpatterns = [
    path("",views.peliculas, name='principal'),
    path("ver/<int:id>/",views.vermas, name='ver')
]