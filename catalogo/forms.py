from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Autor, Libro


class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ["nombre", "bio"]
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "bio": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
        }


class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ["titulo", "autor", "categorias", "stock", "fecha_publicacion", "imagen"]

        widgets = {
            "titulo": forms.TextInput(attrs={"class": "form-control"}),
            "autor": forms.Select(attrs={"class": "form-select"}),

            # ✔ CATEGORÍAS COMO SELECT NORMAL DESPLEGABLE (SIN CUADRO FEO)
            "categorias": forms.SelectMultiple(
                attrs={
                    "class": "form-select",   # mismo estilo que autor
                    "size": 1                 # hace que sea desplegable y NO gigante
                }
            ),

            "stock": forms.NumberInput(attrs={"class": "form-control"}),
            "fecha_publicacion": forms.DateInput(
                attrs={"type": "date", "class": "form-control"}
            ),
        }

    def clean_stock(self):
        stock = self.cleaned_data.get("stock")
        if stock is not None and stock < 0:
            raise forms.ValidationError("El stock no puede ser negativo.")
        return stock


class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "password1": forms.PasswordInput(attrs={"class": "form-control"}),
            "password2": forms.PasswordInput(attrs={"class": "form-control"}),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
