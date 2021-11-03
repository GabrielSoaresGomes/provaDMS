from django import forms
from .models import Estadio, PrecoFinal


class EstadioForm(forms.ModelForm):
    class Meta:
        model = Estadio
        fields = ["cidade", "nomeEstadio", "donoCampo", "enderecoCampo", "comprimentoCampo", "larguraCampo", "precoHora"]


class PrecoFinalForm(forms.ModelForm):
    class Meta:
        model = PrecoFinal
        fields = ["nome", "data"]

