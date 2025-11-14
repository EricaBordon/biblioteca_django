from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .api import AutorViewSet, LibroViewSet

router = DefaultRouter()
router.register(r'api/autores', AutorViewSet, basename='api-autores')
router.register(r'api/libros', LibroViewSet, basename='api-libros')

urlpatterns = [

    # HOME
    path('', views.HomeView.as_view(), name='home'),

    # AUTH
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('register/', views.RegistroView.as_view(), name='register'),

    # AUTORES CRUD
    path('autores/', views.AutorListView.as_view(), name='autor_list'),
    path('autores/crear/', views.AutorCreateView.as_view(), name='autor_create'),
    path('autores/<int:pk>/editar/', views.AutorUpdateView.as_view(), name='autor_update'),
    path('autores/<int:pk>/eliminar/', views.AutorDeleteView.as_view(), name='autor_delete'),

    # LIBROS CRUD
    path('libros/', views.LibroListView.as_view(), name='libro_list'),
    path('libros/crear/', views.LibroCreateView.as_view(), name='libro_create'),
    path('libros/<int:pk>/', views.LibroDetailView.as_view(), name='libro_detail'),
    path('libros/<int:pk>/editar/', views.LibroUpdateView.as_view(), name='libro_update'),
    path('libros/<int:pk>/eliminar/', views.LibroDeleteView.as_view(), name='libro_delete'),

    # PRÉSTAMOS USUARIO
    path('prestamos/mis/', views.MisPrestamosView.as_view(), name='mis_prestamos'),
    path('prestamos/<int:libro_id>/tomar/', views.tomar_prestamo, name='tomar_prestamo'),
    path('prestamos/<int:prestamo_id>/devolver/', views.devolver_prestamo, name='devolver_prestamo'),

    # PRÉSTAMOS ADMIN (esta es la correcta)
    path('prestamos/admin/', views.prestamos_admin, name='prestamos_admin'),

    # API REST
    path('', include(router.urls)),
]

