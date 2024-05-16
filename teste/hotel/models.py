from django.db import models
import datetime

TIPOS_QUARTOS = (
    ("SOLTEIRO", "Solteiro"),
    ("CASAL", "Casal"),
    ("CONFORT", "Confort"),
    ("LUXO", "Luxo"),
)


class hotel(models.Model):
    titulo = models.CharField(max_length=50)
    desc = models.TextField(max_length=500)
    logo = models.ImageField(upload_to="logo/")

    def __str__(self):
        return self.titulo


class quarto(models.Model):
    titulo = models.CharField(max_length=50)
    tipo = models.CharField(max_length=15, choices=TIPOS_QUARTOS)
    disponibilidade = models.IntegerField()
    valor = models.FloatField(max_length=9999)
    descricao = models.TextField(max_length=255)
    data_reserva = models.DateTimeField(default=datetime.datetime.now)
    foto_quarto = models.ImageField(upload_to="quartos/")

    def __str__(self):
        return self.tipo


class cadastro(models.Model):
    nome = models.CharField(max_length=20)
    sobrenome = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    tipo_quarto = models.CharField(max_length=15, choices=TIPOS_QUARTOS)
    data_reserva = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.nome
