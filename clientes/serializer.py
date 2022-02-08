from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *
import re

class ClienteSerializer(serializers.ModelSerializer):
    """ Exibindo todos os clientes """
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate(self, data):
        # Validando o campo do nome
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome':'O campo nome não pode conter números'})
        # Validando o campo do RG
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'rg':'O campo RG é inválido'})
        # Validando o campo de CPF, colocando pontuações se não possuir
        data['cpf'] = cpf_valido(data['cpf'])
        if not data['cpf']:
            raise serializers.ValidationError({'cpf':'O campo CPF é inválido'})
        # Validando o campo número de celular, colocando pontuações se não possuir
        data['celular'] = celular_valido(data['celular'])
        if not data['celular']:
            raise serializers.ValidationError({'celular':'O campo celular é inválido (XX)XXXXX-XXXX'})
        return data
