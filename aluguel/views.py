from django.shortcuts import render, redirect
from .models import Estadio, PrecoFinal
from .forms import EstadioForm, PrecoFinalForm


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
        return redirect('estadiosEscolhidos')
    return render(request, 'precoFinal.html', {"form": form, "estadio": estadio})


def listaEstadios(request):
    estadios = Estadio.objects.all()
    return render(request, "estadios.html", {"estadios": estadios})


def estadiosEscolhidos(request):
    estadios = PrecoFinal.objects.all()

    return render(request, "estadiosAgendados.html", {"estadios": estadios})


def atualizarEstadio(request, id):
    editar = False
    estadio = Estadio.objects.get(id=id)
    form = EstadioForm(request.POST or None, instance=estadio)

    if form.is_valid():
        form.save()
        return redirect('listaEstadios')
    editar = True
    return render(request, "estadioForm.html", {"form": form, "estadio": estadio, "editar": editar, })


def atualizarEscolhido(request, id):
    alugado = PrecoFinal.objects.get(id=id)
    form = PrecoFinalForm(request.POST or None, instance=alugado)

    if form.is_valid():
        form.save()
        return redirect('estadiosEscolhidos')
    return render(request, "precoFinal.html", {"form": form, "alugado": alugado, })


def deletarEstadio(request, id):
    estadio = Estadio.objects.get(id=id)

    if request.method == "POST":
        estadio.delete()
        return redirect('listaEstadios')
    return render(request, 'estadioDeleteConfirm.html', {'estadio': estadio})


def deletarEscolhido(request, id):
    estadio = PrecoFinal.objects.get(id=id)

    if request.method == "POST":
        estadio.delete()
        return redirect('estadiosEscolhidos')
    return render(request, 'estadioAgendadoDelete.html', {'estadio': estadio})



