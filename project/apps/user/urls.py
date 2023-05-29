from django.urls import path

from .views import crear_user, crear_users_predeterminados, index, prueba_búsqueda

# Es necesario este nombre, para ser llamado desde la plantila,
# por ejemplo: {% url 'user:index' %}
app_name = "user"

urlpatterns = [
    path("", index, name="index"),
    path("crear-users-predeterminados/", crear_users_predeterminados, name="crear-users"),
    path("prueba-búsqueda/", prueba_búsqueda, name="prueba-búsqueda"),
    path("crear/", crear_user, name="crear"),
]