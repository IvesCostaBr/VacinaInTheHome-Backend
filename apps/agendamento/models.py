from django.db import models
from apps.user.models import User, Endereco
from apps.vacina.models import Vacina
import uuid



class Agendamento(models.Model):
    STATUS = (
        ("1", "Concuildo"),
        ("2", "Agendado"),
        ("3", "Cancelado"),
        ("4", "Em Analise")
    )
    
    
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    data_criacao = models.DateTimeField('Data',auto_now_add=True)
    data_visita = models.DateTimeField(null=True, blank=True)
    obs =  models.CharField(max_length=120, blank=True)
    status =  models.CharField(max_length=10, choices=STATUS, default=STATUS[3])
    paciente = models.ForeignKey(User, on_delete=models.PROTECT, null=False, blank=False)
    vacina = models.OneToOneField(Vacina, on_delete=models.PROTECT, null=True, blank=False)
    endreco_visita = models.OneToOneField(Endereco, on_delete=models.PROTECT, null=True, blank=True)
    
    