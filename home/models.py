from django.db import models


# Create your models here.

class Pessoa(models.Model):
    nome = models.CharField(max_length=15)
    sobrenome = models.CharField(max_length=50)
    nascimento = models.DateField()
    email = models.EmailField()
    usuario = models.CharField(max_length=30)
    senha = models.CharField(max_length=50)
