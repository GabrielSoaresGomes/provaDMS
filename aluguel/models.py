from django.db import models


class Estadio(models.Model):
    CIDADE_CHOICES = (
        ("Valença", "Valença"),
        ("Barra do Piraí", "Barra do Piraí"),
        ("Paracambi", "Paracambi"),
        ("Vassouras", "Vassouras"),
    )

    cidade = models.CharField('Cidade', choices=CIDADE_CHOICES, max_length=40)
    nomeEstadio = models.CharField('Nome do Estadio', max_length=50)
    donoCampo = models.CharField('Dono do Campo', max_length=80)
    enderecoCampo = models.CharField('Endereço do Campo', max_length=150)
    comprimentoCampo = models.SmallIntegerField('Comprimento do Campo')
    larguraCampo = models.SmallIntegerField('Largura do Campo')
    precoHora = models.PositiveSmallIntegerField('Preço por Hora')

    def __str__(self):
        return self.cidade