from django.db import models

class Estadio(models.Model):
    cidade = models.CharField(max_length=40)
    nomeClube = models.CharField(max_length=50)
    donoCampo = models.CharField(max_length=80)
    enderecoCampo = models.CharField(max_length=150)
    comprimentoCampo = models.SmallIntegerField()
    larguraCampo = models.SmallIntegerField()
    precoHora = models.PositiveSmallIntegerField()
    def __str__(self):
        return self.cidade