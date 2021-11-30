from django.db.models import fields
from rest_framework import serializers
from ..models import User, Endereco



class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = ['rua', 'numero', 'complemento', 'bairro', 'cidade', 'estado']

class UserSerializer(serializers.ModelSerializer):
    adress = EnderecoSerializer(many=False)
    class Meta:
        model = User
        fields = [ 'uuid', 'cpf', 'first_name' , 'last_name' , 'email', 'card_sus', 'adress' ]


