from rest_framework import serializers
from ..models import Vacina


class VacinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacina
        fields = ('uuid', 'vacina_type')

