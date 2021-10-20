from django.db import models

# Create your models here.

class Carro(models.Model):
    modelo = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    ano = models.IntegerField()
    preco = models.IntegerField()
