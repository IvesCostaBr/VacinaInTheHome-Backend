from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _
from .managers import UserManager
from rest_framework_jwt.settings import api_settings
import uuid

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class Endereco(models.Model):
    rua = models.CharField(max_length=60)
    numero = models.IntegerField()
    complemento = models.CharField(max_length=40, null=True, blank=True)
    bairro = models.CharField(max_length=40)
    cidade = models.CharField(max_length=60)
    estado = models.CharField(max_length=40, default="Acre")
    


class User(AbstractBaseUser, PermissionsMixin):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cpf = models.CharField(max_length=12)
    rg = models.CharField(max_length=15, null=True, blank=True)
    mother = models.CharField(max_length=60, null=True, blank=True)
    data_nascimento = models.DateField(blank=True, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = None
    email = models.EmailField(_('email address'), unique=True)
    card_sus =  models.CharField(max_length=20)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    #TODO: Trocar OneToOneField por um ForeingKey
    adress =  models.OneToOneField(Endereco, 
                                   on_delete=models.CASCADE, null=True, blank=True)
    
    
    
    

    USERNAME_FIELD = 'email'
    #TODO:Alterar em produção
    objects = UserManager()
    
    @property
    def token(self):
        payload = jwt_payload_handler(self)
        token = jwt_encode_handler(payload)
        
        return token
    
    class Meta:
        permissions = [
            ('user_public', 'acesso default'),
            ('user_base', 'usuario com vacina')
        ]
