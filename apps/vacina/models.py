from django.db import models
import uuid



class Vacina(models.Model):
    VACINAS_DISPONIVEIS = (
    ("Outra", "Sem indentificação"),
    ("Pfizer", "pfizer"),
    ("Astrazenica", "astra"),
    ("CoronaVAC", "coronavac"),
    ("Febre Amarela", "fba"),
    ("Girpe", "gripe")
)
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    vacina_type = models.CharField(max_length=30,choices=VACINAS_DISPONIVEIS)
    
