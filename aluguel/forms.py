from django import forms
from .models import Estadio

class EstadioForm(forms.ModelForm):
    class Meta:
        model = Estadio
        fields = ["cidade", "nomeEstadio", "donoCampo", "enderecoCampo", "comprimentoCampo", "larguraCampo", "precoHora"]