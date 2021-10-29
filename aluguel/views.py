from django.shortcuts import render
from .models import Estadio

# Funções em python que respondem ao request na urls
def listaEstadios(request):
    estadios = Estadio.objects.all()
    return render(request, "estadios.html", {"estadios": estadios})
