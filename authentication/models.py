from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings as conf
from .managers import UserManager
import jwt
import datetime


class User(AbstractBaseUser, PermissionsMixin):
    cpf = models.CharField(max_length=12)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = None
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    token = models.CharField(max_length=129, default=None, null=True)

    USERNAME_FIELD = 'email'
    #TODO:Alterar em produção
    objects = UserManager()
    
    @property
    def token(self):
        token = jwt.encode({'username':self.username,
        'email':self.email,
        'exp':datetime.datetime.utcnow() + datetime.timedelta(hours=24)},conf.SECRET_KEY, algorithm='HS256')

        return token

    class Meta:
        permissions = [
            ('user_public', 'user default acess'),
        ]

