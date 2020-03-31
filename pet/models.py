from django.db import models
from django import forms


# Create your models here.

class Dono_pet(models.Model):
    nome_completo = models.CharField(max_length=50)
    telefone = models.CharField(max_length=20)
    nascimento = models.DateField()
    email = models.EmailField()
    endereco = models.CharField(max_length=30)


class Pet(models.Model):
    especie = models.CharField(max_length= 40) 
    raça = models.CharField(max_length=50)
    vacina = models.CharField(max_length=50)
    pedigree = models.CharField(max_length=50)
    ração = models.CharField(max_length=50)



# nome_pet = models.ForeignKey('pet.Dono_pet', on_delete=models.PROTECT, null = True)


