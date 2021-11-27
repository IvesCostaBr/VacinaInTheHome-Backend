from rest_framework import serializers
from ..models import Agendamento
from apps.vacina.api import serializers as vacina_serializer

class AgendamentoSerializer(serializers.ModelSerializer):
    vacina = vacina_serializer.VacinaSerializer(many=False)
    
    
    class Meta:
        model = Agendamento
        fields = [
            'uuid', 'data_criacao', 'data_visita', 'obs', 'status', 'vacina'
        ]