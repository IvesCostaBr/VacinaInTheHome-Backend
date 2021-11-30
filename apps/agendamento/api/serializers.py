from rest_framework import serializers
from ..models import Agendamento
from apps.vacina.api import serializers as vacina_serializers
from apps.user.api import serializers as user_serializers

class AgendamentoSerializer(serializers.ModelSerializer):
    vacina = vacina_serializers.VacinaSerializer(many=False)
    paciente = user_serializers.UserSerializer(many=False)
    
    
    class Meta:
        model = Agendamento
        fields = [
            'uuid', 'data_criacao', 'data_visita', 'obs', 'status', 'vacina', 'paciente'
        ]