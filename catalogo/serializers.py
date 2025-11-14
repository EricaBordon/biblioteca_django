from rest_framework import serializers
from .models import Autor, Libro, Categoria


class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = ["id", "nombre", "bio"]


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ["id", "nombre", "slug"]


class LibroSerializer(serializers.ModelSerializer):
    autor = AutorSerializer(read_only=True)
    autor_id = serializers.PrimaryKeyRelatedField(
        queryset=Autor.objects.all(), source='autor', write_only=True
    )
    categorias = CategoriaSerializer(many=True, read_only=True)
    categorias_ids = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Categoria.objects.all(), source='categorias', write_only=True
    )

    class Meta:
        model = Libro
        fields = [
            "id", "titulo", "autor", "autor_id", "categorias", "categorias_ids",
            "stock", "fecha_publicacion"
        ]
