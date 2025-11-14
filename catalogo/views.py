from django.contrib import messages
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import AutorForm, LibroForm, RegistroForm
from .models import Autor, Libro, Prestamo


# ============================================================
# HOME
# ============================================================
class HomeView(ListView):
    model = Libro
    template_name = 'libros/list.html'
    context_object_name = 'libros'
    paginate_by = 8


# ============================================================
# MIXIN PARA STAFF
# ============================================================
class StaffRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_staff


# ============================================================
# AUTENTICACIÓN
# ============================================================
class UserLoginView(auth_views.LoginView):
    template_name = 'auth/login.html'


class UserLogoutView(auth_views.LogoutView):
    next_page = reverse_lazy('home')


class RegistroView(CreateView):
    form_class = RegistroForm
    template_name = 'auth/register.html'
    success_url = reverse_lazy('login')


# ============================================================
# AUTORES CRUD
# ============================================================
class AutorListView(LoginRequiredMixin, ListView):
    model = Autor
    template_name = 'autores/list.html'
    context_object_name = 'autores'


class AutorCreateView(StaffRequiredMixin, CreateView):
    model = Autor
    form_class = AutorForm
    template_name = 'autores/form.html'
    success_url = reverse_lazy('autor_list')


class AutorUpdateView(StaffRequiredMixin, UpdateView):
    model = Autor
    form_class = AutorForm
    template_name = 'autores/form.html'
    success_url = reverse_lazy('autor_list')


class AutorDeleteView(StaffRequiredMixin, DeleteView):
    model = Autor
    template_name = 'autores/confirm_delete.html'
    success_url = reverse_lazy('autor_list')


# ============================================================
# LIBROS CRUD
# ============================================================
class LibroListView(ListView):
    model = Libro
    template_name = 'libros/list.html'
    context_object_name = 'libros'
    paginate_by = 8


class LibroDetailView(DetailView):
    model = Libro
    template_name = 'libros/detail.html'
    context_object_name = 'libro'


class LibroCreateView(StaffRequiredMixin, CreateView):
    model = Libro
    form_class = LibroForm
    template_name = 'libros/form.html'
    success_url = reverse_lazy('libro_list')


class LibroUpdateView(StaffRequiredMixin, UpdateView):
    model = Libro
    form_class = LibroForm
    template_name = 'libros/form.html'
    success_url = reverse_lazy('libro_list')


class LibroDeleteView(StaffRequiredMixin, DeleteView):
    model = Libro
    template_name = 'libros/confirm_delete.html'
    success_url = reverse_lazy('libro_list')


# ============================================================
# PRÉSTAMOS USUARIO NORMAL
# ============================================================
class MisPrestamosView(LoginRequiredMixin, ListView):
    model = Prestamo
    template_name = 'prestamos/mis_prestamos.html'
    context_object_name = 'prestamos'

    def get_queryset(self):
        return Prestamo.objects.filter(
            usuario=self.request.user
        ).select_related('libro')


# ============================================================
# TOMAR PRESTAMO
# ============================================================
@login_required
@transaction.atomic
def tomar_prestamo(request, libro_id):
    libro = get_object_or_404(Libro, id=libro_id)

    if libro.stock <= 0:
        messages.error(request, 'No hay stock disponible para este libro.')
        return redirect('libro_detail', pk=libro_id)

    libro.stock -= 1
    libro.save()

    Prestamo.objects.create(usuario=request.user, libro=libro)

    messages.success(request, 'Préstamo realizado correctamente.')
    return redirect('mis_prestamos')


# ============================================================
# DEVOLVER PRÉSTAMO
# ============================================================
@login_required
@transaction.atomic
def devolver_prestamo(request, prestamo_id):
    prestamo = get_object_or_404(
        Prestamo,
        id=prestamo_id,
        usuario=request.user
    )

    if not prestamo.devuelto:
        prestamo.devuelto = True
        prestamo.save()

        prestamo.libro.stock += 1
        prestamo.libro.save()

        messages.success(request, 'Devolución registrada.')
    else:
        messages.info(request, 'Este préstamo ya estaba devuelto.')
    
    return redirect('mis_prestamos')


# ============================================================
# PRÉSTAMOS ADMIN (TODOS LOS USUARIOS)
# ============================================================
@login_required
def prestamos_admin(request):
    if not request.user.is_staff:
        return render(request, "403.html", status=403)

    prestamos = Prestamo.objects.select_related('libro', 'usuario').all()

    return render(request, 'prestamostotal/mis_prestamos.html', {
        'prestamos': prestamos
    })
