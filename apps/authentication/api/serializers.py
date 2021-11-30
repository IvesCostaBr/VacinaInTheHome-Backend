from django.utils.functional import empty
from apps.user.models import User
from rest_framework import serializers



class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, min_length=5, write_only=True)
    
    class Meta:
        model = User
        fields = ('email','password', 'token')

        read_only_fields = ['token']
        
    def validate(self, attrs):
        print("Estou validando o aquivo antes de serializar")
        return super().validate(attrs)



