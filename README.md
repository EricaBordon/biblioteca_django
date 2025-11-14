# Biblioteca – Proyecto Django + DRF

Proyecto educativo que cumple la rúbrica: modelos relacionados, CRUD, autenticación, permisos, admin, templates responsive y API REST.

## Requisitos
- Python 3.10+
- Git (opcional para versionado)

## Instalación (Windows / VS Code)
1. Abrir esta carpeta en VS Code.
2. Abrir terminal (Terminal > New Terminal) y crear entorno:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```
3. Instalar dependencias:
   ```bash
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```
4. Crear archivo `.env` (copiar de `.env.example`) y definir SECRET_KEY y DEBUG.
5. Aplicar migraciones y crear superusuario:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py createsuperuser
   ```
6. Ejecutar servidor:
   ```bash
   python manage.py runserver
   ```

## Funcionalidad
- Modelos: Autor, Categoria, Libro, Prestamo (relaciones FK y M2M) + Usuario (Django)
- CRUD de Autores y Libros (solo staff crea/edita/borra)
- Préstamos: tomar/devolver y manejo de stock
- Autenticación: login, logout, registro
- Permisos: usuarios ven; staff administra
- Admin personalizado
- Templates con Bootstrap 5, responsive, herencia base
- API REST: /api/libros/ y /api/autores/ con búsqueda

## Endpoints API
- GET/POST: /api/autores/
- GET/PUT/PATCH/DELETE: /api/autores/{id}/
- GET/POST: /api/libros/
- GET/PUT/PATCH/DELETE: /api/libros/{id}/
- Auth por sesión o Token (instalar y crear token si deseas)

## Usuarios de prueba
- Crea un superusuario con `createsuperuser` para administrar.
- Regístrate desde /register/ para usuario normal.

## Estructura
- App: catalogo (modelos, vistas, urls, api, serializers, forms)
- Templates: auth, autores, libros, prestamos
- Static: css/styles.css

## Notas
- No subas `.env` ni `venv/` al repo.
- Para requirements actualizados: `pip freeze > requirements.txt`.

## Licencia
Uso educativo.
