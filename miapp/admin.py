from django.contrib import admin
from .models import Peliculas
# Register your models here.

class PeliculasAdmin(admin.ModelAdmin):
    list_display = ['id','titulo']
    search_fields = ['titulo']
    list_filter = ['titulo']

admin.site.register(Peliculas,PeliculasAdmin)
