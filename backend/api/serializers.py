from .models import *

from rest_framework import serializers


class PessoaSearilizer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = ['id','nome','data_nasc','cpf','sexo','altura','peso']

