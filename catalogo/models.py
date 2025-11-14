from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.text import slugify


class Autor(models.Model):
    nombre = models.CharField(max_length=150)
    bio = models.TextField(blank=True)

    class Meta:
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre


class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True)

    class Meta:
        verbose_name_plural = "Categorías"
        ordering = ["nombre"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nombre)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre


class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='libros')
    categorias = models.ManyToManyField(Categoria, related_name='libros', blank=True)
    stock = models.PositiveIntegerField(default=0)
    fecha_publicacion = models.DateField(null=True, blank=True)
    imagen = models.ImageField(upload_to="libros/", null=True, blank=True)
    class Meta:
        ordering = ["titulo"]

    def clean(self):
        if self.stock < 0:
            raise ValidationError({"stock": "El stock no puede ser negativo."})

    def __str__(self):
        return self.titulo


class Prestamo(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='prestamos')
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name='prestamos')
    fecha_prestamo = models.DateField(auto_now_add=True)
    fecha_devolucion = models.DateField(null=True, blank=True)
    devuelto = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Préstamo"
        verbose_name_plural = "Préstamos"
        ordering = ["-fecha_prestamo"]

    def __str__(self):
        return f"{self.usuario.username} -> {self.libro.titulo} ({'devuelto' if self.devuelto else 'pendiente'})"
