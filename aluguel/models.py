from django.db import models

class Estadio(models.Model):

    cidade = models.CharField('Cidade', max_length=40, default="oi")
    nomeEstadio = models.CharField('Nome do Estadio', max_length=50, default="oi")
    donoCampo = models.CharField('Dono do Campo', max_length=80, default="oi")
    enderecoCampo = models.CharField('Endereço do Campo', max_length=150, default="oi")
    comprimentoCampo = models.SmallIntegerField('Comprimento do Campo')
    larguraCampo = models.SmallIntegerField('Largura do Campo')
    precoHora = models.PositiveSmallIntegerField('Preço por Hora')

    def __str__(self):
        return self.cidade


class PrecoFinal(models.Model):
    nome = models.CharField("", max_length=50)
    data = models.CharField("Insira a data no formato DD/MM/YYYY", max_length=10)
    horas = models.SmallIntegerField("Insira por quantas horas deseja alugar")
    valorFinal = models.FloatField("")

    def __str__(self):
        return self.data

