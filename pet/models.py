from django.db import models

# Create your models here.

class Dono_bicho(models.Model):
    nome_completo = models.CharField(max_length=50)
    telefone = models.CharField(max_length=20)
    nascimento = models.DateField()
    email = models.EmailField()
    endereco = models.CharField(max_length=30)
    senha = models.CharField(max_length=50)
