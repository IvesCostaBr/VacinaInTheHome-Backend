from .models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [ 'id', 'cpf', 'first_name' , 'last_name' , 'email' ]


class LoginSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=128, min_length=5, write_only=True)
    
    class Meta:
        model = User
        fields = ('email', 'password', 'token')

        read_only_fields = ['token']



