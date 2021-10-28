from django.shortcuts import render, redirect
from .models import Estadio
from .forms import EstadioForm


def listaEstadios(request):
    estadios = Estadio.objects.all()
    return render(request, "estadios.html", {"estadios": estadios})


def adicionarEstadio(request):
    form = EstadioForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listaEstadios')
    return render(request, "estadioForm.html", {"form": form})


def atualizarEstadio(request, id):
    estadio = Estadio.objects.get(id=id)
    form = EstadioForm(request.POST or None, instance=estadio)

    if form.is_valid():
        form.save()
        return redirect('listaEstadios')
    return render(request, "estadioForm.html", {"form": form, "estadio": estadio})


def deletarEstadio(request, id):
    estadio = Estadio.objects.get(id=id)

    if request.method == "POST":
        estadio.delete()
        return redirect('listaEstadios')
    return render(request, 'estadioDeleteConfirm.html', {'estadio': estadio})


def escolherEstadio(request, id):
    estadio = Estadio.objects.get(id=id)

    return render(request, 'precoFinal.html', {'estadio': estadio})