from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *

class ClienteSerializer(serializers.ModelSerializer):
    """ Exibindo todos os clientes """
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate(self, data):
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome':'O campo nome não pode conter números'})
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'rg':'O campo RG é inválido'})
        data['cpf'] = cpf_valido(data['cpf'])
        if not data['cpf']:
            raise serializers.ValidationError({'cpf':'O campo CPF é inválido'})
        data['celular'] = celular_valido(data['celular'])
        if not data['celular']:
            raise serializers.ValidationError({'celular':'O campo celular é inválido (XX)XXXXX-XXXX'})
        return data
