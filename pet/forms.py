from .models import Dono_pet, Pet
from django import forms




class Dono_pet:
    class Meta:
        pessoa_dono = models.Dono_pet()
        fields = '__all__'