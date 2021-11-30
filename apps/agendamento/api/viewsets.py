from rest_framework import authentication, viewsets
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from apps.agendamento.models import Agendamento
from .serializers import AgendamentoSerializer
from rest_framework.status import *


class AgendamentoViewSet(viewsets.ModelViewSet):
    serializer_class=AgendamentoSerializer
    authentication_classes = [JSONWebTokenAuthentication,]
    permission_classes = [IsAuthenticated,]
    
    def get_queryset(self):
        if self.request.user.is_staff:
            list_agendamentos = Agendamento.objects.all()
            if list_agendamentos:
                return list_agendamentos
        else:
            list_agendamentos = Agendamento.objects.filter(paciente=self.request.user)
            if list_agendamentos:
                return list_agendamentos
            
            
    def retrieve(self, request, pk , *args, **kwargs):
        user_request = self.request.user
        agendamento = Agendamento.objects.get(uuid=pk)
        if agendamento:
            if agendamento.paciente == user_request or user_request.is_superuser:
                data = self.serializer_class(agendamento).data
                return Response(data)
                
        return Response({"message":"operation not allowed"}, HTTP_403_FORBIDDEN)
        
            
            