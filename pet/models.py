from django.db import models

# Create your models here.

class dono_pet(models.Model):
    nome_completo = models.CharField(max_length=50)
    nome_pet = models.CharField(max_length=50, default='')
    telefone = models.CharField(max_length=20)
    nascimento = models.DateField()
    email = models.EmailField()
    endereco = models.CharField(max_length=30)
    senha = models.CharField(max_length=50)

class pet(models.Model):
    nome_pet = models.ForeignKey(dono_pet, on_delete= models.CASCADE)
    especie = models.CharField(max_length= 40) 
    raça = models.CharField(max_length=50)
    vacina = models.CharField(max_length=50)
    pedigree = models.CharField(max_length=50)
    ração = models.CharField(max_length=50)
