from django.shortcuts import render, redirect
from .models import Estadio
from .forms import EstadioForm, PrecoFinalForm


def listaEstadios(request):
    estadios = Estadio.objects.all()
    return render(request, "estadios.html", {"estadios": estadios})





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


def adicionarEstadio(request):
    form = EstadioForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listaEstadios')
    return render(request, "estadioForm.html", {"form": form})


def escolherEstadio(request, id):
    estadio = Estadio.objects.get(id=id)
    form = PrecoFinalForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listaEstadios')
    return render(request, 'precoFinal.html', {"form": form, "estadio": estadio})


def estadiosEscolhidos(request):
    estadios = Estadio.objects.all()

    return render(request, "estadiosAgendados.html", {"estadios": estadios})
