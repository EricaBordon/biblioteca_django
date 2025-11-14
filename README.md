#  Biblioteca – Proyecto Django + DRF

Proyecto web completo desarrollado con Django, Django REST Framework y Bootstrap 5, siguiendo los criterios de la rúbrica académica:
modelos relacionados, CRUD completo, autenticación, permisos, vistas responsivas, carga de imágenes y API REST funcional.

#  Características principales del sistema
#  Gestión de Biblioteca

- Catálogo completo de libros con portada (ImageField)

- Autores con biografía

- Categorías (M2M)

- Stock dinámico

#  Usuarios

- Registro, login y logout

- Diferencias claras:

- Usuario normal: puede prestar libros y ver su historial

- Administrador (staff): CRUD completo + historial global de préstamos

#  Préstamos

- Tomar préstamo (solo si hay stock)

- Devolver préstamo

- Vista Mis préstamos (usuario normal)

- Vista Préstamos (Admin) con listado global

#  Frontend

- Bootstrap 5

- Templates responsivos

- Imagen completa en portada (cover)

- Cards modernas para libros

#  API REST (DRF)

- Endpoints de Autores y Libros

- CRUD completo

- Paginación

- Búsqueda por título, autor y categoría

#  Requisitos

- Python 3.10+

- Pip actualizado

- Git (opcional)

- Django 4.x

- Django REST Framework

- Pillow (para imágenes)

#  Instalación (Windows / VS Code)

- Abrir el proyecto en VS Code.

- Crear entorno virtual:

python -m venv venv
venv\Scripts\activate


- Instalar dependencias:

pip install --upgrade pip
pip install -r requirements.txt


- Crear archivo .env (copiar de .env.example):

SECRET_KEY=tu_clave_unica
DEBUG=True


- Aplicar migraciones:

python manage.py makemigrations
python manage.py migrate


- Crear superusuario:

python manage.py createsuperuser


- Ejecutar servidor:

python manage.py runserver

#  Estructura del proyecto
biblioteca_project/
catalogo/
    ├── api.py
    ├── forms.py
    ├── models.py
    ├── serializers.py
    ├── urls.py
    ├── views.py
static/
templates/
    ├── auth/
    ├── autores/
    ├── libros/
    ├── prestamos/
manage.py
requirements.txt
.env.example

#  Modelos incluidos
- Autor

- nombre

- bio (opcional)

- Categoría

- nombre

- Libro

- título

- autor (FK)

- categorías (M2M)

- stock

- imagen (portada)

- Préstamo

- usuario

- libro

- fecha_prestamo

- devuelto (bool)

#  Permisos y Roles
Acción	                        Usuario normal	   Staff/Admin
Ver libros	                        ✔	               ✔

Ver autores	                        ✔	               ✔

Crear/Editar/Eliminar autores	      ❌	              ✔

Crear/Editar/Eliminar libros	      ❌	              ✔

Tomar préstamo	                     ✔	               ✔

Ver mis préstamos	                  ✔	               ❌

Ver todos los préstamos	            ❌	               ✔
#  API REST – Endpoints
- Autores
- Método	Endpoint	Función
- GET	/api/autores/	Lista autores
- POST	/api/autores/	Crear autor
- GET	/api/autores/{id}/	Detalle autor
- PUT/PATCH	/api/autores/{id}/	Editar autor
- DELETE	/api/autores/{id}/	Eliminar autor
- Libros
- Método	Endpoint	Función
- GET	/api/libros/	Lista libros
- POST	/api/libros/	Crear libro
- GET	/api/libros/{id}/	Detalle libro
- PUT/PATCH	/api/libros/{id}/	Editar libro
- DELETE	/api/libros/{id}/	Eliminar libro
#  Usuarios de prueba

- Crear administrador:

python manage.py createsuperuser


- Registro de usuario normal:

/register/

#  Notas importantes

- No subir .env, venv/ ni la base de datos.
- Para actualizar dependencias:
- pip freeze > requirements.txt
