from django.contrib import admin
from .models import Autor, Categoria, Libro, Prestamo


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre")
    search_fields = ("nombre",)


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "slug")
    prepopulated_fields = {"slug": ("nombre",)}
    search_fields = ("nombre",)


@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ("id", "titulo", "autor", "stock")
    list_filter = ("autor", "categorias")
    search_fields = ("titulo", "autor__nombre")


@admin.register(Prestamo)
class PrestamoAdmin(admin.ModelAdmin):
    list_display = ("id", "usuario", "libro", "fecha_prestamo", "devuelto")
    list_filter = ("devuelto", "fecha_prestamo")
    search_fields = ("usuario__username", "libro__titulo")
