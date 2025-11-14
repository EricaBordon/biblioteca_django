from rest_framework import viewsets, permissions, filters
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from .models import Autor, Libro
from .serializers import AutorSerializer, LibroSerializer


class IsStaffOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated and request.user.is_staff


class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsStaffOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ["nombre"]


class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.select_related('autor').prefetch_related('categorias').all()
    serializer_class = LibroSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsStaffOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ["titulo", "autor__nombre", "categorias__nombre"]
