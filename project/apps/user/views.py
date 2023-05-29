from django.shortcuts import redirect, render
from django.urls import reverse

from .models import User


def index(request):
    users_registros = User.objects.all()
    contexto = {"users": users_registros}
    return render(request, "user/index.html", contexto)


def crear_users_predeterminados(request):
    from datetime import date

    # Crear instancias de users
    User.objects.create(nombre="Almendra", apellido="Ruiseñor", nacimiento=date(2015, 1, 1))
    User.objects.create(nombre="Giordana", apellido="Tapello", nacimiento=date(2005, 2, 2))
    User.objects.create(nombre="Macarena", apellido="Litter", nacimiento=date(1990, 3, 3))
    User.objects.create(nombre="Jhiordana", apellido="Perez", nacimiento=date(2005, 2, 2))

    # url = reverse("user:index")
    return redirect("user:index")


def prueba_búsqueda(request):
    from datetime import date

    # Búsqueda por nombre que contenga "dana"
    users_nombre = User.objects.filter(nombre__contains="dana")

    # Búsqueda por fecha de nacimiento mayor a 2000
    users_nacimiento = User.objects.filter(nacimiento__gt=date(2000, 1, 1))

    # Búsqueda por país de origen vacío
    users_pais = User.objects.filter(pais_origen_id=None)

    contexto = {
        "users_nombre": users_nombre,
        "users_nacimiento": users_nacimiento,
        "users_pais": users_pais,
    }
    return render(request, "user/resultados_busqueda.html", contexto)


def crear_user(request):
    from .forms import UserForm

    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("user:index"))
    else:  # method == "GET"
        form = UserForm()
    return render(request, "user/crear.html", {"form": form})