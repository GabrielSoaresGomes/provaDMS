import dateutil.utils
from django.db import models
from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime


class Estadio(models.Model):

    cidade = models.CharField('Cidade', max_length=40)
    nomeEstadio = models.CharField('Nome do Estadio', max_length=50)
    donoCampo = models.CharField('Dono do Campo', max_length=80)
    enderecoCampo = models.CharField('Endereço do Campo', max_length=150)
    comprimentoCampo = models.SmallIntegerField('Comprimento do Campo')
    larguraCampo = models.SmallIntegerField('Largura do Campo')
    precoHora = models.PositiveSmallIntegerField('Preço por Hora')

    def __str__(self):
        return self.cidade


class PrecoFinal(models.Model):
    estadio = Estadio.nomeEstadio
    data = models.DateField("Insira a data no formato MM/DD/YYYY : ")

    def __str__(self):
        return self.data

