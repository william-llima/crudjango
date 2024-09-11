from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Pessoa(models.Model):
    nome = models.CharField(max_length=300)
    data_nasc = models.DateField()
    cpf = models.CharField(max_length=20)
    sexo = models.CharField(max_length=1)
    altura = models.FloatField(max_length=2)
    peso = models.FloatField(max_length=10)
